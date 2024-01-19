import tensorflow as tf
import cv2
import numpy as np

# Load the pre-trained deep neural network model
model = tf.keras.models.load_model('dnn_model.h5')

# Define the error concealment function
def conceal_error(image, error_map):
    # Preprocess the input image and error map
    image = cv2.resize(image, (256, 256))
    error_map = cv2.resize(error_map, (256, 256))
    image = np.expand_dims(image, axis=0)
    error_map = np.expand_dims(error_map, axis=0)
    image = image / 255.0
    error_map = error_map / 255.0

    # Predict the concealed image using the deep neural network model
    concealed_image = model.predict([image, error_map])
    concealed_image = concealed_image * 255.0
    concealed_image = concealed_image.squeeze()
    concealed_image = concealed_image.astype(np.uint8)

    # Postprocess the concealed image
    concealed_image = cv2.resize(concealed_image, image.shape[:2][::-1])
    concealed_image = concealed_image.astype(np.float32)
    concealed_image = cv2.addWeighted(image, 0.5, concealed_image, 0.5, 0)

    return concealed_image

# Test the error concealment function on a sample image and error map
image = cv2.imread('D:/LAPORAN TA/Pemrograman/sz_256x256.jpg')
error_map = cv2.imread('D:/LAPORAN TA/Pemrograman/Insert Error Result/Error_Frame235.jpg', cv2.IMREAD_GRAYSCALE)
concealed_image = conceal_error(image, error_map)
cv2.imwrite('D:/LAPORAN TA/Pemrograman/Error Concealment/concealed_image.jpg', concealed_image)