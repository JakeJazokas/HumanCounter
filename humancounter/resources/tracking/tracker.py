import time
import sys

class Tracker:
    def __init__(self):
        self.previous_frame = []
        self.current_frame = []

    def track(self, trackables):
        self.previous_frame = self.current_frame
        self.current_frame = trackables

    def count(self):
        # Check the previous frame for merges in current frame
        
        # Look at all of the rectangles in the current frame
        

        '''
        num_people = len(self.current_frame)

        for trackable in self.current_frame:
            num = trackable.countBounding(self.previous_frame)
            
            for prev_trackable in self.previous_frame:
                if (prev_trackable.num_people >= 1 and prev_trackable.containsPoint(trackable.cent)):
                    num -= prev_trackable.num_people


            num_people += num

        '''

        # Initialize the number of people to the number of boxes in the current frame
        num_people = 0

        # Checking merging
        # 1) Check if centroids of previous frames are part of the current trackable
        # 2) Count those numbers of centroids that pass
        # 3) Update the current trackable with the number of centroids that it is bounding
        for trackable in self.current_frame:
            num = trackable.countBounding(self.previous_frame)
            trackable.num_people = num
            num_people += num

        # Checking splittings
        # 1) Check if the centroids of the current frame are part of each previous trackables
        num_people_splitting = 0
        for trackable in self.previous_frame:
            num = trackable.countBounding(self.current_frame)
            num_people -= num*num

        return num_people
