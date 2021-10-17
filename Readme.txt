|Tutorial 8 Group 1 - Fruit Recognition System |
 ----------------------------------------------

Option 1 - Build and run in Visual Studio 2017:

Step 1
------
Download the fruits image dataset from the google drive link provided below
https://drive.google.com/drive/folders/16SfSsZk0wi78WrE9Ola_Pw7dp3uTy02G?usp=sharing


Step 2
------
Change the path of the fruits image dataset at line 160 in FeaturesToCSV.cpp.

Then, run FeaturesToCSV.cpp to extract Hu Moments, Hue, and Saturation values from fruits image dataset to a csv file named data(All fruits).csv.


Step 3
------
Change the path of the data(All fruits).csv file at line 18 in ModelTraining.py.

Then, run ModelTraining.py to train and test the Gaussian Naive Bayes model.
The output will be 2 pkl file named GaussianNB.pkl and NormalizeData.pkl, located at the same directory as ModelTraining.py.


Step 4
------
Change the path of DemoCode.py at line 164 in DemoCode.cpp.
Change the path of GaussianNB.pkl at line 8, NormalizeData.pkl at line 11, and image_input.csv at line 20 in DemoCode.py.

Then, run the DemoCode.cpp to receive user input for a fruit image path.
The output will be a csv file named image_input.csv, located at the same directory as DemoCode.cpp.

The system will run the DemoCode.py after user enter a fruit image path.
The output will be the prediction of the name of the fruit.



Option 2 - Run the .exe file

Step 1
------
Change the path of GaussianNB.pkl at line 8, NormalizeData.pkl at line 11, and image_input.csv at line 20 in NaiveBayesPython.py.

Then, run the FruitRecognitionSystem.exe to receive user input for a fruit image path.
The output will be a csv file named image_input.csv.

The system will run the NaiveBayesPython.py after user enter a fruit image path.
The output will be the prediction of the name of the fruit.


 ------------------
|Problems may occur|
 ------------------
1. The output window close immediately after user enter a fruit image path.
Cause    - joblib package is not installed.
Solution - In Visual Studio 2017, Click View -> Other Windows -> Python Environments,
	   click the drop down list in Python Environments and select Packages (PyPI) (default is Overview),
	   search and install joblib.