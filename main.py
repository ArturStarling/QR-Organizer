import pyzbar.pyzbar as pyzbar
import kivy  
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
import numpy as np
import cv2

kivy.require("1.11.1")  

class RootWidget(BoxLayout): 
  
    def btn_clk(self): 
      
       

        img = cv2.imread('bruninho.jpg', 1)


        cap = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_PLAIN

        while True:
            _, frame = cap.read()

            decodedObjects = pyzbar.decode(frame)
            
            cv2.imshow("Frame", frame)

            for obj in decodedObjects:
                if  int(obj.data) == 1:
                    cv2.destroyWindow('Frame')
                    cv2.imshow('deucerto', img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    break
            
            key = cv2.waitKey(1)
            if key == 27:
                break
            elif key == ord('s'):
                cv2.imwrite('qrcode_result.jpg', frame)     
                break            

  
class ActionApp(App): 
  
    def build(self): 
        return RootWidget() 
   
myApp = ActionApp() 
myApp.run() 
