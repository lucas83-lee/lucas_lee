import cv2
import numpy as np
import RPi.GPIO as GPIO

led = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, False)


face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")	

cap = cv2.VideoCapture(0)

if cap.isOpened():
	print('width:', cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	print('height:', cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	print('fps:', cap.get(cv2.CAP_PROP_FPS))
	
	
while cap.isOpened():
	ret,img = cap.read()	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	how_many_faces = len(faces)
	if how_many_faces:
		GPIO.output(led, True)
	else: GPIO.output(led, False)

	for (x,y,w,h) in faces:
		img = cv2.rectangle(img, (x,y), (x +w, y +h), (255,0,0),2)
	if ret:
		cv2.imshow('cam_1', img)		
		key = cv2.waitKey(1)&0xFF
		if key == 27:
			break
			
cap.release()
cv2.destroyAllWindows()