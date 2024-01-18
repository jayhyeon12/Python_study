from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model(r"C:\Users\ITPS\Desktop\python2\tensorflow_cat_dog\keras_model.h5", compile=False)

# Load the labels
class_names = open(r"C:\Users\ITPS\Desktop\python2\tensorflow_cat_dog\labels.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True:
  quiz = int(input('문제의 이미지 번호를 입력하세요>>'))

  if quiz == 0:
    break

  image = Image.open(r"C:\Users\ITPS\Desktop\python2\tensorflow_cat_dog"+f"/Quiz{quiz}.jpg").convert("RGB")

  # resizing the image to be at least 224x224 and then cropping from the center
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

  # turn the image into a numpy array
  image_array = np.asarray(image)

  # Normalize the image
  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

  # Load the image into the array
  data[0] = normalized_image_array

  # Predicts the model
  prediction = model.predict(data)
  index = np.argmax(prediction)
  class_name = class_names[index]
  confidence_score = prediction[0][index]

  # Print prediction and confidence score
  print("정답:", '고양이' if int(class_name.split(' ')[0]) == 0 else '강아지')
  print(f"신뢰도: {confidence_score*100:.1f}%")