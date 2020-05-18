import cv2 as cv
cap = cv.VideoCapture('tree.avi')
forcc = cv.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv.VideoWriter('output.mp4', forcc, 20.0, (320, 240))


print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('video', grey)
        if cv.waitKey(1) == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()
