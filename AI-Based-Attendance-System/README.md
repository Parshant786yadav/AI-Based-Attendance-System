📸 AI-Based Attendance System
A smart and efficient attendance system using Face Recognition technology powered by Python and OpenCV. This project automatically identifies and marks attendance based on facial features, eliminating manual errors and reducing time consumption in traditional roll-call methods.

🚀 Features
👤 Detects and recognizes registered faces in real-time.

📷 Captures live video feed from webcam for recognition.

🗂️ Maintains attendance records automatically.

📝 Displays student details like ID, name, and date/time.

📦 Easy to manage database using simple folder-based images.

🔄 Option to register new students by simply uploading images.

🧠 Technologies Used

Python 3.8+

OpenCV

face_recognition library

NumPy

PIL (Pillow)

Tkinter (for GUI interface)

Pickle (for encoding file storage)

📁 Project Structure

AI-Based-Attendance-System/
│
├── Images/                  # Folder with student images (ID.jpg format)
│
├── Resources/
│   ├── background.png       # Background UI image
│   └── Modes/               # Mode display images (mode1.png, mode2.png, etc.)
│
├── EncodeGenerator.py       # Encodes student images into a file
├── main.py                  # Main script to run the system
├── EncodeFile.p             # Pickle file storing encodings
├── README.md                # This file
⚙️ How It Works
Add Student Images
Place student face images in the Images/ folder named like 1001.jpg, 1002.jpg, etc.

Generate Encodings
Run the following command to generate face encodings:

nginx
Copy
Edit
python EncodeGenerator.py
Run the System
Start the GUI-based system:

css
Copy
Edit
python main.py
Face Detected → Attendance Marked!
Once the system detects a registered face, attendance is marked and displayed in the interface.

📷 UI Preview

📌 Requirements
Install all required libraries using:

bash
Copy
Edit
pip install -r requirements.txt
Or individually:

bash
Copy
Edit
pip install opencv-python face_recognition numpy Pillow
Note: The face_recognition library requires dlib. You can download the compatible .whl file from Gohlke's repository if you're on Windows.

⚠️ Troubleshooting
Ensure all face images are clear, 8-bit RGB, and face is front-facing.

Verify that image dimensions are reasonable (e.g., 500x500 px).

Confirm you have installed all dependencies.

If you get Unsupported image type error, preprocess your images using Pillow.

💡 Future Improvements
Add Firebase for cloud storage.

Enable real-time student database integration.

Send attendance reports via email or store in Excel/Google Sheets.

🙌 Contributors
[Your Name] — Developer & UI Designer

[Contributor Name] (if any)

📜 License
This project is licensed under the MIT License.
