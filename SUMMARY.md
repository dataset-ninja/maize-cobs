**Maize Cobs: A Dataset for DeepCob Analysis** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the agricultural industry, and in the genetic research. 

The dataset consists of 1250 images with 8905 labeled objects belonging to 2 different classes including *ruler* and *cob*.

Images in the Maize Cobs dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 4 (0% of the total) unlabeled images (i.e. without annotations). There are 2 splits in the dataset: *train* (800 images) and *val* (450 images). Alternatively, the dataset could be split into 3 versions: <span style="background-color: #ecdefc; padding: 2px 4px; border-radius: 4px;">ImgCross-training-data</span> (150 images), <span style="background-color: #ecdefc; padding: 2px 4px; border-radius: 4px;">ImgOldImgNew-training-data-1000</span> (1000 images), and <span style="background-color: #ecdefc; padding: 2px 4px; border-radius: 4px;">ImgOldImgNew-validation-data</span> (100 images). The dataset was released in 2021 by the University of Hohenheim, Germany.

Here is the visualized example grid with animated annotations:

[animated grid](https://github.com/dataset-ninja/maize-cobs/raw/main/visualizations/horizontal_grid.webm)
