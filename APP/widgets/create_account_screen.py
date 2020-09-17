from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
import json

# global user variable
from widgets import current_user


class create_account_screen(Screen):
    user_name = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    invalid_details_label = Label(text="Ya gone fucked up son!")

    def register_success(self, req, result):
        current_user["user_name"] = "something"
        print(result)

    def register_failure(self, req, result):
        self.invalid_form()
  


    def submit(self):
        if (
            self.user_name.text != ""
            and self.password.text != ""
            and self.email.text != ""
            and self.email.text.count("@") == 1
            and self.email.text.count(".") > 0
        ):
            json_message = json.dumps({
                "user_name" : self.user_name.text,
                "email": self.email.text,
                "password": self.password.text
                })
            url = "http://127.0.0.1:5000/user/"
            UrlRequest(url, on_success=self.register_success,
             on_failure=self.register_failure, req_body=json_message)
        else:
            self.invalid_form()

    def login(self):
        self.reset()
        # sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.user_name.text = ""

    def invalid_form(self):
        pop = Popup(
            title="Invalid Form",
            content=self.invalid_details_label,
            size_hint=(None, None),
            size=(400, 400),
        )

        pop.open()


Builder.load_file("widgets/create_account_screen.kv")

