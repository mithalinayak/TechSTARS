from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import StringProperty

class SignupInterface(BoxLayout):
    error_message = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [20, 10]

        self.add_widget(Label(text="Signup", font_size=24, size_hint=(1, 0.2)))

        self.username_input = TextInput(hint_text="Username", size_hint=(1, 0.1))
        self.email_input = TextInput(hint_text="Email", size_hint=(1, 0.1))
        self.password_input = TextInput(hint_text="Password", password=True, size_hint=(1, 0.1))
        self.confirm_password_input = TextInput(hint_text="Confirm Password", password=True, size_hint=(1, 0.1))
        self.error_label = Label(text="", color=(1, 0, 0, 1), size_hint=(1, 0.1))

        self.add_widget(self.username_input)
        self.add_widget(self.email_input)
        self.add_widget(self.password_input)
        self.add_widget(self.confirm_password_input)
        self.add_widget(self.error_label)

        signup_button = Button(text="Sign Up", size_hint=(1, 0.1))
        signup_button.bind(on_press=self.validate_signup)
        self.add_widget(signup_button)

    def validate_signup(self, instance):
        username = self.username_input.text.strip()
        email = self.email_input.text.strip()
        password = self.password_input.text.strip()
        confirm_password = self.confirm_password_input.text.strip()

        if not username or not email or not password or not confirm_password:
            self.error_message = "Please fill in all fields."
        elif password != confirm_password:
            self.error_message = "Passwords do not match."
        else:
            self.error_message = ""
            # Perform signup process here
            print("Signup successful!")

class SignupApp(App):
    def build(self):
        return SignupInterface()

if __name__ == "__main__":
    SignupApp().run()
