import kivy
from kivy.app import App
from kivy.lang import Builder

kivy.require("1.11.1")

# add the following 2 lines to solve OpenGL 2.0 bug
from kivy import Config
Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '568')

KV = ("""
GridLayout:
    cols: 1
    TextInput:
        id: first_input_id
    TextInput:
        id: second_input_id
    Button:
        text: "Get the inputs"
        on_release:
            app.get_text_inputs()
""")
root = Builder.load_string(KV)

class MainApp(App):
    def build(self):
        return root

    def get_text_inputs(self):
        my_list = [self.root.ids.first_input_id.text, self.root.ids.second_input_id.text]
        print(my_list)

MainApp().run()