from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, WipeTransition, Screen
from widgets.login_screen import login_screen
from widgets.create_account_screen import create_account_screen
from widgets.client_details import client_details

# We need what we had before working
class way_app(App):

    screen_manager = ScreenManager(transition=WipeTransition())

    def build(self):
        self.screen_manager.add_widget(login_screen(name='login'))
        self.screen_manager.add_widget(create_account_screen(name='create'))
        self.screen_manager.add_widget(client_details(name='details'))
        self.screen_manager.current = 'login'
        return self.screen_manager


if __name__ == '__main__':
    wapp = way_app()
    wapp.run()
