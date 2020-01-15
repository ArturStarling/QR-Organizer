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

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

kv_text = '''
<GameArea>:

    Button:
        id: flybox
        halign: 'center'
        border: 0, 0, 0, 0
        size_hint_y: 1/7
        size_hint_x: 1/8
        pos_hint: {'center_x': 1/2, 'center_y':1/10}
        on_press: app.qrcode()

    Label:
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.185}
        text: "QR CODE READER"
        color: 1, .5, 0, 1

    FloatLayout:
        orientation: 'vertical'

        TextInput:
            on_text: app.process()
            focus: True
            halign: 'center'
            id: dado
            size_hint_y: 1/14
            size_hint_x: .3
            pos_hint: {'center_x': 1/2, 'center_y':3/4}
            name: 'test'
            hint_text: 'Digite o objeto a ser buscado'
            multiline: False
            
            background_color: 1, .6, 0, .25
'''


store = JsonStore('hello.json')
store.put('resistores', local = 'arduino', qr = 2)
store.put('arduino', local = 'arduino', qr = 3)


storing = JsonStore('hellow.json')
storing.put('1', local = 'pregos/parafusos/rebites', qr = 1)
storing.put('2', local = 'arduino', qr = 2)
storing.put('3', local = 'arduino', qr = 3)
storing.put('4', local = 'componentes 1', qr = 4)
storing.put('5', local = 'componentes 2', qr = 5)
storing.put('6', local = 'armario madeira - 1ª prateleira', qr = 6)
storing.put('7', local = 'armario madeira - 2ª prateleira', qr = 7)
storing.put('8', local = 'armario madeira - 4ª prateleira', qr = 8)
storing.put('9', local = 'prateleira canto - 3º', qr = 9)
storing.put('10', local = 'prateleira canto - 4º', qr = 10)
storing.put('11', local = 'prateleira canto - 5º', qr = 11)
storing.put('12', local = 'armário porta - 1º', qr = 12)
storing.put('13', local = 'armário porta - 2º', qr = 13)
storing.put('14', local = 'armário porta - 3º', qr = 14)
storing.put('15', local = 'armário porta - 4º', qr = 15)
storing.put('32', local = 'armário porta - 5º', qr = 32)


def poppingup(n):
    view = ModalView(auto_dismiss=True, size_hint=(0.6, 0.2))
    view.add_widget(Label(text= n))
    view.open()   

class GameArea(FloatLayout):
    pass


class FlyApp(App):
    def build(self):
        Builder.load_string(kv_text)
        return GameArea()

    def process(self):
        text = self.root.ids.dado.text

        if text in store:
            poppingup(store.get(text)['local'])

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
