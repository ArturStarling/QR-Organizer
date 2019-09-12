import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import openpyxl

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)

    cv2.imshow("Frame", frame)

    for obj in decodedObjects:
        wb = openpyxl.load_workbook('excel_test.xlsx')
        sheet = 
        h = int(obj.data) + 1
        print(sheet.cell(row = h, column=2).value)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        break
   
    key = cv2.waitKey(1)
    if key == 27:
        break

    elif key == ord('s'):
        cv2.imwrite('qrcode_result.jpg', frame)    
        break
