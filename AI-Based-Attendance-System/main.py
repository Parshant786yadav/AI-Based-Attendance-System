import cv2
import os
import ntpath
import pickle
import numpy as np
import face_recognition
import cvzone
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
# from firebase_admin import storage
from datetime import datetime

# cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred,{
#     'databaseURL' :" ",
#     'storageBucket' : " "
# })
# bucket = storage.bucket()

cap  = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

image_path = cv2.imread('Resources/background.png')

# Import the mode images into the list.
folderModePath = os.fspath('Resources/Modes')
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

print(len(imgModeList))

# load the encoding file
print("Loading encode file")
file = open('EncodeFile.p', 'rb')
encodeListKnownIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownIds
print("Encode File Loaded")

modeType = 0
counter = 0
id = -1
imgStudent = []

while True:
    success, img = cap.read()

if img is not None:
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    if imgS.dtype != 'uint8':
        imgS = imgS.astype('uint8')


    # Detect faces
    faceCurrentFrame = face_recognition.face_locations(imgS)
    encodeCurrentFrame = face_recognition.face_encodings(imgS, faceCurrentFrame)

    image_path[162:162 + 480, 55:55 + 640] = img
    image_path[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    if faceCurrentFrame:
        for encodeFace, faceLoc in zip(encodeCurrentFrame, faceCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDistance = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDistance)

            if matches[matchIndex]:
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1

                id = studentIds[matchIndex]
                if counter == 0:
                    cvzone.putTextRect(image_path, "Loading", (275, 400))
                    cv2.imshow("Face Attendance", image_path)
                    cv2.waitKey(3)
                    counter = 1
                    modeType = 1

        if counter != 0:
            if counter == 1:
                # Get the Data
                # studentInfo = db.reference(f'Students/{id}').get()
                # print(studentInfo)
                # Get the Image from the Storage
                # blob = bucket.get_blob(f'Images/{id}.png')
                # array = np.frombuffer(blob.download_as_string(), np.uint8)
                # imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)
                # Update data of attendance
                # datetimeObject = datetime.strptime(studentInfo['last_attendance_time'], "%Y-%m-%d %H:%M:%S")
                # secondsElapsed = (datetime.now() - datetimeObject).total_seconds()
                # print(secondsElapsed)
                # if secondsElapsed > 30:
                #     ref = db.reference(f'Students/{id}')
                #     studentInfo['total_attendance'] += 1
                #     ref.child('total_attendance').set(studentInfo['total_attendance'])
                #     ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                pass
            else:
                modeType = 3
                counter = 0
                image_path[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

            if modeType != 3:
                if 10 < counter < 20:
                    modeType = 2
                    image_path[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

                if counter <= 10:
                    cv2.putText(image_path, str(studentInfo['total_attendance']), (861, 125), 1, 2, (255, 255, 255), 0)
                    cv2.putText(image_path, str(studentInfo['Major']), (1006, 550), 1, 1, (255, 255, 255), 0)
                    cv2.putText(image_path, str(id), (1006, 493), 1, 1, (255, 255, 255), 0)
                    cv2.putText(image_path, str(studentInfo['standing']), (910, 625), 1, 2, (100, 100, 100), 0)
                    cv2.putText(image_path, str(studentInfo['Year']), (1025, 625), 1, 2, (100, 100, 100), 0)
                    cv2.putText(image_path, str(studentInfo['Starting_year']), (1125, 625), 1, 2, (100, 100, 100), 0)

                    (w, h), _ = cv2.getTextSize(studentInfo['name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                    offset = (414 - w) // 2
                    cv2.putText(image_path, str(studentInfo['name']), (808 + offset, 445), 1, 2, (50, 50, 50), 0)

                    image_path[175:175 + 216, 909:909 + 216] = imgStudent

            counter += 1
            if counter >= 20:
                counter = 0
                modeType = 0
                studentInfo = []
                imgStudent = []
                image_path[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    else:
        modeType = 0
        counter = 0

    cv2.imshow("Face Attendance", image_path)
    cv2.waitKey(1)
