import numpy as np
import cv2
from HumanCounter.settings import STATICFILES_DIRS

# confidence and threshold default values
CONFIDENCE = 0.5
THRESHOLD = 0.4

def build_network_model():
    # Define the paths to the yolo weights and configuration files
    weights = STATICFILES_DIRS[0] + "/models/yolov3.weights"
    config = STATICFILES_DIRS[0] + "/models/yolov3.cfg"

    # Load and initialize the pre-trained model
    return cv2.dnn.readNetFromDarknet(config, weights)


def detected_person(detection):
    # The first 4 elements of a detection consist of data related to the dimensions of the bounding box
    # The remaining elements consist to the classification confidences for each bin. The bin corresponding
    # to human confidence is the 5th element in detection, or the first element in scores
    box_data = detection[:4]
    scores = detection[5:]

    # The bin number corresponding to a person is element 0
    key_bin_number = np.argmax(scores)
    human_detected = key_bin_number == 0
    confidence = scores[key_bin_number]

    return (human_detected, box_data, confidence)

def get_rect_coordinates(frame_shape, box_dimensions):
    # The box dimensions contain four elements, the first two are
    # the center coordinates (x, y) and the last are the width and height.
    # It is also important to note that the box dimension data is normalized

    frame_height, frame_width = frame_shape

    # Scale the data in the associated direction
    center_x, center_y, box_width, box_height = box_dimensions * np.array([frame_width, frame_height, frame_width, frame_height])

    # When drawing a rectangle, we draw it as a set of two points, the upper 
    # left corner and the bottom right corner. Transform the center point 
    # to the upper left coordinate
    x, y = center_x - (box_width / 2), center_y - (box_height / 2)

    return int(x), int(y), int(box_width), int(box_height)


def parse_detection(detection, shape, boxes, confidences):
    person_detected, box_data, confidence = detected_person(detection)

    if not person_detected:
        return (boxes, confidences)

    if confidence > CONFIDENCE:
        # Extract the rectangle shape from the detection data
        x, y, width, height = get_rect_coordinates(shape, box_data)

        # update our list of bounding box coordinates, confidences,
        # and class IDs
        boxes.append([x, y, width, height])
        confidences.append(float(confidence))
    return (boxes, confidences)


def drawBoxes(image, boxes, confidences):
    # Filter boxes using non-maximum suppression to remove overlapping
    ids = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE, THRESHOLD)

    # Ensure there are boxes to draw
    if len(ids) == 0:
        return image

    # Extract the boxes which passed filtering
    boxes_retained = [boxes[i] for i in ids.flatten()]

    num_people = 0

    # loop over the indexes we are keeping
    for box in boxes_retained:
        # Define the rectangle coordinates
        x1, y1 = box[0], box[1]
        x2, y2 = x1 + box[2], y1 + box[3]
        # Draw the rectangle
        cv2.rectangle(image, (x1, y1), (x2, y2),
                      color=(0, 255, 0), thickness=5)

        num_people += 1

    return (image, num_people)
