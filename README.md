Face Recognition Project
Introduction
This project utilizes facial recognition technology to identify people in front of a camera. The process involves installing necessary libraries, such as OpenCV and face_recognition, and resolving potential installation errors related to the Dlib library.

Installation
To launch the project, you need to install the following libraries:

OpenCV: Install using pip:
pip install opencv-python

face_recognition: Install using pip:
pip install face_recognition

Installation Note
During installation, you might encounter the following error related to Dlib:

ERROR: Could not build wheels for dlib, which is required to install pyproject.toml-based projects
To resolve this issue, please follow these steps:


Go to Dlib_Windows_Python3.x repository.
Download and install Dlib wheels compatible with your Python version.

Usage
Once the necessary libraries are installed, you can compile and run the project. Simply pass the directory containing photos of the people you want to recognize. The application will then identify the person in front of the camera based on the provided photos.

Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.
