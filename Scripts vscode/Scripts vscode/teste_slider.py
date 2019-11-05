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
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
import cv2

kivy.require("1.11.1")

# add the following 2 lines to solve OpenGL 2.0 bug
from kivy import Config
Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '568')

name = ['joao', 'roberto', 'zezinho', 'carlos']

class CarouselApp(App):
    def build(self):
        carousel = Carousel(direction='right')
        for i in range(0,4):
            
            # Em text = {}, colocar o texto a ser mostrato naquele png. A lista deve ser dada pelo storage
            src = "http://placehold.it/480x270.png&text={}&.png".format(name[i])
            image = AsyncImage(source=src, allow_stretch=True)
            carousel.add_widget(image)
        return carousel

CarouselApp().run()