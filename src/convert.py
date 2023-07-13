# https://zenodo.org/record/4587304#.Yk_ePH9Bzmg

import os

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.io.fs import (
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)
from supervisely.io.json import load_json_file

# if sly.is_development():
# load_dotenv("local.env")
# load_dotenv(os.path.expanduser("~/supervisely.env"))

# api = sly.Api.from_env()
# team_id = sly.env.team_id()
# workspace_id = sly.env.workspace_id()


# project_name = "maize cob"
# dataset_path = "/home/alex/DATASETS/TODO/maize cob/ImgCross-training-data"

all_folders = [
    "./APP_DATA/maize-cobs/ImgCross-training-data/train",
    "./APP_DATA/maize-cobs/ImgCross-training-data/val",
    "./APP_DATA/maize-cobs/ImgOldImgNew-training-data-1000/train",
    "./APP_DATA/maize-cobs/ImgOldImgNew-training-data-1000/val",
    "./APP_DATA/maize-cobs/ImgOldImgNew-validation-data/val",
]

ds_names = [
    "train",
    "val",
    "train",
    "val",
    "val",
]
batch_size = 30
images_ext = ".jpg"
ann_file_name = "via_region_data.json"


def create_ann(image_path: str, image_to_ann_data, meta):
    labels = []

    image_np = sly.imaging.image.read(image_path)[:, :, 0]
    img_height = image_np.shape[0]
    img_wight = image_np.shape[1]

    regions = image_to_ann_data.get(get_file_name_with_ext(image_path))

    if regions is not None:
        for region in regions:
            class_name_dict = region["region_attributes"]["name"]
            for curr_name, bool_val in class_name_dict.items():
                if bool_val is True:
                    obj_class = meta.get_obj_class(curr_name)

            exterior = []
            x_coords = region["shape_attributes"]["all_points_x"]
            y_coords = region["shape_attributes"]["all_points_y"]
            for x, y in zip(x_coords, y_coords):
                exterior.append([int(y), int(x)])

            poligon = sly.Polygon(exterior)
            label_poly = sly.Label(poligon, obj_class)
            labels.append(label_poly)

    tag_name = image_path.split("/")[-3]
    tags = [sly.Tag(tag_meta) for tag_meta in tag_metas if tag_meta.name == tag_name]

    return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=tags)


obj_class_cob = sly.ObjClass("cob", sly.Polygon)
obj_class_ruler = sly.ObjClass("ruler", sly.Polygon)

tag_names = [
    "ImgCross-training-data",
    "ImgOldImgNew-training-data-1000",
    "ImgOldImgNew-validation-data",
]
tag_metas = [sly.TagMeta(name, sly.TagValueType.NONE) for name in tag_names]


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class_cob, obj_class_ruler], tag_metas=tag_metas)
    api.project.update_meta(project.id, meta.to_json())

    already_created = []
    for ds_name, curr_data_path in zip(ds_names, all_folders):
        if ds_name not in already_created:
            dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)
        else:
            dataset = api.dataset.get_info_by_name(project.id, ds_name)
        already_created.append(ds_name)

        # curr_data_path = os.path.join(dataset_path, ds_name)
        ann_file_path = os.path.join(curr_data_path, ann_file_name)
        ann_data = load_json_file(ann_file_path)
        image_to_ann_data = {}
        img_metadata = ann_data["_via_img_metadata"]
        for curr_data in list(img_metadata.values()):
            regions = curr_data["regions"]
            image_to_ann_data[curr_data["filename"]] = regions

        images_names = [
            item for item in os.listdir(curr_data_path) if get_file_ext(item).lower() == images_ext
        ]
        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

        for img_names_batch in sly.batched(images_names, batch_size=batch_size):
            img_pathes_batch = [
                os.path.join(curr_data_path, im_name) for im_name in img_names_batch
            ]

            img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = [
                create_ann(image_path, image_to_ann_data, meta) for image_path in img_pathes_batch
            ]
            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(img_names_batch))

    return project
