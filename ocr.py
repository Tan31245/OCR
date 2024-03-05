import pytesseract
import cv2 as cv
import string
chars= string.ascii_letters + string.digits
count = 0 
for c in chars:
    img = cv.imread(f"character_{c}.png")
    ocr_result= pytesseract.image_to_string(img,config= '--psm 6')
    if(ocr_result.strip()==c):
        count+=1
    print("Extracted text: ",ocr_result)
print("Accuracy",count/62)