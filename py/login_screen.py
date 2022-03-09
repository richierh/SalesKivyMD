from kivymd.uix.screen import Screen
from kivy.properties import StringProperty,ObjectProperty


class LoginScreen(Screen):

    main_icon = StringProperty('mainjob')
    inputuser = ObjectProperty(None)
    passwuser = ObjectProperty(None)

    # main_icon = "account-cog"


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.main_icon = 'account-cog'
        print ("helo again")
        print (self.main_icon)

        pass

    def login(self,event):
        # import pdb
        # pdb.set_trace()
        # self.username = self.ids.inputuser.text 
        # self.passwuser = self.ids.passwuser.text

        self.username = self.inputuser.text
        self.password = self.passwuser.text
        # it is the username of your input in the first login session
        # self.username = "abdel"
        # self.password =  "temon"
        self.userdata = Login(self.username,self.password)
        self.userdata.get_userdata()
        if self.userdata.get_userdata():
            self.parent.manager_screen.current="main_screen"
        pass

    def registration(self,event):
        self.parent.manager_screen.current="registration"

import numbers
class Login() :

    def __init__(self,*args):
        self.username=args[0]
        self.password=args[1]
        if isinstance(self.username,numbers.Number) :
            print(self.username)
            self.separatenumber = [self.check for self.check in str(self.username)]
            self.firstphonenumber = self.separatenumber[0]+self.separatenumber[1]
            print (self.firstphonenumber)
            if self.firstphonenumber == str(62) or self.firstphonenumber == str(+6):
                print(True)
            else :
                print(False)
                # Beri peringatan pada input box username / phone number bahwa nilainya tidak cocok
        elif not(isinstance(self.username,numbers.Number)):
            print (f"ini bukan nomor melainkan nama string {self.username}")
        self.login_check()
    
    def get_userdata(self):
        
        return self.login_check()

    def login_check(self):

        # Di bawah ini kode untuk menghubungkan input data ke database user yang ada di server
        from py.db_connection_type import connect_run
        # self.tipe_database = 'sqlite'
        # self.nama_database = "hahaha"
        # self.host = None
        # self.user = None
        # self.password = None
        # self.database = None
        # dua argument , yang pertama nama _ database dan yang kedua adalah tipe database (sqlite, mariadb, dsb)
        # connect_run(self.nama_database,self.tipe_database,self.host,self.user,self.password)
        # connect_run(self.nama_database,self.tipe_database,None,None,None,None)
        self.user = "admin"
        self.passw = "admin"
        

 
        #
        
        # Cocokkan antara username yang diinput oleh user dengan database yang ada di server
        if self.username == self.user and self.password==self.passw:
            # go to main screen
            return True
        print ("Wrong username/password")
        return False
if __name__=="__main__":
    username = 62909090
    password = "cicalengka"
    user = Login(username,password)
    user.get_userdata()
        