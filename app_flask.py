from flask import Flask, request, jsonify
import tensorflow as tf



app = flask.Flask(__name__)


# load the best model, have done the evaluation 
@app.route("/summary", methods=["GET"])
def model_summary():
    info = {
        "name": "hurricane_damage_classifier",
        "version": "v1",
        "input_size": list(IMG_SIZE) + [3],
        "classes": ["damage", "no_damage"],
        "description": "Binary CNN that classifies satellite images after Hurricane Harvey."
    }
    return jsonify(info)

# Preprocessing image
def prepocesssing()


# Inference endpoint
@app.route("/inference", methods=["POST"])
def inference():



if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0")










