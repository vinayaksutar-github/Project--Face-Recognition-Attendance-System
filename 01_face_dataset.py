import cv2
import os
from excel_db import ExcelWorkBook

cam = cv2.VideoCapture(0)
cam.set(3, 640)  #here we set video width
cam.set(4, 480)  # here we set video height
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# For each person, enter one numeric face id
# face_id = input("enter user id end press <return> ==>  ")
face_id = int(len([os.path.join("dataset", f) for f in os.listdir("dataset")]) / 30)
id = input("enter user id end press <return> ==>  ")
name = input("enter user name end press <return> ==>  ")
branch = input("enter branch end press <return> ==>  ")
class_name = input("enter class end press <return> ==>  ")

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0
while True:
    ret, img = cam.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1
        #  it will Save the captured image into the datasets folder
        cv2.imwrite(
            "dataset/User." + str(face_id) + "." + str(count) + ".jpg",
            gray[y : y + h, x : x + w],
        )
        cv2.imshow("image", img)
    k = cv2.waitKey(100) & 0xFF  # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30:  # Take 30 face sample and stop video
        break

# Add to excel user data
ExcelWorkBook().add_user(id, face_id, name, branch, class_name)

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
