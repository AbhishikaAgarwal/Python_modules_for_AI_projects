import cv2,time

video=cv2.VideoCapture(0)
while True:
    check , frame = video.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Master",grey)
    cv2.waitKey(0)
    time.sleep(5)
video.release()
cv2.destroyAllWindows()