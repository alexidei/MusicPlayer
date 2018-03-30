import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.button import Button


class DummyApp(App):
    def build(self):
        return Button(text='Music Player')


if __name__ == '__main__':
    DummyApp().run()
