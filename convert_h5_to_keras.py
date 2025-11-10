import tensorflow as tf

# 1. Load the .h5 model
# Replace 'your_model.h5' with the path to your model file
model = tf.keras.models.load_model('best_model.h5')

# 2. Save the model in the .keras format
model.save('best_model.keras', save_format='keras')

# Verify by reloading
new_model = tf.keras.models.load_model('best_model.keras')
new_model.summary()