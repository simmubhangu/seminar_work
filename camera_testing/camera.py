import cv2

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

while(True):
	ret, frame = cap.read()
	ret1,frame1= cap2.read()
	cv2.imshow('image',frame)
	cv2.imshow("image2",frame1)
	if cv2.waitKey(1) & 0xff == ord('q'):
		break
cap.release()
cap2.release()
cv2.destroyAllWindows()
