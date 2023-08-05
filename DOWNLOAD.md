Dataset **Maize Cobs** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/U/k/Kx/BzmFPQWQ7Vt9msUvWY0dqO5ZWsbTW74HeDZfsbK04jywsm5sVLAp0rHyjvwJSOJyPp9CN66RxtluMVjSaGffEf2n3qJJHLHg135YNv2wWSiU1A0dt8Ti6ELXNCuJ.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Maize Cobs', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [ImgCross-training-data](https://zenodo.org/record/4587304/files/ImgCross-training-data.zip?download=1)
- [ImgOldImgNew-training-data](https://zenodo.org/record/4587304/files/ImgCross-training-data.zip?download=1)
- [ImgOldImgNew-validation-data](https://zenodo.org/record/4587304/files/ImgOldImgNew-validation-data.zip?download=1)
