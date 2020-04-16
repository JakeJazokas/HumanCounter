from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from HumanCounter.settings import MEDIA_ROOT

import time
import cv2
import os
import imutils
from imutils.object_detection import non_max_suppression
import numpy as np

# Create your views here.
def upload_video(request):
    context = {}
    if request.method == 'POST':
        uploaded_video = request.FILES['video']
        fs = FileSystemStorage()
        name = fs.save(uploaded_video.name, uploaded_video)
        context['upload_url'] = fs.url(name)

        video_name = detectVideo(name)
        context['counted_url'] = fs.url(video_name)

        print(fs.url(video_name))
    return render(request, 'upload_video.html', context)

#create the mask
def create_mask(frame,kernel,fgbg):
    mask = fgbg.apply(frame)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    _, mask= cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)
    return mask

def create_contours(frame,mask):
    # Find the contours on the mask that was just thresholded
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # List of bounding rectangles
    new_contours = np.array([cv2.boundingRect(contour) for contour in contours if cv2.contourArea(contour) > 200])
    # Get a list of all rectangles
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in new_contours])
    # Perform non maxima supression on the list of rectangles
    nms_rects = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    # Draw the supressed rectangles
    [cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2) for (xA, yA, xB, yB) in nms_rects]
    # Return the number of rectangles drawn i.e. the number of people
    return len(nms_rects)

def detectVideo(video_name):
    filename = os.path.abspath(os.path.join(MEDIA_ROOT, video_name))

    print("Running Application Human Counter")

    # Initiate video capture for video file, here we are using the video file in which pedestrians would be detected
    cap = cv2.VideoCapture(filename)

    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    fourcc = cv2.VideoWriter_fourcc('a','v','c','1')

    name = 'counted_' + video_name
    out = cv2.VideoWriter(os.path.abspath(os.path.join(MEDIA_ROOT, name)), fourcc, 20.0, (width, height))

    # Loop once video is successfully loaded
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    fgbg = cv2.createBackgroundSubtractorMOG2()

    while cap.isOpened():
        ret, frame = cap.read()

        if frame is None:
            break
        
        mask = create_mask(frame,kernel,fgbg)
        num_people = create_contours(frame,mask)

        indices = np.where(mask == 0)

        cv2.putText(frame, 
                    "Number of People: {}".format(num_people), 
                    (10, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)

        out.write(frame)

    cap.release()
    out.release()

    # name = fs.save('counted_2_' + video_name, fs.open(os.path.abspath(os.path.join(MEDIA_ROOT, name))))
    return name