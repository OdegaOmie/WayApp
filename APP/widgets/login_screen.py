from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
import json

# global user variable
from widgets import current_user

class login_screen(Screen):

    # def __init__(self,**kwargs):
    #     super (login_screen,self).__init__(**kwargs)
    invalid_login_label = Label(text="Invalid username or password.")


    def login_success(self, req, result):
        current_user["user_name"] = result["user_name"]
        current_user["token"] = result["access_token"]
        current_user["refresh_token"] = result["refresh_token"]
        self.manager.current = "details"
        # return "details"

    def login_failure(self, req, result):
        self.invalid_login()


    def login_btn(self):
        if (self.ids.email.text != ""
        and self.ids.password.text != ""):
            json_message = json.dumps({"email": self.ids.email.text, "password": self.ids.password.text})
            url = "http://127.0.0.1:5000/user/login/"
            UrlRequest(url, on_success=self.login_success, on_failure=self.login_failure, req_body=json_message)
        else:
            self.invalid_login()

    def create_btn(self):
        self.reset()
        return "create"

    def invalid_login(self):
        
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
