import kivy
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
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown

import cv2

kivy.require("1.11.1")

# add the following 2 lines to solve OpenGL 2.0 bug
from kivy import Config
Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'width', '320') 
Config.set('graphics', 'height', '568')

Builder.load_string("""
  StackLayout:
    orientation: 'rl-tb'
    padding: 10
    Button:
      text: 'S1'
      size_hint: [.6, .2]
    Button:
      text: 'S2'
       size_hint: [.4, .4]
    Button:
      text: 'S3'
      size_hint: [.3, .2]
    Button:
      text: 'S4'
      size_hint: [.4, .3] 
      """)
 
class MyGridLayout(GridLayout):
   pass
 
class LayoutsApp(App):
    def build(self):
        return MyGridLayout()
 
if __name__=="__main__":
    LayoutsApp().run()