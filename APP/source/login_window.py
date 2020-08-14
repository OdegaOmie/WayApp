from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def invalidLogin():
        pop = Popup(title='Invalid Login',
                    content=Label(text='Invalid username or password.'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()

    def reset(self):
        self.email.text = ""
        self.password.text = ""
