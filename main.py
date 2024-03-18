from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

class SignupScreen(Screen):
    pass

class ScreenManager(ScreenManager):
    pass

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"  # Use a light theme
        self.theme_cls.primary_palette = "Blue"  # Set primary color palette
        return Builder.load_file("main.kv")

if __name__ == "__main__":
    MyApp().run()
