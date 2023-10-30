from typing import Dict, List, Literal, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Maize Cobs"
PROJECT_NAME_FULL: str = "Maize Cobs: A Dataset for DeepCob Analysis"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_NC_2_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [
    Industry.Agricultural(),
    Research.Genetic(),
]
CATEGORY: Category = Category.Agriculture(extra=Category.Biology())

CV_TASKS: List[CVTask] = [
    CVTask.InstanceSegmentation(),
    CVTask.SemanticSegmentation(),
    CVTask.ObjectDetection(),
]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.InstanceSegmentation()]

RELEASE_DATE: Optional[str] = "2021-03-08"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://zenodo.org/record/4587304#.Yk_ePH9Bzmg"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 1671450
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/maize-cobs"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "ImgCross-training-data": "https://zenodo.org/record/4587304/files/ImgCross-training-data.zip?download=1",
    "ImgOldImgNew-training-data": "https://zenodo.org/record/4587304/files/ImgCross-training-data.zip?download=1",
    "ImgOldImgNew-validation-data": "https://zenodo.org/record/4587304/files/ImgOldImgNew-validation-data.zip?download=1",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "ruler": [139, 87, 42],
    "cob": [74, 144, 226],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = "https://plantmethods.biomedcentral.com/articles/10.1186/s13007-021-00787-6"
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = {"GitLab":"https://gitlab.com/kjschmidlab/deepcob"}


CITATION_URL: Optional[str] = "https://zenodo.org/record/4587304/export/hx"
AUTHORS: Optional[List[str]] = [
    "Lydia Kienbaum",
    "Miguel Correa Abondano",
    "Raul Blas",
    "Karl Schmid",
]
AUTHORS_CONTACTS: Optional[List[str]] = ["karl.schmid@uni-hohenheim.de"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = ["University of Hohenheim, Germany"]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://www.uni-hohenheim.de/en/organization/institution/institute-of-plant-breeding-seed-science-and-population-genetics?tx_base_lsfcontentadmin%5Baction%5D=listLsfPublicationsOfLsfInstitution&cHash=bd559ee87a896ffd4afe80dd6dcd400c"
]
SLYTAGSPLIT: Dict[str, List[str]] = {
    "versions": [
        "ImgCross-training-data",
        "ImgOldImgNew-training-data-1000",
        "ImgOldImgNew-validation-data",
    ]
}
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
