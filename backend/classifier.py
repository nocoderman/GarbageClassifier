import collections
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import scipy.io as scio
import tensorflow as tf
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from tensorflow.keras.optimizers import RMSprop, Adam

#Variables to play with settings
num_classes = 5
img_height, img_width = 32, 32
batch_size = 32
epoch_num = 60
verbose_num = 2

#Load Data
data_train = scio.loadmat("X_train.mat")
data_test = scio.loadmat("X_test.mat")
label_train = scio.loadmat("y_train.mat")
label_test = scio.loadmat("y_test.mat")

X_train = data_train['x_train']  ###
X_test = data_test['x_test']
y_train = label_train['y_train']  ###
y_test = label_test['y_test']

def convert_to_one_hot(Y, C):
    Y = np.eye(C)[Y.reshape(-1)].T
    return Y

# using Counter to find frequency of elements
frequency1 = collections.Counter(y_train[0])
# using Counter to find frequency of elements
frequency2 = collections.Counter(y_test[0])
print("FREQUENCY")
print(frequency1, frequency2)

# Convert training and test labels to one hot matrices
Y_train = convert_to_one_hot(y_train, num_classes).T
Y_test = convert_to_one_hot(y_test, num_classes).T

Y_train = tf.reshape(Y_train, [Y_train.shape[0], num_classes])
Y_test = tf.reshape(Y_test, [Y_test.shape[0], num_classes])

X_train = tf.image.resize(X_train, size=(img_height, img_width))
X_test = tf.image.resize(X_test, size=(img_height, img_width))

# Print the shape
tf.compat.v1.enable_eager_execution()
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

# # Model here
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(img_height, img_width, 3)),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Conv2D(16, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])


model.compile(loss='categorical_crossentropy',
              optimizer=Adam(),
              metrics=['accuracy'])

# Train your model
hist = model.fit(X_train, Y_train, verbose=verbose_num, epochs=epoch_num, validation_data=(X_test, Y_test), batch_size=batch_size)
print(hist.history.keys())

# Save the model
model.save("classifier_model.tf")

# Plot the Graph ----------------------

# Accuracy
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('Acc vs Epoch')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# Loss
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('loss vs epoch')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# Print the highest accuracy and val_acuracy to terminal
print("highest acc")
print(max(hist.history['accuracy']))
print("highest val acc")
print(max(hist.history['val_accuracy']))

