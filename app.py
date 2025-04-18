import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load your trained model
model = tf.keras.models.load_model('FFDv2.keras')

# Print the model input shape (to check what the model expects)
print("Model input shape:", model.input_shape)

# Function to preprocess image
def preprocess_image(img):
    img = img.resize((150, 150))  # Resize image to match model’s input size
    img_array = np.array(img) / 255.0  # Normalize the image
    return np.expand_dims(img_array, axis=0)

# UI
st.title("🌲 Forest Fire Detection")
st.write("Upload an image to check if it contains signs of wildfire.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    st.write("Result")

    # Preprocess image and predict
    processed_img = preprocess_image(image)

    # Make prediction
    prediction = model.predict(processed_img)[0][0]  # Adjust depending on your model's output

    # Assuming it's a binary classification (0 or 1 for fire detection)
    if prediction > 0.5:  # If the prediction probability is greater than 0.5, fire is detected
        st.success("✅ No Fire Detected!")
    else:
        st.error("🔥 Fire Detected.")
