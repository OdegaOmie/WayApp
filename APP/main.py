from kivy.app import App
#kivy.require("1.9.1")
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest

class MyWidget(BoxLayout):
    def __init__(self,**kwargs):
        super(MyWidget,self).__init__(**kwargs)
        search_url = "http://api.openweathermap.org/data/2.5/forecast/daily?APPID=ef4f6b76310abad083b96a45a6f547be&q=new%20york"
        print (search_url)
        self.request = UrlRequest(search_url, self.res)
        print (self.request)
        print ("Result: before success", self.request.result,"\n")


    def res(self,*args):
        print ("Result: after success", self.request.result)


class MyApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyApp().run()