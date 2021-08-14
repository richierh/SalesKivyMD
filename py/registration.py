from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty,ListProperty


class Registration(MDScreen):
    kembali_kerumah=ObjectProperty()
    lp_properties=ListProperty()
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        pass
    
    def registration_form(self):
        pass
    
    def back(self,event):
        # import pdb
        # pdb.set_trace()
        print ('Go back')
        self.parent.manager_screen.current = "login_screen"
    
    def action(self,event):
        # import pdb
        # pdb.set_trace()
        self.list_data = []
        for data in self.lp_properties:
            self.list_data.append(data.text)
        print (self.list_data)
 

# This is the logic of Registration , involved database 
class Register():

    def __init__(self,*args):
        self.parent = args
    
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.lang import Builder

class runApp(MDApp):
    # kv_directory = ".."

    def build(self):
        Builder.load_file("kv/registration.kv")
        return Registration()

if __name__ == "__main__" :

    
    user1 = Register("rony")
    print(user1.parent)
    runApp().run()