from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from HumanCounter.settings import MEDIA_ROOT
from HumanCounter.settings import STATICFILES_DIRS

import os
import cv2
import imutils
# from imutils.object_detection import non_max_suppression
import numpy as np

# Create your views here.
def upload_image(request):
    context = {}
    if request.method == 'POST' and request.FILES:
        uploaded_image = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save(uploaded_image.name, uploaded_image)
        context['upload_url'] = fs.url(name)
        # Count people in image
        num_people, img = count_people(name)
        context['counted_url'] = fs.url(img)
        context['counted_num'] = num_people
    return render(request, 'upload_image.html', context)

def count_people(image_name):
    # File name
    filename = os.path.abspath(os.path.join(MEDIA_ROOT, image_name))

    image = cv2.imread(filename, cv2.COLOR_BGR2GRAY)
    gray = image.copy()

    body_classifier = cv2.CascadeClassifier(os.path.abspath(os.path.join(STATICFILES_DIRS[0], '/models/haarcascade_fullbody.xml')))
    # body_classifier = cv2.CascadeClassifier('HumanCounter\static\models\haarcascade_fullbody.xml')

    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    ''' Our classifier returns the ROI of the detected face as a tuple, 
    It stores the top left coordinate and the bottom right coordiantes'''
    bodys = body_classifier.detectMultiScale(gray, 1.0485258, 6)

    # '''When no bodys detected, body_classifier returns and empty tuple'''
    # if bodys is ():
    #     print("No bodys found")

    '''We iterate through our bodys array and draw a rectangle over each face in bodys'''
    [cv2.rectangle(image, (x,y), (x+w,y+h), (127,0,255), 2) for (x,y,w,h) in bodys]
        
    num_people = len(bodys)
    # # Create a HOG dectector
    # hog = cv2.HOGDescriptor()

    # # Set the coefficients of the linear SVM classifier
    # hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # # Load the image
    # image = cv2.imread(filename)
    # # image = imutils.resize(image, width=min(400, image.shape[1]))

    # # detect people in the image
    # rects, weights = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)
	
    # # apply non-maxima suppression to the bounding boxes using a
	# # fairly large overlap threshold to try to maintain overlapping
	# # boxes that are still people
    # rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    # pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    
    # # draw the final bounding boxes
    # [cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2) for (xA, yA, xB, yB) in pick]
    
    # # Number of people in the image
    # num_people = len(pick)

    # Write the number of people to the image
    cv2.putText(img=image,
                text="Number of People: {}".format(num_people),
                org=(10, 40),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1,
                color=(0, 0, 255),
                thickness=3)
    
    # Save the image
    name = 'counted_' + image_name
    cv2.imwrite(os.path.abspath(os.path.join(MEDIA_ROOT, name)), image)
    
    # Return the number of people and the image name
    return num_people, name
