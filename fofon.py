import kivy  
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
  

class RootWidget(BoxLayout): 
  
    def btn_clk(self): 
        print("hello world")
  
class ActionApp(App): 
  
    def build(self): 
        return RootWidget() 
   
myApp = ActionApp() 
myApp.run() 