import face_recognition
import cv2
import time
import subprocess
import sys


def authorize_face_encodings(face_encodings, authorized_face_encoding):
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(
            [authorized_face_encoding], face_encoding)

        # If a match was found in known_face_encodings, just use the first.
        if True in matches:
            return True
    return False


def unlock():
    subprocess.call(["loginctl", "unlock-sessions"])


def authenticate():
    while True:
        # Grab a single frame of video
        _, frame = video_capture.read()

        # Only process every other frames of video to save time

        # Resize frame of video to 1/4 size for faster face recognition
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB.
        rgb_small_frame = small_frame[:, :, ::-1]
        # Find all the faces and face encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)

        authorized_user_present = authorize_face_encodings(
            face_encodings,
            authorized_face_encoding)

        if(authorized_user_present):
            print("authorized")
            unlock()
            break
        else:
            print("not authorized")


try:
    with open("/opt/face-authenticator/test.log", "a") as logfile:
        logfile.write("hello world\n")
    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)
    # Load the authorized picture and learn how to recognize it.
    authorized_image = face_recognition.load_image_file(
        "authorized/admin.jpg")
    authorized_face_encoding = face_recognition.face_encodings(authorized_image)[
        0]
    authenticate()
    video_capture.release()
    cv2.destroyAllWindows()
except:  # catch *all* exceptions
    e = sys.exc_info()[0]
    with open("/opt/face-authenticator/test.log", "a") as logfile:
        logfile.write(str(e))
        logfile.write("\n")
