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
    if request.method == 'POST' and request.FILES:
        uploaded_video = request.FILES['video']
        fs = FileSystemStorage()
        name = fs.save(uploaded_video.name, uploaded_video)
        context['upload_url'] = fs.url(name)
        video_name = detectVideo(name)
        context['counted_url'] = fs.url(video_name)
    return render(request, 'upload_video.html', context)


def create_mask(frame, kernel, subtractor):
    # Apply the frame to the subtractor
    mask = subtractor.apply(frame)

    # Remove noise in the mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    _, mask= cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)
    return mask

def count_people(frame, mask):
    # Find the contours on the mask that was just thresholded
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # List of bounding rectangles
    new_contours = np.array([cv2.boundingRect(contour) for contour in contours if cv2.contourArea(contour) > 200])
    
    # Get a list of all rectangles
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in new_contours])
    
    # Perform non maxima supression on the list of rectangles
    nms_rects = non_max_suppression(rects, probs=None, overlapThresh=0.2)
    
    # Draw the supressed rectangles
    [cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2) for (xA, yA, xB, yB) in nms_rects]
    
    # Return the number of rectangles drawn i.e. the number of people
    return len(nms_rects)

def detectVideo(video_name):
    filename = os.path.abspath(os.path.join(MEDIA_ROOT, video_name))

    print("Running Application Human Counter")

    # Initiate video capture for video file, here we are using the video file in which pedestrians would be detected
    cap = cv2.VideoCapture(filename)

    # Extract parameters about the video, such as the resolution, video length and fps
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    name = 'counted_' + video_name

    # Define the video writer for the output file
    fourcc = cv2.VideoWriter_fourcc('a','v','c','1')
    out = cv2.VideoWriter(os.path.abspath(os.path.join(MEDIA_ROOT, name)), fourcc, fps, (width, height))

    # Define the subtractor and kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    subtractor = cv2.createBackgroundSubtractorMOG2()

    frame_num = 1
    while cap.isOpened():
        ret, frame = cap.read()

        if frame is None:
            break
        
        print('INFO: Processing frame {}/{}.'.format(frame_num, num_frames))

        # Create a mask containing all pixels which are different from the background image
        mask = create_mask(frame, kernel, subtractor)

        # Form contours around the mask to count the number of people in the image
        num_people = count_people(frame, mask)

        # Write the number of people to the image
        cv2.putText(img=frame,
                    text="Number of People: {}".format(num_people),
                    org=(10, 40),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1,
                    color=(0, 0, 255),
                    thickness=3)
        
        out.write(frame) # Write the processed frame
        frame_num += 1  # Increment the frame counter for INFO logs

    cap.release()
    out.release()

    return name
