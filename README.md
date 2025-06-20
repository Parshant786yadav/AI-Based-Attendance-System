📸 **AI-Based Attendance System** <br>
A smart and efficient attendance system using Face Recognition technology powered by Python and OpenCV. This project automatically identifies and marks attendance based on facial features, eliminating manual errors and reducing time consumption in traditional roll-call methods.

**🚀 Features**

👤 Detects and recognizes registered faces in real-time. <br>
📷 Captures live video feed from webcam for recognition. <br>
🗂️ Maintains attendance records automatically. <br>
📝 Displays student details like ID, name, and date/time.
📦 Easy to manage database using simple folder-based images.
🔄 Option to register new students by simply uploading images.

**🧠 Technologies Used**
Python 3.8+
OpenCV
face_recognition library
NumPy
PIL (Pillow)
Tkinter (for GUI interface)
Pickle (for encoding file storage)

**⚙️ How It Works**
Add Student Images
Place student face images in the Images/ folder named like 1001.jpg, 1002.jpg, etc.
Generate Encodings

**📌 Requirements**
Install all required libraries using:

You can use directly -
pip install -r requirements.txt

Or individually -


pip install opencv-python face_recognition numpy Pillow
Note: The face_recognition library requires dlib. You can download the compatible .whl file from Gohlke's repository if you're on Windows.

**⚠️ Troubleshooting**
Ensure all face images are clear, 8-bit RGB, and face is front-facing.

Verify that image dimensions are reasonable (e.g., 500x500 px).

Confirm you have installed all dependencies.

If you get Unsupported image type error, preprocess your images using Pillow.


**🙌 Contributors**
PARSHANT — Developer & UI Designer


**📜 License**
This project is licensed under the MIT License.


