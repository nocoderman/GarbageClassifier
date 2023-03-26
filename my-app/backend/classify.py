import collections
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np


# Recreate model
model = tf.keras.models.load_model('./classifier_model.tf')

# Show the model architecture
# model.summary()

##only for testing
def temp():
    print("hello! this really works oho")

# Functon to classify images
def classify(img_path):
    img = image.load_img(img_path, target_size=(32, 32))
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)

    img_preprocessed = preprocess_input(img_batch)
    prediction = model.predict(img_preprocessed)
    # print(prediction[0])
    print(np.argmax(prediction[0]))
    return np.argmax(prediction[0])

# classify("plastic_bag.jpg")
# classify("cardboard.JPG")
# classify("Garbage classification/Garbage classification/cardboard/cardboard1.jpg")
# classify("Garbage classification/Garbage classification/cardboard/cardboard12.jpg")
# classify("Garbage classification/Garbage classification/cardboard/cardboard15.jpg")
# classify("Garbage classification/Garbage classification/cardboard/cardboard19.jpg")

preds = []
for i in range(1, 50, 1):
    cls_str = "plastic"
    class_pred = classify("Garbage classification/Garbage classification/" + cls_str + "/" + cls_str + str(i) + ".jpg")
    preds.append(class_pred)

# using Counter to find frequency of elements
frequency = collections.Counter(preds)
print(preds)
# printing the frequency
print(dict(frequency))

# 0 :
# 1 : Cardboard
# 2 :
# 3 :
# 4 :

# glass -> {1: 30, 0: 1, 2: 9, 4: 9}
# cardboard -> {0: 4, 1: 36, 2: 7, 4: 1, 3: 1}
# metal -> {1: 36, 4: 9, 2: 4}
# paper -> {4: 8, 1: 28, 2: 10, 3: 2, 0: 1}
# plastic -> {1: 27, 2: 14, 4: 5, 0: 2, 3: 1}

# classes=["cardboard","glass","metal","paper","plastic"]