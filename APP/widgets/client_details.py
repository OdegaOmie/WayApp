from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.lang import Builder
from widgets import current_user, domain
from kivy.network.urlrequest import UrlRequest
from datetime import datetime


class client_details(Screen):

    request = None

    def logOut(self):
        current_user = {"user_name": "", "token": "", "refresh_token": ""}
        self.manager.current = "login"

    def get_data_success(self, result):
        created_date = datetime.utcfromtimestamp(
            result["date_created"]["$date"] / 1000).strftime('%Y-%m-%d %H:%M:%S')
        self.ids.user_name.text = "Account Name: " + result["user_name"]
        self.ids.email.text = "Email: " + result["email"]
        self.ids.created.text = "Created On: " + created_date

    def get_data_failure(self, result):
        print("Error : " + result)

    def get_details(self):
        headers = {"AccessToken": current_user["token"]}
        url = domain + "/user/"
        self.request = UrlRequest(
            url,
            timeout=5,
            debug=True,
            verify=False,           
            req_headers=headers,
        )

        self.request.wait()
        print("done waiting")
        if(self.request.resp_status == 200):
            print(self.request.result)
            self.get_data_success(result=self.request.result)
        else:
            print(self.request.result)                    
            self.get_data_failure(result=self.request.result)

    def on_enter(self, *args):
        self.get_details()


Builder.load_file('widgets/client_details.kv')
