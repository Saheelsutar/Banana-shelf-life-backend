
import numpy as np
from io import BytesIO
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.models import load_model
from flask import Flask,request,jsonify

model = tf.saved_model.load("./model_export")

infer = model.signatures["serving_default"]

class_names=['overripe','ripe','rotten','unripe']
shelf_life = {
        "unripe": "6-9 days",
        "ripe": "3-5 days",
        "overripe": "1-2 days",
        "rotten": "0 days"
    }


def preprocess_img(img_file):
  img=image.load_img(
      BytesIO(img_file.read()),
      target_size=(224,224)
  )
  img_array=image.img_to_array(img)
  img_array=np.expand_dims(img_array,axis=0)
  img_array=preprocess_input(img_array)
  return img_array


app = Flask(__name__)

@app.route("/")
def main():
   return jsonify({"backend_status":"running"})

@app.route("/predict",methods=["POST"])
def predict():
    if "image" not in request.files:
       return jsonify({
          "error":"No image uploaded"
       }),400
    file=request.files["image"]
    pred = infer(tf.constant(preprocess_img(file)))
    scores=pred['output_0'].numpy()
    predicted_class=class_names[np.argmax(scores)]
    confidence=round(float((np.max(scores))*100),2)
    return jsonify({
       "ripeness":predicted_class,
       "shelf-life":shelf_life[predicted_class],
       "confidence":confidence
    })

app.run()