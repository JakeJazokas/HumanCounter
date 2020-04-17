from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from HumanCounter.settings import MEDIA_ROOT
from HumanCounter.settings import STATICFILES_DIRS
import os
import cv2
import imutils
from imutils.object_detection import non_max_suppression
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
    # Read the image and blur it
    image = cv2.imread(filename, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(image,(3,3),2)

    # First, attempt to classify faces
    face_classifier = cv2.CascadeClassifier(STATICFILES_DIRS[0] + '/models/haarcascade_frontalface_default.xml')
    
    # Our classifier returns the ROI of the detected face as a tuple, 
    # It stores the top left coordinate and the bottom right coordiantes
    # Attempt to classify faces
    classified = face_classifier.detectMultiScale(blurred, 1.0785258, 15)

    # When no faces detected, face_classifier returns and empty tuple
    # In that case, use a body classifier and attempt to classify bodys
    if classified == ():
        # Our classifier returns the ROI of the detected face as a tuple, 
        # It stores the top left coordinate and the bottom right coordiantes
        body_classifier = cv2.CascadeClassifier(STATICFILES_DIRS[0] + '/models/haarcascade_fullbody.xml')
        classified = body_classifier.detectMultiScale(blurred, 1.0485258, 1)

    # Get the rectangles from all the classifed objects
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in classified])
    # Perform non maxima supression on the list of rectangles
    picks = non_max_suppression(rects, probs=None, overlapThresh=0.2)

    # We iterate through our bodys array and draw a rectangle over each face in bodys
    [cv2.rectangle(image, (xA,yA), (xB,yB), (0,0,255), 2) for (xA,yA,xB,yB) in picks]
    
    # Number of people is equal to the length of the non-maximal array
    num_people = len(picks)

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
