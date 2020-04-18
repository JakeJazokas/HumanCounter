from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from HumanCounter.settings import MEDIA_ROOT
from HumanCounter.settings import STATICFILES_DIRS
from HumanCounter.utils import yolo_utils as utils
import os
import time
import numpy as np
import cv2

# Create your views here.
def upload_video_yolo(request):
    context = {}
    if request.method == 'POST' and request.FILES:
        uploaded_video = request.FILES['video']
        fs = FileSystemStorage()
        name = fs.save(uploaded_video.name, uploaded_video)
        context['upload_url'] = fs.url(name)
        # Count people in video
        video_name = detectVideo(name)
        context['counted_url'] = fs.url(video_name)
    return render(request, 'upload_video_yolo.html', context)


def count_frame(model, frame):
    shape = frame.shape[:2]

    # Build a blob from the frame
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
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

    return utils.drawBoxes(frame, boxes, confidences)


def detectVideo(video_name):
    # Fetch the pre-trained model
    model = utils.build_network_model()

    # Define the input video file path
    filename = os.path.abspath(os.path.join(MEDIA_ROOT, video_name))
    
    # Create video capture
    cap = cv2.VideoCapture(filename)

    # Extract parameters about the video, such as the resolution, video length and fps
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Define the output file name
    processed_video_name = 'counted_' + video_name

    # Define the video writer for the output file
    fourcc = cv2.VideoWriter_fourcc('a', 'v', 'c', '1')
    out = cv2.VideoWriter(os.path.abspath(os.path.join(MEDIA_ROOT, processed_video_name)), fourcc, fps, (width, height))

    frame_num = 1
    while cap.isOpened():
        _, frame = cap.read()  # Read a frame

        # If we reach end of file stop reading
        if frame is None:
            break
            
        print('INFO: Processing frame {}/{}.'.format(frame_num, num_frames))
        frame, num_people = count_frame(model, frame)  # Process the frame

        # Write the number of people detected on the image
        cv2.putText(img=frame,
                    text="Number of People: {}".format(num_people),
                    org=(10,40),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1,
                    color=(0, 0, 255),
                    thickness=3)

        out.write(frame)  # Write the processed frame
        frame_num += 1  # Increment the frame counter for INFO logs

    cap.release()
    out.release()

    return processed_video_name
