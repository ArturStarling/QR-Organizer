import kivy
kivy.require("1.11.1")

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
# to use buttons:
from kivy.uix.button import Button
from kivy.storage.jsonstore import JsonStore
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.clock import Clock
from kivy import Config
from kivy.uix.widget import Widget

Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '568')

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<ScreenManager>:
    id: screen_manager
    MenuScreen:
        id: menu_screen
        name: 'menuando'
        manager: 'screen_manager'
    SettingsScreen:
        id: settings_screen
        name: 'setando'
        manager: 'screen_manager'

<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Goto settings'
            on_press: app.root.current = 'settings'
        Button:
            text: 'Quit'

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: app.root.current = 'menu'
""")



# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))

class TestApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()