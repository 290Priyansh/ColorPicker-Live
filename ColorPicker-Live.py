import cv2
import numpy as np
frameWidth = 500
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

def empty(a):
    pass

cv2.namedWindow("hsv")
cv2.resizeWindow("hsv",640,240)
cv2.createTrackbar("hue min","hsv",0,179,empty)
cv2.createTrackbar("hue max","hsv",179,179,empty)
cv2.createTrackbar("sat min","hsv",0,255,empty)
cv2.createTrackbar("sat max","hsv",255,255,empty)
cv2.createTrackbar("value min","hsv",0,255,empty)
cv2.createTrackbar("value max","hsv",255,255,empty)

#pick color
def pick_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if x < img.shape[1]:  # Only allow picking from the original image (left side)
            bgr = img[y, x]
            hsv = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2HSV)[0][0]
            h, s, v = hsv

            tolerance = 20
            h_min = max(0, h - tolerance)
            h_max = min(179, h + tolerance)
            s_min = max(0, s - 50)
            s_max = min(255, s + 50)
            v_min = max(0, v - 50)
            v_max = min(255, v + 50)

            cv2.setTrackbarPos("hue min", "hsv", h_min)
            cv2.setTrackbarPos("hue max", "hsv", h_max)
            cv2.setTrackbarPos("sat min", "hsv", s_min)
            cv2.setTrackbarPos("sat max", "hsv", s_max)
            cv2.setTrackbarPos("value min", "hsv", v_min)
            cv2.setTrackbarPos("value max", "hsv", v_max)

            print(f"Picked HSV: ({h}, {s}, {v})")


        # Set trackbar positions
        cv2.setTrackbarPos("hue min", "hsv", h_min)
        cv2.setTrackbarPos("hue max", "hsv", h_max)
        cv2.setTrackbarPos("sat min", "hsv", s_min)
        cv2.setTrackbarPos("sat max", "hsv", s_max)
        cv2.setTrackbarPos("value min", "hsv", v_min)
        cv2.setTrackbarPos("value max", "hsv", v_max)

        print(f"Picked HSV: ({h}, {s}, {v})")

cv2.namedWindow("stacked")
cv2.setMouseCallback("stacked", pick_color)
while True:
    _,img = cap.read()
    img = cv2.flip(img, 1)
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    cv2.resizeWindow("hsv",640,240)
    h_min = cv2.getTrackbarPos("hue min","hsv")
    h_max = cv2.getTrackbarPos("hue max","hsv")
    s_min = cv2.getTrackbarPos("sat min","hsv")
    s_max = cv2.getTrackbarPos("sat max","hsv")
    v_min = cv2.getTrackbarPos("value min","hsv")
    v_max = cv2.getTrackbarPos("value max","hsv")

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHsv,lower,upper)
    result = cv2.bitwise_and(img,img,mask = mask)

    hstack = np.hstack([img,result])
    cv2.imshow("stacked",hstack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
