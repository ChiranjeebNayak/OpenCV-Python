import cv2 as cv
import datetime
cap = cv.VideoCapture('signup video.mp4')

print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
#cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv.CAP_PROP_FRAME_HEIGHT, 360)
#print(cap.get(3))
#print(cap.get(4))

print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        date = str(datetime.datetime.now())
        font = cv.FONT_HERSHEY_SIMPLEX
        text = "hello world"
        frame = cv.putText(frame, date, (10, 50), font, 1, (255, 0, 255), 4)
        cv.imshow('video', frame)
        if cv.waitKey(1) == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
