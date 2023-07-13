**Maize Cobs: A Dataset for DeepCob Analysis** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the agricultural industry and genetic research. 

The dataset consists of 1250 images with 8905 labeled objects belonging to 2 different classes including *ruler* and *cob*.

Images in the Maize Cobs dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 4 (0% of the total) unlabeled images (i.e. without annotations). There are 2 splits in the dataset: *train* (800 images) and *val* (450 images). Alternatively, dataset could be splitted by <i>version</i> criteria: *ImgCross-training-data* (150 images), *ImgOldImgNew-training-data-1000* (1000 images), and *ImgOldImgNew-validation-data* (100 images). The dataset was released in 2021 by the [University of Hohenheim, Germany](https://www.uni-hohenheim.de/en/organization/institution/institute-of-plant-breeding-seed-science-and-population-genetics?tx_base_lsfcontentadmin%5Baction%5D=listLsfPublicationsOfLsfInstitution&cHash=bd559ee87a896ffd4afe80dd6dcd400c).

Here is the visualized example grid with annotations:

<img src="https://github.com/dataset-ninja/maize-cobs/raw/main/visualizations/side_annotations_grid.png">
