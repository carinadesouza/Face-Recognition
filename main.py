import cv2
import numpy as np

# Global variables for flag and initial coordinates
flag = False
ix, iy = -1, -1

# Load the image
img = cv2.imread("fruits.jpg")
img_copy = img.copy()  # Create a copy of the original image to reset it during dragging

# Function to handle mouse events
def crop(event, x, y, flags, param):
    global flag, ix, iy, img

    if event == 1:  # Left mouse button pressed
        flag = True
        ix, iy = x, y  # Record initial point
    
    elif event == 0:  # Mouse is moving
        if flag:
            img = img_copy.copy()  # Reset the image to the original copy while dragging
            cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y), color=(255, 0, 0), thickness=2)  # Draw border-only rectangle
    
    elif event == 4:  # Left mouse button released
        flag = False
        fx, fy = x, y
        cv2.rectangle(img, pt1=(ix, iy), pt2=(fx, fy), color=(255, 0, 0), thickness=2)  # Final rectangle
        cropped_img = img_copy[iy:fy, ix:fx]  # Crop the image
        cv2.imshow("Cropped Image", cropped_img)  # Show the cropped image

        # Save the cropped image
        cv2.imwrite("cropped_image.jpg", cropped_img)
        print("Cropped image saved as 'cropped_image.jpg'")

# Create a window and set a mouse callback
cv2.namedWindow(winname="window")
cv2.setMouseCallback("window", crop)

# Display the image and allow the user to interact
while True:
    cv2.imshow("window", img)
    if cv2.waitKey(1) & 0xFF == ord('x'):  # Press 'x' to exit the loop
        break

cv2.destroyAllWindows()  # Close all windows
