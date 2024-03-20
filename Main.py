import cv2
import numpy as np
import dlib
import face_recognition
import threading

# Load images and encode known faces
known_face_encodings = []
known_face_names = []

# Add paths to images of known people
image_paths = [""]

for path in image_paths:
    image = face_recognition.load_image_file(path)
    face_encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(face_encoding)
    name = path.split("/")[-1].split(".")[0]
    known_face_names.append(name)


def capture_frames(video_capture):
    global frame, ret

    while True:
        ret, frame = video_capture.read()


def recognize_faces():
    global frame, ret

    while True:
        if ret:
            rgb_frame = frame[:, :, ::-1]


            gray_frame = cv2.cvtColor(rgb_frame, cv2.COLOR_BGR2GRAY)

            detector = dlib.get_cuda_face_detector() if dlib.DLIB_USE_CUDA else dlib.get_frontal_face_detector()
            dlib_faces = detector(gray_frame)


            face_locations = [(face.top(), face.right(), face.bottom(), face.left()) for face in dlib_faces]

            face_locations = np.array(face_locations)

            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (0, 0, 0), 1)

            cv2.imshow('Video', frame)

            # Break the loop when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

video_capture = cv2.VideoCapture(0)
ret, frame = video_capture.read()

capture_thread = threading.Thread(target=capture_frames, args=(video_capture,))
recognize_thread = threading.Thread(target=recognize_faces)

capture_thread.start()
recognize_thread.start()

capture_thread.join()
recognize_thread.join()

video_capture.release()
cv2.destroyAllWindows()
