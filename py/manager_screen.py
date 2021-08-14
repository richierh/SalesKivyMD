from kivy.uix.screenmanager import ScreenManager

from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.properties import ObjectProperty
from kivymd.uix.toolbar import MDToolbar
#from kivymd.uix.navigationdrawer import NavigationLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.tab import MDTabsBase

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from py.popups import OpenDialog


class ManagerScreen(ScreenManager):
    pass

class PosScreen(Screen):
    pos_m=ObjectProperty(None)
    app1=ObjectProperty(None)
    # popup=ObjectProperty(None)
    nav_drawer=ObjectProperty(None)
    pass

    def hello(self):
        print("aaaaa")

    def popup(self):
        print("test here")

class MDToolbarKu(MDToolbar):

    pass
    def popup(self):
        print("test from toolbar here")

class Navigation(Screen):
    app1=ObjectProperty(None)
    nav = ObjectProperty(None)
    recflatbutton=ObjectProperty(None)
    dialog=None

    pass

    def build(self):
        print(kv)
        return Builder.load_string(kv)

    def hello(self):
        print("ini udah bisa")
    
    def popup(self):
        # kv_directory="views"
        print("pop up euy")
        if not self.dialog:
            self.dialog=MDDialog(
            type="custom",
            size_hint=(.7, .6),
            content_cls=OpenDialog(),               
            )
        self.dialog.open()
        # print(kv_directory)
        # import pdb
        # pdb.set_trace()
        return 
    
    def back(self):
        self.parent.parent.screen_manager.current="login_m"
        print("success")

    def gotoscreen2(self):
        print ("okay you are overhere")
        # print(self.ids.screenmanager.current="screen1")

        self.ids.screenmanager.current="screen1"

class Tab(BoxLayout,MDTabsBase):

    pass

    def on_tab_switch(self,instance):
        print("work")
        pass