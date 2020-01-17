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
from kivy.uix.widget import Widget

kv_text = '''
<MenuScreen>:

    Button:
        id: flybox
        halign: 'center'
        border: 0, 0, 0, 0
        size_hint_y: 1/7
        size_hint_x: 1/8
        pos_hint: {'center_x': 1/2, 'center_y':1/10}
        on_press: app.qrcode()

    BoxLayout:
        Button:
            text: 'Goto settings'
            on_press: root.manager.current = 'settings'

    Label:
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.185}
        text: "QR CODE READER"
        color: 1, .5, 0, 1

<DataScreen>: 

    BoxLayout:
        Button:
            text: 'Back to menu'
            id: flybox
            halign: 'center'
            border: 0, 0, 0, 0
            size_hint_y: 1/7
            size_hint_x: 1/8
            pos_hint: {'center_x': 1/2, 'center_y':1/10}
            on_press: root.manager.current = 'menu'

    orientation: 'vertical'
    AccordionItem: 
        title: 'Madeira - 1º'
        MyImage: 
            source: 'Madeira - 1º.jpg'
    AccordionItem: 
        title: 'Madeira - 2º'
        MyImage: 
            source: 'Madeira - 2º.jpg'
    AccordionItem: 
        title: 'Madeira - 3º.jpg'
        MyImage: 
            source: 'Madeira - 3º.jpg'
    AccordionItem: 
        title: 'Madeira - 4º'
        MyImage: 
            source: 'Madeira - 4º.jpg'
    AccordionItem: 
        title: 'Prateleira - 1º'
        MyImage: 
            source: 'Prateleira - 1º.jpg'

'''

def poppingup(n):
    view = ModalView(auto_dismiss=True, size_hint=(0.6, 0.2))
    view.add_widget(Label(text= n))
    view.open()   

class MenuScreen(Screen):
    pass

class DataScreen(Screen):
    pass

class MouseWidget(Widget):
    def on_touch_down(self, touch):
        print(touch)

class FlyApp(App):
    def build(self):
        root = Accordion(orientation='horizontal')

        item= AccordionItem(title='Madeira - 1º')
        src = "Madeira - 1º.jpg"
        image = MouseWidget(source=src)
        # add image to AccordionItem
        item.add_widget(image)
        root.add_widget(item)


        item= AccordionItem(title='Madeira - 2º')
        src = "Madeira - 2º.jpg"
        image = MouseWidget(source=src)
        # add image to AccordionItem
        item.add_widget(image)
        root.add_widget(item)

    def qrcode(self, *args):
            self.img1 = Image()
            self.capture = cv2.VideoCapture(0)
            ret, frame = self.capture.read()
            qrDecoder = cv2.QRCodeDetector()
            data,bbox,rectifiedImage = qrDecoder.detectAndDecode(frame)

            if data in storing:
                poppingup(storing.get(data)['local'])

            else:
                poppingup("qrcode inválido, tire outra foto")

if __name__ == '__main__':
    FlyApp().run()
