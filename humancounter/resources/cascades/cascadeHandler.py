import cv2
import os
from humancounter.utils.filehandler import fetch_file_path


_BODY_CASCADE = 'haarcascade_fullbody.xml'
_CAR_CASCADE = 'haarcascade_car.xml'
_FACE_CASCADE = 'haarcascade_frontalface_default.xml'
_EYE_CASCADE = 'haarcascade_eye.xml'

def body():
    return cv2.CascadeClassifier(fetch_file_path(__file__, _BODY_CASCADE))

def car():
    return cv2.CascadeClassifier(fetch_file_path(__file__, _CAR_CASCADE))

def face():
    return cv2.CascadeClassifier(fetch_file_path(__file__, _FACE_CASCADE))

def eye():
    return cv2.CascadeClassifier(fetch_file_path(__file__, _EYE_CASCADE))