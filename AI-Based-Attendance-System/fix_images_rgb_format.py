from PIL import Image
import os

folder = "Images"
for filename in os.listdir(folder):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        path = os.path.join(folder, filename)
        img = Image.open(path).convert("RGB")  # Force-convert to 8-bit RGB
        img.save(path, "JPEG")  # Overwrite as JPEG
        print(f"✅ Fixed: {filename}")
