# Fruit-Image-Recognition-with-Open-CV-and-Naive-Bayes
This project is focus on developing a fully functional fruit recognition system that aid in identification of fruit at anytime and anywhere. To achieve this target, the system will make use of OpenCV technique together with some other technologies such as webcam to obtain and process the fruit image. Certain attribute values were extracted from image and stored in Excel file, then analysis was performed with ML model- Naïve Bayes.

### Dataset Description:
14 types of fruit image had been chosen as training and testing dataset in this project, which include Apple Crimson Snow, Apple Granny Smith, Apple Pink Lady, Avocado, Grape Blue, Grape Pink, Grape White, Lemon, Lemon Meyer, Lychee, Mango, Mango Red, Orange, and Papaya. Each of these fruit subsets contains around 400 sample images.

### Software and Libraries

1.  Microsoft Visual Studio 2017
2.  Open CV SDK
3.  Python IDE

### Hardware:

1.  Logitech C920 Webcam
2.  Laptop

### Image Preprocessing Flow Chart

<p align="center">
  <img src="https://user-images.githubusercontent.com/91049876/137615201-89600213-24e2-41f7-8d7a-6de97797068c.png">
</p>

Gaussian blur technique is used to decrease the noise and detail of fruit images. The output of the Gaussian blur implementation will be the input of segmentation. Output of segmented image will be the input of Hu moment implementation. Seven moments derived by Hu for shape description. The first 6 moments will be invariant to scale, translation, reflection and reflection. While the 7th moment’s sign changes for image reflection. The value of each moment extracted out as features to help in shape identification for fruits images.After that, for color extraction, extract the color features of the fruit as in hue and saturation while generate the color histogram for the system to identify the fruit.

### Model Training FlowChart

<p align="center">
  <img src="https://user-images.githubusercontent.com/91049876/137615286-54ce0c3f-38a9-4bfe-bcc7-0c9e64a864b7.png">
</p>

Data from image processing was separated to training set and testing set with ratio of 80:20 . Different models of Navies Bayes was trained using training set to gauge its accuracy. 

### Results

<p align="center">
  <img src="https://user-images.githubusercontent.com/91049876/137615366-aca58d2d-3460-4d83-8aff-c45da29fad8a.png">
</p>


