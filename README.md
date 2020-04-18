# HumanCounter

**Github :** [_https://github.com/JakeJazokas/HumanCounter_](https://github.com/JakeJazokas/HumanCounter)

**Final Document:** Located in the ```/docs/``` folder.

**Title :** HumanCounter

**Members:**

- Jake Jazokas - 101083496
- Cody Bennett - 101035873
- Andrew Burry - 100832328

**Build steps:**
1) Clone the Github Repository
2) Open Terminal in the HumanCounter directory
3) Install the python requirements using the following command: ```pip install -r requirements.txt```
4) Download the weights for the neural network: [https://pjreddie.com/media/files/yolov3.weights](https://pjreddie.com/media/files/yolov3.weights)
5) Copy the weights file to: ```HumanCounter\HumanCounter\static\models\```

**Running:**

1) Run the following command in the HumanCounter directory: ```python manage.py runserver```
2) Open a web browser and go to: [http://localhost:8000/](http://localhost:8000/)

**Summary:**

- Human detection is a well documented computer vision problem with applications becoming more and more prevalent in our everyday lives. The goal of our project was to accurately count the number of people in an image or video. To achieve this goal, we explored several detection utilities readily available within the OpenCV library, namely cascade classifiers, histogram of oriented gradients (HOG) feature descriptors, background subtractors and deep neural networks. After comparing the results of each of the human detection methodologies, the deep neural network based detector was the most successful at detecting humans in both images and videos with a high degree of accuracy.

**Background:**

- **Existing Research :**
  - [http://homepages.inf.ed.ac.uk/rbf/CAVIAR/](http://homepages.inf.ed.ac.uk/rbf/CAVIAR/)
  - [https://pjreddie.com/darknet/yolo/](https://pjreddie.com/darknet/yolo/)
- **What we are doing differently:**
  - CAVIAR aims to detect unusual human behavior, or patterns in their activity. Our application will revolve around detecting the number of people in a crowd. And displaying real time data data.

**The Challenge :**

- The problem of human detection in static images is challenging for many reasons. In order to count the number of people in an image, the application must be able to properly identify a person within the image. This is not a trivial task since not only do people have unique physical appearances, but they may be oriented differently relative to the camera. Basically, being able to determine what constitutes a human in an image, and then counting them.

**Could you solve your problem using just a few pre-existing functions in OpenCV?**
**Try to state explicitly what you are hoping to learn by doing this project?**

- From this project, we are hoping to become familiar with openCV for object classification within an image. We hope to also gain insight into the process of recognizing humans within images. As image data may differ from camera to camera, we hope to apply techniques to standardize the images, in order to get consistent results.

- We would not be able to solve this problem using only a few pre-existing functions in OpenCV, as object detection and classification is not a trivial problem.
Thus, we have to write our own algorithms in order to solve the problem.

**Visual Description:**

Given an image of a crowd of people (like in figure A), our application will count the number of people that it sees in the image, and return that number (like in figure B).

**(A)** 
![Image A](https://media.discordapp.net/attachments/672452802630516747/701094632058257468/people_close.png)

**(B)** 
![Image B](https://media.discordapp.net/attachments/672452802630516747/701094658167537674/counted_people_close.png)

**Goals and Deliverables:**

**• What We Plan To Achieve:**

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