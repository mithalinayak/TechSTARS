from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

class DashboardInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [20, 10]

        self.add_widget(Label(text="Dashboard", font_size=24, size_hint=(1, 0.2)))

        # Profile information
        self.add_widget(Label(text="Welcome, User", size_hint=(1, 0.1)))
        self.add_widget(Image(source="profile_picture.png", size_hint=(1, 0.4)))

        # Other relevant data
        self.add_widget(Label(text="Your Data", font_size=20, size_hint=(1, 0.1)))
        self.add_widget(Label(text="Some data here", size_hint=(1, 0.1)))
        self.add_widget(Label(text="More data here", size_hint=(1, 0.1)))

        logout_button = Button(text="Logout", size_hint=(1, 0.1))
        logout_button.bind(on_press=self.logout)
        self.add_widget(logout_button)

    def logout(self, instance):
        # Perform logout action here
        print("Logging out...")

class DashboardApp(App):
    def build(self):
        return DashboardInterface()

if __name__ == "__main__":
    DashboardApp().run()
