from kivy.app import App
from kivy.lang import Builder
from kivy.uix.effectwidget import EffectWidget
from kivy.uix.effectwidget import InvertEffect,HorizontalBlurEffect
from kivy.uix.button import Button


class Runapp(App):

    def build(self):
        w = EffectWidget()
        w.add_widget(Button(text='Hello!'))
        w.effects = [InvertEffect(), HorizontalBlurEffect(size=5.0)]
        return w
 
if __name__=="__main__":        
    Runapp().run()