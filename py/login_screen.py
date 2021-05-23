from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty


class LoginScreen(MDScreen):

    main_icon = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_icon = 'account-cog'
        pass
    
    def login_check(self,*args):
        self.username = args[0]
        self.password = args[1]
        self.user ="abdel"
        self.passw = "temon"
        if self.username == self.user and self.password==self.passw:
            # go to main screen
            return True
        print ("Wrong username/password")
        return False

    def login(self,event):
        # it is the username of your input in the first login session
        self.username = "abdel"
        self.password = "temon"
        if self.login_check(self.username,self.password) == True:
            self.parent.manager_screen.current="main_screen"
        pass

    def registration(self,event):
        self.parent.manager_screen.current="registration"
