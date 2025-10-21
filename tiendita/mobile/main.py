# mobile/main.py
import requests
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

API_URL = "https://tu-api-render.onrender.com/api/"

class LoginScreen(Screen):
    def login(self):
        data = {"username": self.ids.username.text, "password": self.ids.password.text}
        r = requests.post(API_URL + "token/", data=data)
        if r.status_code == 200:
            token = r.json()["access"]
            self.manager.current = "home"

class HomeScreen(Screen):
    pass

class MarketplaceApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(HomeScreen(name="home"))
        return sm

if __name__ == "__main__":
    MarketplaceApp().run()

