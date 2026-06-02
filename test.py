import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input

model = tf.saved_model.load("./model_export")

infer = model.signatures["serving_default"]

img = image.load_img(
    "./real_img-banana.jpeg",
    target_size=(224,224)
)

img = image.img_to_array(img)
img = np.expand_dims(img, axis=0)
img = preprocess_input(img)

pred = infer(
    tf.constant(img)
)

print(np.max(pred['output_0'].numpy()))