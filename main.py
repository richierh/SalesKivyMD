from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.app import App
from py.manager_screen import ManagerScreen
from py.login_screen import LoginScreen
from py.main_screen import MainScreen
from py.registration import Registration
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivyauth.google_auth import initialize_google, login_google, logout_google
from android.permissions import request_permissions, Permission 

request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE,\
    Permission.INTERNET])

GOOGLE_CLIENT_ID = ('1054061919729-76nicpfqkstir6gjp0ec9g6geondib4h.apps.googleusercontent.com')
GOOGLE_CLIENT_SECRET = ('t3fIj8XT8WQuWwKr5_h6MWlU')
# from kivy_deps import sdl2, glew
# from kaki.app import App
# from kivy.factory import Factory

# class Live(App):
#     CLASSES = {
#         "UI": "live.ui"
#     }
#     AUTORELOADER_PATHS = [
#         (".", {"recursive": True}),
#     ]
#     def build_app(self):
#         return Factory.UI()

# 
# #: Control either we activate debugging in the app or not
# #: Defaults depend if "DEBUG" exists in os.environ
# DEBUG = "DEBUG" in os.environ

# #: If true, it will require the foreground lock on windows
# FOREGROUND_LOCK = False

# #: List of KV files under management for auto reloader
# KV_FILES = []

# #: List of path to watch for autoreloading
# AUTORELOADER_PATHS = [
#     # (".", {"recursive": False}),
# ]

# #: List of extensions to ignore
# AUTORELOADER_IGNORE_PATTERNS = [
#     "*.pyc", "*__pycache__*"]

# #: Factory classes managed by kaki
# CLASSES = {}

# #: Idle detection (if True, event on_idle/on_wakeup will be fired)
# #: Rearming idle can also be done with rearm_idle()
# IDLE_DETECTION = False

# #: Default idle timeout
# IDLE_TIMEOUT = 60

# #: Raise error
# #: When the DEBUG is activated, it will raise any error instead
# #: of showing it on the screen. If you still want to show the error
# #: when not in DEBUG, put this to False
# RAISE_ERROR = True

class MyApp(MDApp):

    def build(self):
        kv_directory = "kv"

        initialize_google(
            GOOGLE_CLIENT_ID,
            GOOGLE_CLIENT_SECRET,
        )
        # initialize_google(
        #     self.after_login==None,
        #     self.error_listener,
        #     GOOGLE_CLIENT_ID,
        #     GOOGLE_CLIENT_SECRET,
        # )
  

        self.title = "Login Screen"
        Builder.load_file("kv/manager_screen.kv")
        Builder.load_file("kv/popups.kv")

        return ManagerScreen()


if __name__ == '__main__':
    MyApp().run()
    # Live().run()