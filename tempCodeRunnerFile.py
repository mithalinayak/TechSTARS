from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class SignUpPage(GridLayout):
    def __init__(self, **kwargs):
        super(SignUpPage, self).__init__(**kwargs)
        self.cols = 2
        self.padding = [20, 20]

        self.add_widget(Label(text='Username:', halign='right'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password:', halign='right'))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

        self.add_widget(Label(text='Confirm Password:', halign='right'))
        self.confirm_password = TextInput(multiline=False, password=True)
        self.add_widget(self.confirm_password)

        self.sign_up_button = Button(text='Sign Up')
        self.sign_up_button.bind(on_press=self.sign_up)
        self.add_widget(self.sign_up_button)

    def sign_up(self, instance):
        username = self.username.text
        password = self.password.text
        confirm_password = self.confirm_password.text

        if password == confirm_password:
            # Add your signup logic here (e.g., saving to a database)
            print(f"Username: {username}, Password: {password}")
        else:
            print("Passwords do not match")

class LoginPage(GridLayout):
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)
        self.cols = 2
        self.padding = [50, 50]

        self.add_widget(Label(text='Username:', halign='right'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password:', halign='right'))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

        self.login_button = Button(text='Login')
        self.login_button.bind(on_press=self.login)
        self.add_widget(self.login_button)

    def login(self, instance):
        username = self.username.text
        password = self.password.text

        # Add your login logic here (e.g., check against a database)
        print(f"Username: {username}, Password: {password}")


class MyApp(App):
    def build(self):
        self.title = 'Simple App'
        self.signup_page = SignUpPage()
        self.login_page = LoginPage()
        Window.size = (360, 640)  # Set window size to match Android phone screen (e.g., 720x1280)
        return self.signup_page


if __name__ == '__main__':
    MyApp().run()
