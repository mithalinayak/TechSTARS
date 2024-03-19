from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle

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

        back_button = Button(text="Back", size_hint=(1, 0.1))
        back_button.bind(on_press=self.go_back)
        self.add_widget(back_button)

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

    def go_back(self, instance):
        self.parent.clear_widgets()
        self.parent.add_widget(WelcomePage().build())

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

        back_button = Button(text="Back", size_hint=(1, 0.1))
        back_button.bind(on_press=self.go_back)
        self.add_widget(back_button)

    def validate_login(self, instance):
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()

        # Perform login validation (replace with your actual login logic)
        if username == "admin" and password == "password":
            self.error_message = ""
            print("Login successful!")
        else:
            self.error_message = "Invalid username or password."

    def go_back(self, instance):
        self.parent.clear_widgets()
        self.parent.add_widget(WelcomePage().build())

class WelcomePage(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical')
        with layout.canvas.before:
            Color(1, 1, 1, 1)  # Set the color to white (RGB values and alpha)
            self.rect = Rectangle(size=(layout.width, layout.height), pos=layout.pos)

        # Add logo
        logo = Image(source='assets/SecureGuard.png', size_hint=(0.2, None), height=50, pos_hint={'left': 0, 'top': 1})
        layout.add_widget(logo)

        # Add welcome image
        welcome_image = Image(source='assets/secure.jpeg', size_hint=(1, 1), height=100)
        layout.add_widget(welcome_image)

        # Add labels
        label = Label(text="Stay Safe at every click!", font_size='24sp')
        layout.add_widget(label)

        # Add signup button
        signup_button = Button(text="Sign Up", size_hint=(1, 0.1), background_normal='', background_color=(0, 0.7, 0.3, 1), color=(1, 1, 1, 1), font_size='20sp', padding=(0, 10))
        signup_button.bind(on_press=self.goto_signup)
        layout.add_widget(signup_button)

        # Add login button
        login_button = Button(text="Login", size_hint=(1, 0.1), background_normal='', background_color=(0, 0.5, 0.9, 1), color=(1, 1, 1, 1), font_size='20sp', padding=(0, 10))
        login_button.bind(on_press=self.goto_login)
        layout.add_widget(login_button)

        return layout

    def goto_signup(self, instance):
        # Switch to Signup interface
        self.root.clear_widgets()
        self.root.add_widget(SignupInterface())

    def goto_login(self, instance):
        # Switch to Login interface
        self.root.clear_widgets()
        self.root.add_widget(LoginInterface())

if __name__ == '__main__':
    WelcomePage().run()
