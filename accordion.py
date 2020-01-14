from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.widget import Widget

class MouseWidget(Widget):
    def on_touch_down(self, touch):
        print(touch)


class MyApp(App):
    def build(self):
        root = Accordion(orientation='horizontal')

        item= AccordionItem(title='Papeis')
        src = "Papeis.jpg"
        image = Image(source=src,pos=(200, 100))
        # add image to AccordionItem
        item.add_widget(image)
        root.add_widget(item)


        item= AccordionItem(title='Tintas')
        src = "Tintas.jpg" 
        image = Image(source=src,pos=(200, 100))
        # add image to AccordionItem
        item.add_widget(image)
        root.add_widget(item)

        return root

if __name__ == '__main__':
    MyApp().run()
