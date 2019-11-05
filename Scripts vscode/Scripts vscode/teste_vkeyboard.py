import kivy

kivy.require("1.11.1")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
# to use buttons:
from kivy.uix.button import Button
from kivy.storage.jsonstore import JsonStore
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.vkeyboard import VKeyboard
#from kivy.core.window import Window  #bug opengl
import cv2

# add the following 2 lines to solve OpenGL 2.0 bug
from kivy import Config

Config.set('graphics', 'multisamples', '0')

#Config.set('graphics', 'width', '320')
#Config.set('graphics', 'height', '568')
#Window.size = (320, 568) #bug opengl

Config.set('kivy', 'keyboard_mode', 'systemandmulti') #???

# Create the vkeyboard 
class Test(VKeyboard): 
    VKeyboard.docked = True #???
    #Vkeyboard.size = (320, 568)
    VKeyboard.setup_mode #???
    player = VKeyboard(layout='azerty')
  
# Create the App class 
class VkeyboardApp(App): 
    def build(self): 
        return Test() 
  
# run the App 
if __name__ == '__main__': 
    VkeyboardApp().run() 

