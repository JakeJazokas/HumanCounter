import numpy as np
import cv2


class DetectionBuffer(object):
    '''
    This class attempts to resolve the issue of flickering with the bounding boxes. We do this by 
    performing temporal averaging of the bounding boxes. When we detect an object, we will first attempt to find
    similar objects within the buffer. If they are at the approximate location, we will add the new bounding box to
    that objects buffer.

    There are a few issues,
    1) 
    '''

    def __init__(self):
        self.buffers = []

    def addBodies(self, bodies):
        num_bodies = len(bodies)

        # Each body will have a time to live, we will