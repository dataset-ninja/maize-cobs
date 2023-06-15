**Maize Cobs: A Dataset for DeepCob Analysis** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the agriculture industry.

The dataset consists of 1250 images with 8935 labeled objects belonging to 2 different classes including *ruler* and *cob*.

Each image in the Maize Cobs dataset has pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. All images are labeled (i.e. with annotations). There are 5 splits in the dataset: *ImgOldImgNew-validation-data_val* (100 images), *ImgOldImgNew-training-data-1000_val* (250 images), *ImgOldImgNew-training-data-1000_train* (750 images), *ImgCross-training-data_val* (100 images), and *ImgCross-training-data_train* (50 images). The dataset was released in 2021 by the [University of Hohenheim, Germany](https://www.uni-hohenheim.de/en/organization/institution/institute-of-plant-breeding-seed-science-and-population-genetics?tx_base_lsfcontentadmin%5Baction%5D=listLsfPublicationsOfLsfInstitution&cHash=bd559ee87a896ffd4afe80dd6dcd400c).

Here is the visualized example grid with annotations:

<img src="https://github.com/dataset-ninja/maize-cobs/raw/main/visualizations/side_annotations_grid.png">
