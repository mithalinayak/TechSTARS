from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import StringProperty

class LoginInterface(BoxLayout):
    error_message = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [20, 10]

        self.add_widget(Label(text="Login", font_size=24, size_hint=(1, 0.2)))

        self.username_input = TextInput(hint_text="Username", size_hint=(1, 0.1))
        self.password_input = TextInput(hint_text="Password", password=True, size_hint=(1, 0.1))
        self.error_label = Label(text="", color=(1, 0, 0, 1), size_hint=(1, 0.1))

        self.add_widget(self.username_input)
        self.add_widget(self.password_input)
        self.add_widget(self.error_label)

        login_button = Button(text="Login", size_hint=(1, 0.1))
        login_button.bind(on_press=self.validate_login)
        self.add_widget(login_button)

    def validate_login(self, instance):
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()

        # Perform login validation (replace with your actual login logic)
        if username == "admin" and password == "password":
            self.error_message = ""
            print("Login successful!")
        else:
            self.error_message = "Invalid username or password."

class LoginApp(App):
    def build(self):
        return LoginInterface()

if __name__ == "__main__":
    LoginApp().run()
