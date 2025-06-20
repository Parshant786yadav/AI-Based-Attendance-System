📸 **AI-Based Attendance System** <br>


A smart and efficient attendance system using Face Recognition technology powered by Python and OpenCV. This project automatically identifies and marks attendance based on facial features, eliminating manual errors and reducing time consumption in traditional roll-call methods.

**🚀 Features** <br>

👤 Detects and recognizes registered faces in real-time. <br>
📷 Captures live video feed from webcam for recognition. <br>
🗂️ Maintains attendance records automatically. <br>
📝 Displays student details like ID, name, and date/time. <br>
📦 Easy to manage database using simple folder-based images. <br>
🔄 Option to register new students by simply uploading images. <br>

**🧠 Technologies Used** <br>

Python 3.8+ <br>
OpenCV <br>
face_recognition library <br>
NumPy <br>
PIL (Pillow) <br>
Tkinter (for GUI interface) <br>
Pickle (for encoding file storage) <br>

**⚙️ How It Works** <br>

Add Student Images <br>
Place student face images in the Images/ folder named like 1001.jpg, 1002.jpg, etc. <br>
Generate Encodings <br>

**📌 Requirements** <br>


Install all required libraries using: <br> <br>

You can use directly - <br>

pip install -r requirements.txt <br>

Or individually - <br>

pip install opencv-python face_recognition numpy Pillow <br>
Note: The face_recognition library requires dlib. You can download the compatible .whl file from Gohlke's repository if you're on Windows. <br>

**⚠️ Troubleshooting** <br>


Ensure all face images are clear, 8-bit RGB, and face is front-facing. <br>
Verify that image dimensions are reasonable (e.g., 500x500 px). <br>
Confirm you have installed all dependencies. <br>
If you get Unsupported image type error, preprocess your images using Pillow. <br>


**🙌 Contributors** <br>


PARSHANT — Developer & UI Designer <br>


**📜 License** <br>


This project is licensed under the MIT License. <br>


