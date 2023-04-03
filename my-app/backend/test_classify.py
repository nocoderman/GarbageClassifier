import collections
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
# import image from PIL
import numpy as np


# Show the model architecture
# model.summary()

# Functon to classify images
def classify(img_path):
    # Load Image
    img = image.load_img(img_path, target_size=(32, 32))
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    # Use model to predict
    img_preprocessed = preprocess_input(img_batch)
    # img_preprocessed = img_batch

    # Recreate model
    model = tf.keras.models.load_model('./classifier_model.tf')
    prediction = model.predict(img_preprocessed)
    class_num = np.argmax(prediction[0])

    if class_num == 0:
        print("COMPOSTABLE WASTE")
        return "COMPOSTABLE WASTE"
    else:
        print("RECYCLABLE WASTE")
        return "RECYCLABLE WASTE"

classify("Garbage classification/Garbage classification/Organic/O_12587.jpg")