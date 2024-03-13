# Hard Drive Failure Prediction

This is the final solution created to support my dissertation which explores hard drive disk prediction based machine learning for lightweight devices. The purpose is to find the most optimal model for lightweight devices which has a good cross between a fast testing time and other metrics such as F1 score, recall, accuracy, etc.

The final solution was built using the LightGBM model.

![image](https://github.com/F2ncy/HDD-Prediction/assets/78828685/901e789c-b0f0-4c82-a062-4646dde1bfac)

## Requirements
- [Docker](https://pimylifeup.com/raspberry-pi-docker/)
- [Python](https://www.python.org/downloads/)

## Run With Docker
### Image
[ghcr.io/f2ncy/disk_failure_prediction](https://ghcr.io/f2ncy/disk_failure_prediction)

- docker run --privileged -v hddpredict:/predictt -i --device=/dev/sda -p 5001:5000 disk_failure_prediction:latest

Supports the following platforms:
- linux/arm64

### Volumes
In order to get predictions you must define which device you want the model to predict on within the code. This requires changing one line

![image](https://github.com/F2ncy/HDD-Prediction/assets/78828685/de5af1c6-eda4-41e8-ae51-7d2db1616c80)

Define ``"device_path"`` to whichever drive you would like the prediction to be made on (e.g. ``/dev/sda``, ``sdb``, etc)

This requires the ``docker run`` command to be modified appropriately:

- docker run --privileged -v hddpredict:/predictt -i --device=``/dev/sda`` -p 5001:5000 disk_failure_prediction:latest

## Additional Information
``Prediction: 0`` - Indicates the model thinks the drive will not fail

``Prediction: 1`` - Indicates the model thinks the drive is highly likely to fail

Works with all types of drives including ATA, SATA, NVME, etc.
