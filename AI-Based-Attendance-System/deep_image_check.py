import cv2
from PIL import Image
import numpy as np

path = "Images/1001.jpg"

# Load via PIL
pil_img = Image.open(path)
print(f"🔍 PIL Mode: {pil_img.mode}, Format: {pil_img.format}")

# Convert to RGB
pil_img = pil_img.convert("RGB")

# Save back temporarily
pil_img.save("Images/fixed_1001.jpg", "JPEG")

# Load via OpenCV
cv_img = cv2.imread("Images/fixed_1001.jpg")
print(f"🔍 OpenCV Shape: {cv_img.shape}, Dtype: {cv_img.dtype}")

# Check NumPy array properties
if cv_img.dtype == np.uint8 and cv_img.shape[2] == 3:
    print("✅ Image is 8-bit RGB — ready for encoding.")
else:
    print("❌ Still invalid format for face_recognition.")
