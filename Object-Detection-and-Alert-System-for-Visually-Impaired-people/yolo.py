# -*- coding: utf-8 -*-
"""YOLO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b2hckuDfSjhokqhWp5NkUbv6MDoiVuuE
"""

import cv2
import matplotlib.pyplot as plt

from utils import *
from darknet import Darknet

# Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30

# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(0)

# Captures a single image from the camera and returns it in PIL format
def get_image():
    # read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = camera.read()
    return im


# Set the location and name of the cfg file
cfg_file = './cfg/yolov3.cfg'

# Set the location and name of the pre-trained weights file
weight_file = './weights/yolov3.weights'

# Set the location and name of the COCO object classes file
namesfile = 'data/coco.names'

# Load the network architecture
m = Darknet(cfg_file)

# Load the pre-trained weights
m.load_weights(weight_file)

# Load the COCO object classes
class_names = load_class_names(namesfile)

# # Print the neural network used in YOLOv3
# m.print_network()

# Set the default figure size
plt.rcParams['figure.figsize'] = [24.0, 14.0]

# Load the image
img = cv2.imread('./images/dog.jpg')

# Convert the image to RGB
original_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# We resize the image to the input width and height of the first layer of the network.    
resized_image = cv2.resize(original_image, (m.width, m.height))

# # Display the images
# plt.subplot(121)
# plt.title('Original Image')
# plt.imshow(original_image)
# plt.subplot(122)
# plt.title('Resized Image')
# plt.imshow(resized_image)
# plt.show()

def detectImage():
    i = 10

    while i > 1:
        i -= 1
        # Ramp the camera - these frames will be discarded and are only used to allow v4l2
        # to adjust light levels, if necessary

        camera = cv2.VideoCapture(0)
        for i in range(ramp_frames):
            temp = get_image()
        print("Taking image...")
        # Take the actual image we want to keep
        camera_capture = get_image()
        file = "C:/Users/AVINASH/Desktop/notes/nlp/yolo/test_image.png"
        # A nice feature of the imwrite method is that it will automatically choose the
        # correct format based on the file extension you provide. Convenient!
        cv2.imwrite(file, camera_capture)

        # You'll want to release the camera, otherwise you won't be able to create a new
        # capture object until your script exits
        del camera

        # Set the default figure size
        plt.rcParams['figure.figsize'] = [24.0, 14.0]

        # Load the image
        img = cv2.imread('./test_image.png')

        # Convert the image to RGB
        original_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # We resize the image to the input width and height of the first layer of the network.
        resized_image = cv2.resize(original_image, (m.width, m.height))

        # Set the IOU threshold. Default value is 0.4
        iou_thresh = 0.4

        # Set the NMS threshold. Default value is 0.6
        nms_thresh = 0.6

        # Detect objects in the image
        boxes = detect_objects(m, resized_image, iou_thresh, nms_thresh)

        # Print the objects found and the confidence level
        print_objects(boxes, class_names)

        # # Plot the image with bounding boxes and corresponding object class labels
        # plot_boxes(original_image, boxes, class_names, plot_labels=True)

    return 0

class ImageDetection:
    detectImage()