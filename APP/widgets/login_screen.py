from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from kivy.logger import Logger
import json

# global user variable
from widgets import current_user, domain


class login_screen(Screen):

    # def __init__(self,**kwargs):
    #     super (login_screen,self).__init__(**kwargs)
    invalid_login_label = Label(text="Invalid username or password.")
    request = None

    def login_success(self, result):
        current_user["user_name"] = result["user_name"]
        current_user["token"] = result["access_token"]
        current_user["refresh_token"] = result["refresh_token"]
        self.manager.current = "details"
        # return "details"

    def login_failure(self, result):
        print("print login_failure : " + result)
        self.invalid_login()

    # def test_request(self):
    #     print("test")
    #     # self.request = UrlRequest("https://google.com", debug=True, timeout=2, on_error=self.test_callback, on_success=self.test_callback, on_failure=self.test_callback, verify=False)
    #     self.request = UrlRequest("https://google.com", debug=True, verify=False)
    #     self.request.wait()
    #     print("done waiting")
    #     print(self.request.result)


    # def test_callback(self, req, result):
    #     print("print test_callback")
    #     print(result)




    def login_btn(self):
        print("print login_btn  Enter ")
        print("self.ids.email.text : " + self.ids.email.text)
        print("self.ids.password.text : " + self.ids.password.text)
        if self.ids.email.text != "" and self.ids.password.text != "":
            print("print login_btn  Entered IF statement ")
            try:
                json_message = json.dumps(
                    {"email": self.ids.email.text, "password": self.ids.password.text}
                )
                print("json_message : " + json_message)
                path = "/user/login/"
                print(domain + path)
                self.request = UrlRequest(
                    domain + path,
                    req_body=json_message,
                        timeout=5,
                        debug=True,
                        verify=False
                )
                self.request.wait()
                print("done waiting")
                if(self.request.resp_status == 200):
                    print(self.request.result)
                    self.login_success(result=self.request.result)
                else:
                    print(self.request.result)                    
                    self.login_failure(result=self.request.result)
            except Exception as e:
                print("print login_btn Exception : " + e)
        else:
            print("print login_btn did not Enter IF statement ")
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


Builder.load_file("widgets/login_screen.kv")
