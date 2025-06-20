import face_recognition
import os
import pickle
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
# from firebase_admin import storage
from PIL import Image
import numpy as np

# Firebase setup (commented for now)
# cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred, {
#     'databaseURL': " ",
#     'storageBucket': " "
# })

folderPath = "Images"
PathList = os.listdir(folderPath)
print(PathList)

imgList = []
studentIds = []

for path in PathList:
    try:
        img_path = os.path.join(folderPath, path)
        img_pil = Image.open(img_path).convert("RGB")  # Force RGB mode
        img_np = np.array(img_pil)
        imgList.append(img_np)

        student_id = os.path.splitext(path)[0]
        studentIds.append(student_id)

        # Firebase image upload (commented for now)
        # fileName = f'{folderPath}/{path}'
        # bucket = storage.bucket()
        # blob = bucket.blob(fileName)
        # blob.upload_from_filename(fileName)

    except Exception as e:
        print(f"❌ Skipping {path}: {e}")

print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        try:
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        except Exception as e:
            print(f"❌ Error during encoding: {e}")
    return encodeList

print("Encoding Started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownIds = [encodeListKnown, studentIds]
print("Encoding Complete.")

with open("EncodeFile.p", 'wb') as file:
    pickle.dump(encodeListKnownIds, file)
print("✅ EncodeFile.p Saved Successfully")
