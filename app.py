import streamlit as st
import tensorflow as tf
from PIL import Image

# Load the model
model = tf.keras.models.load_model('artifacts\\training\\model.h5')

def preprocess_image(image):
    # Convert image to RGB format
    image = image.convert('RGB')

    # Preprocess the image
    image = image.resize((224, 224))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.expand_dims(image, axis=0)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)

    return image

def predict(image):
    # Preprocess the image
    image = preprocess_image(image)

    # Make prediction
    prediction = model.predict(image)
    if prediction[0][0] > 0.1:
        return 'No Cancer'
    else:
        return 'Cancer'

# Streamlit app
def main():
    st.title("Chest Cancer Classification")
    st.write("Upload an image and click the 'Predict' button to classify if it has cancer or not.")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Make prediction
        result = predict(image)
        st.write("Prediction:", result)

if __name__ == '__main__':
    main()
   