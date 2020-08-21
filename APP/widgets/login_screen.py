from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder


class login_screen(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    invalid_login_label = Label(text="Invalid username or password.") 

    def login_btn(self):
        self.invalid_login()

    def create_btn(self):
        self.reset()
        return "create"

    def invalid_login():
        
        pop = Popup(
            title="Invalid Login",
            content=self.invalid_login_label,
            size_hint=(None, None),
            size=(400, 400),
        )
        pop.open()

    def reset(self):
        self.email.text = ""
        self.password.text = ""


Builder.load_file('widgets/login_screen.kv')
