import cv2
import pytesseract
import matplotlib.pyplot as plt
def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest_rectangle = [0, 0]
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4:
            area = cv2.contourArea(cnt)
            if area > largest_rectangle[0]:
                largest_rectangle = [cv2.contourArea(cnt), cnt, approx]

    x, y, w, h = cv2.boundingRect(largest_rectangle[1])
    roi = image[y:y+h, x:x+w]
    return roi

if __name__ == "__main__":
    image_path = 'A.png'
    img = cv2.imread(image_path)
    cv2.imshow("Hello",img)
    # Preprocess the image
    # license_plate = preprocess_image(img)
    license_plate = img

    # Perform OCR using Tesseract
    gray_plate = cv2.cvtColor(license_plate, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray_plate)

    print("Detected license plate:", text)

    # Display the cropped license plate
    plt.imshow(license_plate, cmap='gray')
    plt.axis('off')
    plt.title('Detected License Plate')
    plt.show()

