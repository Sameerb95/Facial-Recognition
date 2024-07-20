import streamlit as st
from streamlit_webrtc import WebRtcMode,webrtc_streamer
import cv2
import av

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX
#iniciate id counter
id = 0
# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None', 'Raghav', 'Sameer', 'Ilza', 'Z', 'W'] 

class FaceRecognition:
    def recv(self,frame):
        
        img = frame.to_ndarray(format="bgr24")

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
        )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            # Check if confidence is less them 100 ==> "0" is perfect match 
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
            
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)

        return av.VideoFrame.from_ndarray(img, format='bgr24')

# class webrtc:
#     def __init__(self):
        
if __name__ == '__main__':
    playing = st.checkbox("Playing", value=True)
    webrtc_streamer(
                key="stream",
                desired_playing_state=playing ,
                video_processor_factory=FaceRecognition)




