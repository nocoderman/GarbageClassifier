import collections
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from matplotlib.pyplot import *
import cv2
import os
from sklearn.model_selection import train_test_split
from scipy.io import savemat

d = './Garbage classification/Garbage classification/'
classes=["cardboard","glass","metal","paper","plastic"]
data=[]
for c in classes:
    i = classes.index(c)
    print(i)
    path=os.path.join(d,c)
    for img in os.listdir(path):
        im=cv2.imread(os.path.join(path,img))
        im=cv2.resize(im,(64,64))
        data.append([im,i])

import random
random.shuffle(data)
X=[]
Y=[]
for x,y in data:
    X.append(x)
    Y.append(y)

# # using Counter to find frequency of elements
# frequency1 = collections.Counter(Y)
#
# # printing the frequency
# print(dict(frequency1))

x=np.array(X)
y=np.array(Y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0, stratify=y)

X_train = x_train / 255.0
X_test = x_test / 255.0

print(x.shape, y.shape)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

savemat('y_test.mat', {'y_test': y_test})
savemat('y_train.mat', {'y_train': y_train})
savemat('X_test.mat', {'x_test': x_test})
savemat('X_train.mat', {'x_train': x_train})

