import kivy
import cv2
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.label import Label 
from kivy.storage.jsonstore import JsonStore
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

componentes = {'0':'Madeira1.jpg', '1':'Madeira1.jpg', '2':'Madeira2.jpg', '3':'Madeira3.jpg', '4':'Madeira4.jpg', '5':'Prateleira1.jpg'}


Builder.load_string("""
<MyImage@Image>: 
    keep_ratio: False
    allow_stretch: True

<MenuScreen>:
    Button:
        id: flybox
        halign: 'center'
        background_normal: 'botao.png'
        background_down: 'kivy.png'
        border: 0, 0, 0, 0
        size_hint_y: 1/7
        size_hint_x: 1/8
        pos_hint: {'center_x': 1/2, 'center_y':1/10}
        on_press: app.qrcode()

    FloatLayout:
        orientation: 'vertical'

        Button:
            size_hint_y: 1/14
            size_hint_x: .3
            pos_hint: {'center_x': 1/2, 'center_y':3/4}
            text: 'Menu de itens'
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'settings'
            
            background_color: 1, .6, 0, .25
            on_press: root.manager.current = 'settings'


<SettingsScreen>: 
    Accor:
        orientation: 'vertical'
        AccordionItem: 
            title: 'Madeira - 1º'
            MyImage: 
                source: 'Madeira1.jpg'
        AccordionItem: 
            title: 'Madeira - 2º'
            MyImage: 
                source: 'Madeira2.jpg'
        AccordionItem: 
            title: 'Madeira - 3º'
            MyImage: 
                source: 'Madeira3.jpg'
        AccordionItem: 
            title: 'Madeira - 4º'
            MyImage: 
                source: 'Madeira4.jpg'
        AccordionItem: 
            title: 'Prateleira - 1º'
            MyImage: 
                source: 'Prateleira1.jpg'
""")

def poppingup(n):
    view = ModalView(auto_dismiss=True, size_hint=(0.6, 0.2))
    view.add_widget(Label(text= n))
    view.open()  

def poppando(x):
    pop = Popup(title='test', content=Image(source=x), size_hint=(None, None), size=(400, 400))
    pop.open()

class Accor(Accordion): 
    pass

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))

class TestApp(App):

    def build(self):
        return sm

    def qrcode(self, *args):
            capture = cv2.VideoCapture(0)
            ret, frame = capture.read()
            qrDecoder = cv2.QRCodeDetector()
            data,bbox,rectifiedImage = qrDecoder.detectAndDecode(frame)

            if data in componentes:
                print(componentes[data])
                poppando(componentes[data])

            else:
                poppingup("qrcode inválido, tire outra foto")  
                


if __name__ == '__main__':
    TestApp().run()