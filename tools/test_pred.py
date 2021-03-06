import matplotlib.pyplot as plt
import numpy as np

from darkflow.net.build import TFNet
import cv2


options = {"model": "cfg/new_tiny.cfg", "load": "bin/yolov2-tiny.weights", "threshold": 0.1, "labels": "cfg/coco.names"}

tfnet = TFNet(options)

imgcv = cv2.imread("./darkflow/sample_img/sample_dog.jpg")
result = tfnet.return_predict(imgcv)
print(result)