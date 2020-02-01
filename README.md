# HumanCounter

**Github :** [_https://github.com/JakeJazokas/HumanCounter_](https://github.com/JakeJazokas/HumanCounter)

**Title :** HumanCounter

**Members:**

- Jake Jazokas - 101083496
- Cody Bennett - 101035873
- Andrew Burry - 100832328

**Summary:**

- The computer vision problem that our group will be working on involves human surveillance in static images. Our plan is to count the number of people in a given image. The program should take in an image of a group of people, and return the number of people that it has counted in it. If there is time, we hope to provide live feedback from a cell phone camera feed on how many people are currently in frame.

**Background:**

- **Existing Research :**
  - [http://homepages.inf.ed.ac.uk/rbf/CAVIAR/](http://homepages.inf.ed.ac.uk/rbf/CAVIAR/)
- **What we are doing differently:**
  - CAVIAR aims to detect unusual human behavior, or patterns in their activity. Our application will revolve around detecting the number of people in a crowd. And possibly displaying real time data data.

**The Challenge :**

- The problem of human detection in static images is challenging for many reasons. In order to count the number of people in an image, the application must be able to properly identify a person within the image. This is not a trivial task since not only do people have unique physical appearances, but they may be oriented differently relative to the camera. Basically, being able to determine what constitutes a human in an image, and then counting them.

**Could you solve your problem using just a few pre-existing functions in OpenCV?**
**Try to state explicitly what you are hoping to learn by doing this project?**

- From this project, we are hoping to become familiar with openCV for object classification within an image. We hope to also gain insight into the process of recognizing humans within images. As image data may differ from camera to camera, we hope to apply techniques to standardize the images, in order to get consistent results.

**Visual Description:**

Given an image of a crowd of people (like in figure A), our application will count the number of people that it sees in the image, and return that number (like in figure B).

(A)

![Image A](https://cdn.discordapp.com/attachments/672452802630516747/672893473631764490/unknown.png)

(B)

![Image B](https://cdn.discordapp.com/attachments/672452802630516747/672893497996738560/unknown.png)

**Goals and Deliverables:**

**• What We Plan To Achieve:**

- We plan to achieve a working application which can identify and count people in a static image, displaying the result to the user. Every person identified within the image will be outlined with a box and labelled as a person.

**• What We Hope To Achieve**

- Once we have an application which can identify and count people in a static image, we would hope to extend the project to detect and identify people moving about a scene in a video in live time. (I.e. the feed from a cell phone camera)

**• What success looks like and how it can be evaluated.**

- In order to prove that our application works, we will manually count the number of people in images, and then compare the results that we have got to the output of the application.

**• How realistic is it for your team to get what it needs to get done within the allotted time? Remember you only have a few weeks to get this project completed.**

- We are confident that we will be able to complete the project within the allocated time we have been provided. We have identified the key features to focus on early to allow us time to ensure these features are working as intended by the end. Additional features have been identified but will only be implemented if time allows.

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
