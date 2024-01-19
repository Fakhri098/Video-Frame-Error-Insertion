import cv2
import numpy as np

def process_image(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect edges in the grayscale image
    edges = cv2.Canny(gray, 50, 150)

    # Find contours in the edge detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through the contours to find the one that corresponds to the black block
    for contour in contours:
        # Get the bounding rectangle of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Check if the width and height of the bounding rectangle are above a certain threshold
        if w > 100 and h > 100:
            # If the condition is met, the contour corresponds to the black block
            break

    # Return the x, y, w, and h values of the bounding rectangle
    return x, y, w, h

def main():
    # Load the image
    image = cv2.imread('D:/LAPORAN TA/Pemrograman/256x256/hasil add/hasil_add.jpg')

    # Process the image to detect the black block
    x, y, w, h = process_image(image)

    # Print the x, y, w, and h values of the bounding rectangle
    print('x:', x)
    print('y:', y)
    print('w:', w)
    print('h:', h)

if __name__ == '__main__':
    main()
