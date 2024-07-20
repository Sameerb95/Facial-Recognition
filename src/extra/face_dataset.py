import cv2
import os
import streamlit as st 

cam = cv2.VideoCapture(0)
cam.set(3,960) # set video width
cam.set(4, 720) # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
frame_placeholder = st.empty()

class FaceDataset:
    def capture(self,id = None):
        # For each person, enter one numeric face id

        if id :
            face_id = id 
        else:
            face_id = input('\n enter user id end press <return> ==>  ')

        print("\n [INFO] Initializing face capture. Look the camera and wait ...")
        # Initialize individual sampling face count
        count = 0

        while(True):

            ret, img = cam.read()
            img = cv2.flip(img, 1) # flip video image vertically
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.05, 10)

            for (x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
                count += 1

                # Save the captured image into the datasets folder
                cv2.imwrite("temp/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

                # cv2.imshow('image', img)
                frame_placeholder.image(img)


            if count >= 30: # Take 30 face sample and stop video
                break

        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()


