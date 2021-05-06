import cv2
from cv2 import dnn_superres
import sys
import os

::Create object to reference the neural network
sr = dnn_superres.DnnSuperResImpl_create()
# Read the desired model
path = "LapSRN_x4.pb"
sr.readModel(path)

# Set the desired model and scale to get correct pre- and post-processing
sr.setModel("lapsrn", 4)

img = input("Input File: ")
image = cv2.imread(img)
cv2.waitKey(500)
result = sr.upsample(image)
path, filename = os.path.split(img)
print("Successfully upscaled " + filename + "!")
cv2.waitKey(500)
# Save the image
cv2.imwrite("upscaled_" + str(filename), result)
print("wrote upscaled_" + str(filename) + " to file")