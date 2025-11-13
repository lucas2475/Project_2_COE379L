import tensorflow as tf
from tensorflow import keras

# Load your existing model
model = keras.models.load_model('bestmodel.keras')

# Optional: Also save as .h5 for maximum compatibility
model.save('best_model.keras')