from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from HumanCounter.settings import MEDIA_ROOT
from HumanCounter.utils import yolo_utils as utils
import os
import time
import argparse
import numpy as np
import cv2


# Create your views here.
def upload_image_yolo(request):
    context = {}
    if request.method == 'POST' and request.FILES:
        uploaded_image = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save(uploaded_image.name, uploaded_image)
        context['upload_url'] = fs.url(name)
        img, num_people = count_people(name)
        context['counted_url'] = fs.url(img)
        context['counted_num'] = num_people
    return render(request, 'upload_image_yolo.html', context)


def count_people(image_name):
    # Fetch the pre-trained model
    model = utils.build_network_model()

    # Define the input video file path
    filename = os.path.abspath(os.path.join(MEDIA_ROOT, image_name))

    # Read the image
    image = cv2.imread(filename)

    shape = image.shape[:2]

    # Build a blob from the image
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    model.setInput(blob)

    # Extract the outputs from each classifier
    layerOutputs = model.forward(['yolo_82', 'yolo_94', 'yolo_106'])

    boxes = []
    confidences = []
    # loop over each of the layer outputs
    for output in layerOutputs:
        # loop over each of the detections
        for detection in output:
            boxes, confidences = utils.parse_detection(detection, shape, boxes, confidences)

    image, num_people = utils.drawBoxes(image, boxes, confidences)

    # Write the number of people to the image
    cv2.putText(img=image,
                text="Number of People: {}".format(num_people),
                org=(10, 40),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1,
                color=(0, 0, 255),
                thickness=3)

    name = 'counted_' + image_name
    cv2.imwrite(os.path.abspath(os.path.join(MEDIA_ROOT, name)), image)
    return name, num_people
