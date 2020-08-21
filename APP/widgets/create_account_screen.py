from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.lang import Builder


class create_account_screen(Screen):
    user_name = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    invalid_details_label = Label(text="Ya gone fucked up son!")

    def submit(self):
        if (
            self.user_name.text != ""
            and self.email.text != ""
            and self.email.text.count("@") == 1
            and self.email.text.count(".") > 0
        ):
            if self.password != "":
                # db.add_user(self.email.text, self.password.text, self.user_name.text)

                self.reset()

                # sm.current = "login"
            else:
                self.invalid_form()
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

