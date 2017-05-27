import kivy
kivy.require('1.8.0')  # update with your current version

from kivy.app import App
from kivy.uix.button import Button

class DummyApp(App):

    def build(self):
        return Button(text="Vin: Hello Kivy World")

if __name__ == '__main__':
    DummyApp().run()
