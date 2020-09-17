from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.lang import Builder
from widgets import current_user
from kivy.network.urlrequest import UrlRequest
import json


class client_details(Screen):

    # def logOut(self):
        # sm.current = "login"


    def get_data_success(self, req, result):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created

    def get_data_failure(self, req, result):
        print("Error : " + result)





    def get_details(self):
        headers = {"AccessToken" : current_user["token"]}
        url = "http://127.0.0.1:5000/user/"
        UrlRequest(url, on_success=self.get_data_success, on_failure=self.get_data_failure, headers=headers)
 

    def on_enter(self, *args):
        self.get_details(self)
