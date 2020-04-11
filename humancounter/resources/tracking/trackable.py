

class Trackable:

    def __init__(self, centroid, rectangle):
        self.cent = centroid
        self.rect = rectangle
        self.num_people = 1

    
    def isBoundedByRectangle(self, rectangle):
        '''
        @param rectangle: a rectangle is represented as a tuple (x, y, w, h)
        return bool
        '''

        (person_x, person_y) = self.cent
        (rect_x, rect_y, rect_w, rect_h) = rectangle

        return person_x >= rect_x and person_x <= rect_x + rect_w and person_y >= rect_y and person_y <= rect_y + rect_h

    def containsPoint(self, point):
        (x, y) = point
        (rect_x, rect_y, rect_w, rect_h) = self.rect

        return x >= rect_x and x <= rect_x + rect_w and y >= rect_y and y <= rect_y + rect_h


    def getCentroids(self, trackables):
        
        centroids = []
        for trackable in trackables:
            centroids.append(trackable.cent)
        
        return centroids


    def countBounding(self, trackables):
        num_bounding = 0
        for trackable in trackables:
            if (self.containsPoint(trackable.cent)):
                num_bounding += trackable.num_people
                #self.num_people = num_bounding

        #if num_bounding == 0:
        #    num_bounding = 1

        
        #print(self.num_people)
        
        return num_bounding

