import tensorflow as tf

# Load the SavedModel
converter = tf.lite.TFLiteConverter.from_saved_model('runs/detect/train21/weights/best_saved_model')

# Optimize for size (optional)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# Convert the model
tflite_model = converter.convert()

# Save the TFLite model
with open('best21.tflite', 'wb') as f:
    f.write(tflite_model)

print("Model successfully converted to best21.tflite!")
