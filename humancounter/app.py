
import cv2
import numpy as np
import humancounter.resources.cascades.cascadeHandler as classifier
import humancounter.resources.videos.videoHandler as videos
from humancounter.resources.tracking.trackable import Trackable
from humancounter.resources.tracking.tracker import Tracker
import time

def create_mask(frame,kernel,fgbg):#create the mask
    mask = fgbg.apply(frame)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    _, mask= cv2.threshold(mask, 210, 255, cv2.THRESH_BINARY)

    cv2.imshow("mask", mask)

    return mask


def create_contours(frame,mask):
    # Find the contours on the mask that was just thresholded
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    people = []
    for contour in contours:
        # Create a bounding rectangle from the contour
        (x, y, w, h) = cv2.boundingRect(contour)

        # Draw the rectangle on the current frame
        if cv2.contourArea(contour) > 200:
            centerCoord = (int(x+(w/2)), int(y+(h/2)))
            people.append(Trackable(centerCoord, (x, y, w, h)))
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return people


def detectVideo(video):
    print("Running Application Human Counter")

    # Create our body classifier
    body_classifier = classifier.body()

    # Initiate video capture for video file, here we are using the video file in which pedestrians would be detected
    cap = cv2.VideoCapture(video)

    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('output/output.avi', fourcc, 20.0, (768, 576))

    # Loop once video is successfully loaded
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))
    fgbg = cv2.createBackgroundSubtractorMOG2()


    tracker = Tracker()

    while cap.isOpened():
        ret, frame = cap.read()

        if frame is None:
            break
        
        mask = create_mask(frame,kernel,fgbg)
        people = create_contours(frame,mask)

        tracker.track(people)

        indices = np.where(mask == 0)

        num_people = tracker.count()

        cv2.putText(frame,  "Number of People: {}".format(num_people),  (10, 40),  cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        out.write(frame)
        cv2.imshow('frame', frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        
        if k == 13: #13 is the Enter Key
            time.sleep(0)
            cv2.waitKey(-1)

    out.release()
    cap.release()
    cv2.destroyAllWindows()


def run():
    detectVideo(videos.pedestrians())

if __name__ == '__main__':
    run()

