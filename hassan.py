#quick script created by Hassan to auto remove any images containing more than one person
import os
import cv2
import logging

logging.basicConfig(filename='hassan.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

IMAGE_FOLDER = (r"./images")
for file in os.listdir(IMAGE_FOLDER):
# check if the file is an image
    if file.endswith(".jpg") or file.endswith(".png"):
    # load the image
        img = cv2.imread(os.path.join(IMAGE_FOLDER, file))
        # use face detection to count the number of people in the image
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

            # check if the image is empty or the cascade classifier failed to load
        if img is None or face_cascade.empty():
            print("Failed to load image or cascade classifier, skipping...")
            continue

        faces = face_cascade.detectMultiScale(img, 1.3, 5)

            # if there are more than one person in the image, delete it
        if len(faces) > 1:
            os.remove(os.path.join(IMAGE_FOLDER, file))
            print(f"Removed {file}")
            logging.warning(f"Removed {file}")
        else:
            print(f"{file} has only one person, keeping it")


