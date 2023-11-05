# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 13:17:29 2022

@author: yinku
"""

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label          #
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MyApp(App):   # It inherit  from app
    def build(self):
        return Label(text = 'Tech with Sam')    # Label

if __name__ == "__main__":
    MyApp().run()
