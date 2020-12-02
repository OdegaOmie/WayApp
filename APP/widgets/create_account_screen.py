from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
import json

# global user variable
from widgets import current_user, domain


class create_account_screen(Screen):
    user_name = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    invalid_details_label = Label(text="Ya gone fucked up son!")
    request = None

    def register_success(self, result):
        current_user["user_name"] = result["user_name"]
        current_user["token"] = result["access_token"]
        current_user["refresh_token"] = result["refresh_token"]
        return "details"

    def register_failure(self, result):
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
            path = "/user/"
            self.request = UrlRequest(domain + path, req_body=json_message)
            self.request.wait()
            print("done waiting")
            if(self.request.resp_status == 200):
                print(self.request.result)
                self.register_success(result=self.request.result)
            else:
                print(self.request.result)                    
                self.register_failure(result=self.request.result)            
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
