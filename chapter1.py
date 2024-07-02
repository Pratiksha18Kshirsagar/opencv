import cv2
print("imported packages")



# it reads the stored image
# img = cv2.imread("./assest/shawn.jpg")

# it displays the stored image on screen
# cv2.imshow("output", img)

# this waitkey function is used to decide to display the image after certain sec
# cv2.waitKey(0)

# cv2.videocapture is a function that is used to open a video file

# cap = cv2.VideoCapture("./assest/video.mp4")

cap = cv2.VideoCapture(0) 
cap.set(3,840)
cap.set(4,680)
cap.set(10,1000)


# Within the loop, cap.read() reads the next frame from the video. The function returns two values:
# success: A boolean value that indicates whether the frame was read successfully.
# img: The frame itself, which is an image.
# ord('q') gets the ASCII value of the character 'q'.


while True:
    success , img = cap.read()
    cv2.imshow("video",img)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break 