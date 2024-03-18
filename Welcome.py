from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

# Importing Signup and Login interfaces
from Signup import SignupInterface
from Login import LoginInterface

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
