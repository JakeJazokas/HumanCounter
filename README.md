# HumanCounter

**Github :** [https://github.com/JakeJazokas/HumanCounter](https://github.com/JakeJazokas/HumanCounter)

**Presentation :** [https://www.youtube.com/watch?v=QQhRdD7mLzI&feature=youtu.be](https://www.youtube.com/watch?v=QQhRdD7mLzI&feature=youtu.be)

**Final Document :** Located in the ```/docs/``` folder.

**Videos Showing Our Program Working (Results) :** Located in the ```/output/``` folder.

**Title :** HumanCounter

**Members :**

- Jake Jazokas - 101083496
- Cody Bennett - 101035873
- Andrew Burry - 100832328

**Build steps :**
1) Clone the Github Repository
2) Open Terminal in the HumanCounter directory
3) Use a virtual environment, by running the following commands:
```python -m venv venv```
```
.\venv\Scripts\activate (win)
. /venv/bin/activate (linux)
```
3) Install the python requirements using the following command: ```pip install -r requirements.txt```
4) Download the weights for the neural network: [https://pjreddie.com/media/files/yolov3.weights](https://pjreddie.com/media/files/yolov3.weights)
5) Copy the weights file to the following directory: ```HumanCounter\HumanCounter\static\models\```

**Running :**

1) Run the following command in the HumanCounter directory: ```python manage.py runserver```
2) Open a web browser and go to: [http://localhost:8000/](http://localhost:8000/)
3) The instructions on the home page of the website explain how to upload a video and have it run through the algorithms.
4) Any media uploaded or output is available in the ```/media/``` folder.

**Summary/Abstract :**

- ~~The computer vision problem that our group will be working on involves human surveillance in static images. Our plan is to count the number of people in a given image. The program should take in an image of a group of people, and return the number of people that it has counted in it. If there is time, we hope to provide live feedback from a cell phone camera feed on how many people are currently in frame.~~

- Human detection is a well documented computer vision problem with applications becoming more and more prevalent in our everyday lives. The goal of our project was to accurately count the number of people in an image or video. To achieve this goal, we explored several detection utilities readily available within the OpenCV library, namely cascade classifiers, background subtractors and deep neural networks. After comparing the results of each of the human detection methodologies, the deep neural network based detector was the most successful at detecting humans in both images and videos with a high degree of accuracy.

**Introduction :**
- We implemented an application that is able to identify and count the number of people in either an image or a video. This is a good application for computer vision as it involves core computer vision methods in order to achieve the goal. Our first implementation, for images, relies on feature detection and non-maxima suppression and our first implementation for tracking in videos utilizes masks, contours, and background subtraction. This problem is also challenging because we must be able to segregate overlapping people as well as track people accurately as they move across a scene in a video, which results in continuously changing contours to track and identify properly. We expanded our application further to introduce a neural network to show more improved results and help with these issues. 

**Background :**

- **Existing Research :**
  - ~~[http://homepages.inf.ed.ac.uk/rbf/CAVIAR/](http://homepages.inf.ed.ac.uk/rbf/CAVIAR/)~~
  
| Reference Number | Citation |
|--|--|
| [1] | CAVIAR Project/IST 2001 37540, n.d. http://homepages.inf.ed.ac.uk/rbf/CAVIAR/. |
| [2] | P. Jones, Paul Viola, and Michael Jones. "Rapid Object Detection Using a Boosted Cascade of Simple Features." . In University of Rochester. Charles Rich (pp. 905–910).2001. |
| [3] | Bradski, G.. "The OpenCV Library".Dr. Dobb's Journal of Software Tools (2000). |
| [4] | Paulo Menezes, José Carlos Barreto, and Jorge Dias. "Face tracking based on haar-like features and eigenfaces".IFAC Proceedings Volumes 37, no.8 (2004): 304 - 309. |
| [5] | Redmon, Joseph, and Ali, Farhadi. "YOLOv3: An Incremental Improvement".arXiv (2018). |
| [6] | “Django.” Django. Django Software Foundation, April 1, 2020. https://djangoproject.com/. |
| [7] | Walt, Stéfan van der, S. Chris, Colbert, and Gaël, Varoquaux. "The NumPy Array: A Structure for Efficient Numerical Computation".Computing in Science & Engineering 13, no.2 (2011): 22-30. |
| [8] | jrosebr1. “jrosebr1/Imutils.” GitHub, August 18, 2019. https://github.com/jrosebr1/imutils. |

- **What we are doing differently :**
  - CAVIAR aims to detect unusual human behavior, or patterns in their activity. Our application will revolve around detecting the number of people in a crowd. And displaying real time data data.

- **Project Background :**
  - Human detection is a well documented computer vision problem with applications becoming more prevalent in our everyday lives. We implemented a web-based application which processes images and videos to detect occurrences of humans and videos within each image or frame. Images and videos were processed through several algorithms, namely, cascade classifiers, background subtractors and deep neural networks.
	- We first began this project by examining research findings and datasets presented by the CAVIAR research group [1]. These results helped us build a conceptual model of the problem at hand and helped us learn an important part of the history behind object detection.
	- The first detection method that was explored was human detection through Haar feature-based cascade classifiers developed by Paul Viola and Michael Jones [2]. The algorithm utilities are available within the OpenCV library for public use [3]. A cascade classifier is a 2-class neural network which is trained on images with and without the 
  object of interest. Cascade classifiers apply kernels of each haar-like feature to detect its presence. A few haar-like features can be observed below [4].
  - Figure 1: Example haar-like features [4]. ![Fig1](https://cdn.discordapp.com/attachments/672452802630516747/701200456243740852/unknown.png)
  - After applying each kernel, we can uncover the possible presence of each haar-like feature. Once a list of features have been extracted from an image, they are ordered (cascaded) to be as computationally efficient as possible. 
  - The method we researched to implement as our initial algorithm was a motion detection and background subtraction. This relied on the OpenCV provided functions. OpenCV is a free computer vision and machine learning library that is open source [3]. Our application used the createBackgroundSubtractorMOG2() algorithm within this library [3]. This estimates the background based on the first few frames of the video and then we compare that to subsequent frames [3].
  - The second object detection method that was explored was object detection through a trained neural network. Our neural network model was trained by loading in the pre-trained weights and configuration files provided by YOLOv3 [5]. This model makes predictions about whether or not objects belong to specific, identifiable categories, such as a person or dog, by sending the image, as input, to the neural network. Most implementations apply the model to various parts of the image to make the prediction whereas YOLOv3 applies the model to the image as a whole[3]. YOLOv3 is accessible through the opencv library [3]. The trained neural network is then used to perform human recognition in images and videos.
  - We used the Django python module [6], in order to create a website that acts as an interface between our algorithms and the user. Django allows you to create a webserver using a python frontend and backend. The website allows a user to upload their own videos or images to test against our algorithms
	- Finally the last built in libraries we used were numpy and imutils. Numpy is a common python package that is used from scientific computations [7]. We used this to help with calculating key computer vision equations to solve our problem. Imutils is a package that has built in functions to help with image processing [8]. We use this to implement a non-maxima suppression algorithm.
	- For more specific details about the specific implementation of these algorithms please see our approach section.


**The Challenge :**

- The problem of human detection in static images is challenging for many reasons. In order to count the number of people in an image, the application must be able to properly identify a person within the image. This is not a trivial task since not only do people have unique physical appearances, but they may be oriented differently relative to the camera. Basically, being able to determine what constitutes a human in an image, and then counting them.

**Could you solve your problem using just a few pre-existing functions in OpenCV?**
**Try to state explicitly what you are hoping to learn by doing this project?**

- From this project, we are hoping to become familiar with openCV for object classification within an image. We hope to also gain insight into the process of recognizing humans within images. As image data may differ from camera to camera, we hope to apply techniques to standardize the images, in order to get consistent results.

- We would not be able to solve this problem using only a few pre-existing functions in OpenCV, as object detection and classification is not a trivial problem.
Thus, we have to write our own algorithms in order to solve the problem.

**Visual Description :**

Given an image of a crowd of people (like in figure A), our application will count the number of people that it sees in the image, and return that number (like in figure B).

**(A)** 
![Image A](https://media.discordapp.net/attachments/672452802630516747/701094632058257468/people_close.png)

**(B)** 
![Image B](https://media.discordapp.net/attachments/672452802630516747/701094658167537674/counted_people_close.png)

**Goals and Deliverables :**

**• What We Plan To Achieve :**

- We plan to achieve a working application which can identify and count people in a static image, displaying the result to the user. Every person identified within the image will be outlined with a box and labelled as a person.

**• What We Hope To Achieve**

- Once we have an application which can identify and count people in a static image, we would hope to extend the project to detect and identify people moving about a scene in a video in live time. (I.e. the feed from a cell phone camera)

**• What success looks like and how it can be evaluated.**

- In order to prove that our application works, we will manually count the number of people in images, and then compare the results that we have got to the output of the application.

**• How realistic is it for your team to get what it needs to get done within the allotted time? Remember you only have a few weeks to get this project completed.**

- We are confident that we will be able to complete the project within the allocated time we have been provided. We have identified the key features to focus on early to allow us time to ensure these features are working as intended by the end. Additional features have been identified but will only be implemented if time allows.

**Technical Information**

For this project, we will be using the libraries Tensorflow, NumPy, and OpenCV. Using these libraries, we hope to detect human figures within an image or video. There are two approaches to solve this problem which will be explored within the coming weeks. A brief summary for these approaches can be found below:

(A) Using an image without humans as a baseline, we will detect any new objects appearing in subsequent images/frames through comparison with the baseline. The newly identified objects will be isolated and classified using a neural net trained to identify human figures.

~~(B) Using VIRAT human surveillance dataset videos, we will train a neural net to classify human figures within a scene. The VIRAT human surveillance datasets contain testing and validation data which is formatted unlike those available through MNIST. Additional parsing will be required to correlate annotated events with those in the videos. Once this has been one, a neural net can be trained to identify human figures within a video or image.~~

(B) We now pass the YOLOv3 dataset weights to our neural network, which identifies human figures within a video or image.

As expressed earlier, the libraries TensorFlow, NumPy, and OpenCV will be used in this project. 
Firstly, TensorFlow will be used for training neural networks using human surveillance datasets. TensorBoard, an accompanying tool for TensorFlow, will be used for machine learning data visualization. The second notable library, OpenCV, will be used for image manipulation and parsing. An example of how we would use OpenCV would be loading the VIRAT dataset videos for approach two, where the dataset videos must be opened using OpenCV’s VideoCapture functions to extract frame data. Once all of the frame data has been decoupled from the video datasets, the neural network can be trained. The third notable library, NumPy, boasts a large variety of mathematical operations and will be used for data manipulation in conjunction with OpenCV. NumPy will be used for any mathematical operations which are not available through the OpenCV library.

~~The VIRAT video datasets can be obtained through the VIRAT website, found through the link below.
https://viratdata.org/~~

**Approach :**
- For human detection in images the first implementation we did utilizes a cascade classifier. For this we initially blur the image, using a Gaussian Blur; To remove noise and help reduce spurious detections. 
- We then attempt to classify faces in the picture, as there will be one face per person. Should we not be able to detect any faces we added an additional classifier to detect bodies. This helps us detect people that are too far away for their face to be detectable or people not facing the camera.
- After this we loop through our classified objects and create a rectangle around them. We then apply non-maxima suppression with an overlap threshold to ensure people are only counted once per image, and to further help with spurious detections. Now, since we should only have real detections left, we loop through our detected people and draw rectangles around them. We then count how many people make it through this threshold and output the final image. 
- For video detection the first implementation we did utilizes a background subtraction technique. This algorithm loads the video in and initializes a kernel and background subtractor. We use the built-in one provided by opencv by using the cv2.createBackgroundSubtractorMOG2() method. For each frame in the video we then create a mask using the kernel and background subtractor. This is done by applying the previously mentioned background subtractor to each frame.
- After that we use the previously mentioned kernel to reduce noise in the mask to help with invalid detections. We then threshold, rather than using the built in shadow detection provided by opencv, the mask to filter out their shadows, since the shadows resulted in an object big enough to be a person. Since the shadow was not as intense, the threshold would filter out its lower pixel values and allow true “person” pixels to remain. 
- After that we create a contour around the resulting people to mark their outline. We then create rectangles to enclose these contours. We run these rectangles through the non-maxima suppression algorithm using the imutils.non_max_suppression method with an overlap threshold. This helps to ensure people are not counted twice if their contours are not continuous as the two rectangles are still close enough for us to identify them as one person rather than two. Finally, we draw the suppressed rectangles around the contours on the output video and count the number of rectangles, or people, we have detected.
- After implementing the first methods for images and videos we were able to accurately track people. However, there were still some specific cases in which people were too close and it only detected one person or if a person walked behind an object that partially occluded them they may not be detected. To further our accuracy of identifying people we expanded our project to introduce a neural network. For this we used YOLOv3(You Only Look Once). 
- Our implementation of YOLOv3 for human detection in images first builds the model by loading the provided weights and configuration and then feeding them to a deep neural network. Our implementation uses the opencv deep neural network by using the cv2.dnn.readNetFromDarknet() function. Note we don’t use the actual YOLOv3 neural network but our own implementation of it using its training data. We then build the input, called a blob or binary large object, for the neural network from the image and send it to the network. We then loop through the output of the network which is another blob that contains the detections. We loop through each detection in the output and send it through a parser to determine if it passes as a person. The detection contains information about the bounding box surrounding the detected object. In addition to that it contains the neural network’s probability of the object belonging to each one of its identifiable categories, as it can identify more than just people. We then make sure that a human is the most probable object and, if it is, we threshold the probability to ensure that only detections with high confidence are included. We then draw boxes around the objects that pass the threshold and count the number of people we detect.
- The process for our implementation of YOLOv3 for videos follows a very similar process for how it works with images. It builds the model using the same training data. We extract the video data to ensure we can output with the same data, such as resolution, video length, and the video’s frames per second. We then loop through each frame and send the frame as an input to the neural network. It counts people using the same method as images and outputs how many people it detected in that frame and writes it to the output video. After we loop through all the frames we output the video. 
- On top of all these implementations our application runs on a Django web server. This allows for custom videos and images to be used for testing purposes as it allows for videos to be uploaded dynamically. We don’t have to have our videos in a predefined location and can browse the computer we are on for the video or image we want to run through the program.

- **See project document for full approach and report**

**List of Work :**
- Equal work was completed by all members of the group.

**Schedule:**

| **Jake** | **Cody** | **Andrew** | **Week** |
| --- | --- | --- | --- |
| Researching | Researching | Researching | **February 1 - 8** |
| Researching | Researching | Researching | **February 9 - 16** |
| Algorithm Design | Algorithm Design | Algorithm Design | **February 17 - 24** |
| Algorithm Design | Algorithm Design | Algorithm Design | **February 25 - March 3** |
| Algorithm Implementation | Algorithm Implementation | Algorithm Implementation | **March 4 - March 11** |
| Application Creation | Application Creation | Application Creation | **March 12 - March 19** |
| Application Development | Application Development | Application Development | **March 20 - March 27** |
| Application Testing | Application Testing | Application Testing | **March 28 - April 4** |
| Finishing Touches | Finishing Touches | Finishing Touches | **April 5 - April 10** |
