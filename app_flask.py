from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from tensorflow import keras
from PIL import Image
import io

app = Flask(__name__)

# Load the model once the server starts
path = './best_model.keras' # TODO: need to update the path
model = keras.models.load_model(path)
IMG_SIZE = (224, 224)

# load the best model, have done the evaluation 
@app.route("/summary", methods=["GET"])
def model_summary():
    info = {
        "name": "hurricane_damage_classifier",
        "version": "v1",
        "input_size": list(IMG_SIZE) + [3],
        "classes": ["damage", "no_damage"],
        "description": "Binary CNN that classifies satellite images after Hurricane Harvey.",
        "total_parameters": int(model.count_params()),
        "architecture": model.name
    }
    return jsonify(info)

# Preprocessing image
def prepocesssing():
    pass

# from grader.py from Joe code link
def do_image_preprocessing(image_file):
    # Read the file object into bytes, then open with PIL
    image_bytes = image_file.read()
    img = Image.open(io.BytesIO(image_bytes)).resize(IMG_SIZE)
    img_array = np.array(img) / 255.0
    img_list = np.expand_dims(img_array, axis=0)
    return img_list


# Inference endpoint
@app.route("/inference", methods=["POST"])
def inference():
    # Check if image file is in request
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    image_file = request.files['image']
    
    # Check if file is empty
    if image_file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400
    
    try:
        # Read the image
        img_list = do_image_preprocessing(image_file)
        
        # Run prediction
        predictions = model.predict(img_list)
        
        # Get Predicted class
        prediction_value = float(predictions[0][0])
        
        # Map to required string values
        if prediction_value > 0.5: # prediction > 0.5 = damage (class 1)
            prediction_label = "no_damage"
        else: # prediction <= 0.5 = damage (class 0)
            prediction_label = "damage"
        
        output = {
            "prediction": prediction_label
        }
        return jsonify(output), 200
    
    except Exception as e:
        return jsonify({
            'error': 'Inference failed',
            'details': str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0")