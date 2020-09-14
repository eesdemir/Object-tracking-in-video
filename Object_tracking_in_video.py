import numpy as np
import cv2

# construct the argument parse and parse the arguments
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (3,3), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
    #Sarı
   #çin: ([25, 146, 190], [100, 180, 250])
    lower_pink = np.array([139,0,139])
    upper_pink = np.array([203,192,255])
    mask = cv2.inRange(hsv, lower_pink,upper_pink)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)

    # cv2.drawContours(frame, contours, -1, (0,255,0), 3)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(0)