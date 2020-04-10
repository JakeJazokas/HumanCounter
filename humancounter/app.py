
import cv2
import numpy as np
import humancounter.resources.cascades.cascadeHandler as classifier
import humancounter.resources.videos.videoHandler as videos

def detectVideo(video):
    print("Running Application Human Counter")

    # Create our body classifier
    body_classifier = classifier.body()

    # Initiate video capture for video file, here we are using the video file in which pedestrians would be detected
    cap = cv2.VideoCapture(video)

    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('output/output.avi', fourcc, 20.0, (768, 576))

    # Loop once video is successfully loaded
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    fgbg = cv2.createBackgroundSubtractorMOG2()
    while cap.isOpened():
        ret, frame = cap.read()

        if frame is None:
            break
        
        output = np.copy(frame)

        fgmask = fgbg.apply(frame)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
        _, fgmask= cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)

        indices = np.where(fgmask == 0)
        output[indices] = (0, 0, 0)

        # Find the contours on the mask that was just thresholded
        contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Draw the contours
        cv2.drawContours(output, contours, -1, (0, 255, 0), 2)

        num_people = 0
        for contour in contours:
            # Create a bounding rectangle from the contour
            (x, y, w, h) = cv2.boundingRect(contour)
            centerCoord = (int(x+(w/2)), int(y+(h/2)))
            # Draw the rectangle on the current frame
            if cv2.contourArea(contour) > 200:
                num_people += 1
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(frame, 
                    "Number of People: {}".format(num_people), 
                    (10, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 3)

        out.write(frame)
        cv2.imshow('frame', frame)
        cv2.imshow('original', output)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        
        if cv2.waitKey(1) == 13: #13 is the Enter Key
            break

    out.release()
    cap.release()
    cv2.destroyAllWindows()


def run():
    detectVideo(videos.pedestrians())

if __name__ == '__main__':
    run()

