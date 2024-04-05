import cv2
import os
import face_recognition
import glob
import numpy as np
import time

class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        self.start_time = time.time()
        self.frame_count = 0

    def load_encoding_images(self, images_path):
        """
        Load encoding images from path
        :param images_path:
        :return:
        """
        # Load Images
        images_path = glob.glob(os.path.join(images_path, "*.*"))

        print("{} encoding images found.".format(len(images_path)))

        # Store image encoding and names
        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get the filename only from the initial file path.
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)
            # Get encoding
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            # Store file name and file encoding
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)
        print("Encoding images loaded")

    def detect_faces(self, frame):
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        detected_faces = []
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            face_names = []

            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            face_names.append(name)

            detected_faces.append({"location": (top, right, bottom, left), "names": face_names})

        return detected_faces

# Set the working directory
os.chdir(r"E:\face recognition\face recognition")

# Initialize SimpleFacerec instance
sfr = SimpleFacerec()

# Load encoding images from the specified folder
sfr.load_encoding_images("images/")

# Open the default camera
cap = cv2.VideoCapture(0)

while True:
    # Start time
    start_time = time.time()

    # Read a frame from the camera
    ret, frame = cap.read()

    # Detect faces and their names
    detected_faces = sfr.detect_faces(frame)

    # Print the number of detected faces and their labels to the console
    for face in detected_faces:
        print("Number of faces detected:", len(face["names"]))
        for name in face["names"]:
            print("Detected face label:", name)
            # You can also print face locations if needed
            # print("Face location:", face["location"])

    # Calculate FPS
    sfr.frame_count += 1
    if sfr.frame_count >= 10:  # Calculate FPS every 10 frames
        fps = sfr.frame_count / (time.time() - sfr.start_time)
        sfr.frame_count = 0
        sfr.start_time = time.time()

        # Overlay FPS on the frame
        cv2.putText(frame, f"FPS: {round(fps, 2)}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the frame
    cv2.imshow("Frame", frame)

    # Check for the 'Esc' key press
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the camera
cap.release()




# ### saving taked unknown face image ####
# import cv2
# import os
# import face_recognition
# import glob
# import numpy as np
# import time

# class SimpleFacerec:
#     def __init__(self):
#         self.known_face_encodings = []
#         self.known_face_names = []
#         self.start_time = time.time()
#         self.frame_count = 0
#         self.images_path = "images"

#     def load_encoding_images(self, images_path):
#         """
#         Load encoding images from path
#         :param images_path:
#         :return:
#         """
#         # Load Images
#         images_path = glob.glob(os.path.join(images_path, "*.*"))

#         print("{} encoding images found.".format(len(images_path)))

#         # Store image encoding and names
#         for img_path in images_path:
#             img = cv2.imread(img_path)
#             rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#             # Get the filename only from the initial file path.
#             basename = os.path.basename(img_path)
#             (filename, ext) = os.path.splitext(basename)
#             # Get encoding
#             face_encodings = face_recognition.face_encodings(rgb_img)
#             if len(face_encodings) > 0:
#                 img_encoding = face_encodings[0]
#                 # Store file name and file encoding
#                 self.known_face_encodings.append(img_encoding)
#                 self.known_face_names.append(filename)
#             else:
#                 print("No face detected in image:", img_path)
#         print("Encoding images loaded")

#     def detect_faces(self, frame):
#         # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         face_locations = face_recognition.face_locations(rgb_frame)
#         face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

#         detected_faces = []
#         for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#             face_names = []

#             # See if the face is a match for the known face(s)
#             matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
#             name = "Unknown"

#             # Or instead, use the known face with the smallest distance to the new face
#             face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
#             best_match_index = np.argmin(face_distances)
#             if matches[best_match_index]:
#                 name = self.known_face_names[best_match_index]
#             else:
#                 # Prompt the user to input a label for the unknown face
#                 label = input("Enter label for the unknown face: ")
#                 name = label

#             face_names.append(name)

#             detected_faces.append({"location": (top, right, bottom, left), "names": face_names})

#         return detected_faces

# # Set the working directory
# os.chdir(r"E:\face recognition\face recognition")

# # Initialize SimpleFacerec instance
# sfr = SimpleFacerec()

# # Load encoding images from the specified folder
# sfr.load_encoding_images("images/")

# # Open the default camera
# cap = cv2.VideoCapture(0)

# while True:
#     # Start time
#     start_time = time.time()

#     # Read a frame from the camera
#     ret, frame = cap.read()

#     # Detect faces and their names
#     detected_faces = sfr.detect_faces(frame)

#     # Print the number of detected faces and their labels to the console
#     for face in detected_faces:
#         print("Number of faces detected:", len(face["names"]))
#         for name in face["names"]:
#             print("Detected face label:", name)
#             # You can also print face locations if needed
#             # print("Face location:", face["location"])

#     # Display the frame
#     cv2.imshow("Frame", frame)

#     # Check for the 'Esc' key press
#     key = cv2.waitKey(1)
#     if key == 27:
#         break

#     # End time
#     end_time = time.time()

#     # Increment frame count
#     sfr.frame_count += 1

#     # Calculate FPS
#     if sfr.frame_count >= 10:  # Calculate FPS every 10 frames
#         fps = sfr.frame_count / (end_time - sfr.start_time)
#         print("FPS:", fps)
#         sfr.frame_count = 0
#         sfr.start_time = time.time()

# # Release the camera
# cap.release()
