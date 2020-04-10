import math
import numpy as np


class ObjectBuffer(object):

    def __init__(self):
        self.objects = []
        self.num_objects = 0


    def calculateDistance(self, point):
        if self.num_objects == 0:
            return -1

        # We ideally only want to calculate the distance between the LAST known point in the buffer and the current point

        last_point = self.objects[self.num_objects-1]

        return np.linalg.norm(last_point - point)

    
    def addPoint(self, point):
        self.objects.append(point)
        self.num_objects += 1

    
    def update(self):
        if self.num_objects == 0:
            return

        self.objects.pop(0)
        self.num_objects -= 1
            


