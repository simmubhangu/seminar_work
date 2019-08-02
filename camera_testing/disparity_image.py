import cv2

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
stereo = cv2.StereoBM_create(numDisparities=1024, blockSize=7)

while(True):
	ret, frame = cap.read()
	ret1,frame1= cap2.read()
	frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	frame1= cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
#	stereo = cv2.createStereoBM(numDisparities=16.blocksize=15)
	disparity = stereo.compute(frame,frame1)
	disparity = frame - frame1
#	cv2.imshow('image',frame1)
	cv2.imshow("image2",disparity)
	if cv2.waitKey(1) & 0xff == ord('q'):
		break
cap.release()
cap2.release()
cv2.destroyAllWindows()
