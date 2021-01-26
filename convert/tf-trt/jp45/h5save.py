import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model('mnist_model.h5')

# Save the entire model as a SavedModel.
model.save('mnist_saved_model2')

#saved_model_cli show --all --dir mnist_saved_model
