import kivy

kivy.require("1.11.1")

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.label import Label
from kivy import Config
Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '568')

KV = """
BoxLayout
    RV
        id: rv1
        on_scroll_y: rv2.scroll_y = args[1] 
        
    RV
        id: rv2
        on_scroll_y: rv1.scroll_y = args[1]
<RV>
    viewclass: "MyLabel"
    RecycleBoxLayout:
        default_size: None, None
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'

"""

class RV(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(5)]
        

class MyLabel(Label):
    pass


class MyApp(App):
    def build(self):
        return Builder.load_string(KV)


MyApp().run()
