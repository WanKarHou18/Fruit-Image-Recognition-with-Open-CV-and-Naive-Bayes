import numpy as np
import pandas as pd
import joblib as jl
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB

# load trained model
gnb = jl.load(r'C:\Users\Download\T8G1FruitRecognitionSystem\FruitRecognitionSystem\GaussianNB.pkl') # trained model file path

# load values to normalized data
normVal = jl.load(r'C:\Users\Download\T8G1FruitRecognitionSystem\FruitRecognitionSystem\NormalizeData.pkl') # values for normalization file path
huminVal = normVal[0]
humaxVal = normVal[1]
hueminVal = normVal[2]
huemaxVal = normVal[3]
satminVal = normVal[4]
satmaxVal = normVal[5]

# read user input data
df = pd.read_csv(r'C:\Users\Download\T8G1FruitRecognitionSystem\FruitRecognitionSystem\image_input.csv')

x = df.iloc[:, 0:30]
X = x[["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11", "x12", "x13", "x14", "x15", "x16", "x17", "x18", "x19", "x20", "x21", "x22", "x23", "x24", "x25", "x26", "x27", "x28", "x29", "x30"]].to_numpy()

# normalize data
X[:, [0,1,2,3,4,5,6]] = (X[:, [0,1,2,3,4,5,6]]-huminVal) / (humaxVal - huminVal)
X[:, [14,15,16,17,18,19,20,21]] = (X[:, [14,15,16,17,18,19,20,21]]-hueminVal) / (huemaxVal - hueminVal)
X[:, [22,23,24,25,26,27,28,29]] = (X[:, [22,23,24,25,26,27,28,29]]-satminVal) / (satmaxVal - satminVal)

pred = gnb.predict(X)
if pred == 0:
    pred = "Apple Crimson Snow"
elif pred == 1:
    pred = "Apple Granny Smith"
elif pred == 2:
    pred = "Apple Pink Lady"
elif pred == 3:
    pred = "Avocado"
elif pred == 4:
    pred = "Grape Blue"
elif pred == 5:
    pred = "Grape Pink"
elif pred == 6:
    pred = "Grape White"
elif pred == 7:
    pred = "Lemon"
elif pred == 8:
    pred = "Lemon Meyer"
elif pred == 9:
    pred = "Lychee"
elif pred == 10:
    pred = "Mango"
elif pred == 11:
    pred = "Mango Red"
elif pred == 12:
    pred = "Orange"
elif pred == 13:
    pred = "Papaya"
print("This fruit is", pred)

input("\n\n\nPress any key to close this window...")