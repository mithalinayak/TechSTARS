from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox


class SignUpPage(Screen):
    def __init__(self, **kwargs):
        super(SignUpPage, self).__init__(**kwargs)
        self.layout = GridLayout(cols=1)
        self.layout.spacing = [10]
        self.layout.padding = [20, 20]

        self.layout.add_widget(Label(text='Create Account', font_size='24sp'))

        self.checkbox1 = CheckBox(active=True)
        self.layout.add_widget(self.checkbox1)
        self.layout.add_widget(Label(text='I agree to the terms and conditions'))

        self.layout.add_widget(Label(text='Username:'))
        self.username = TextInput(multiline=False)
        self.layout.add_widget(self.username)

        self.layout.add_widget(Label(text='Password:'))
        self.password = TextInput(multiline=False, password=True)
        self.layout.add_widget(self.password)

        self.layout.add_widget(Label(text='Confirm Password:'))
        self.confirm_password = TextInput(multiline=False, password=True)
        self.layout.add_widget(self.confirm_password)

        self.next_button = Button(text='Next')
        self.next_button.bind(on_press=self.next_page)
        self.layout.add_widget(self.next_button)

        self.add_widget(self.layout)

    def next_page(self, instance):
        app = App.get_running_app()
        if self.checkbox1.active:
            username = self.username.text
            password = self.password.text
            confirm_password = self.confirm_password.text

            if password == confirm_password:
                # Add your signup logic here (e.g., saving to a database)
                print(f"Username: {username}, Password: {password}")
                app.switch_to_login()
            else:
                print("Passwords do not match")
        else:
            print("Please agree to the terms and conditions")


class LoginPage(Screen):
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)
        self.layout = GridLayout(cols=2)
        self.layout.padding = [50, 50]

        self.layout.add_widget(Label(text='Username:', halign='right'))
        self.username = TextInput(multiline=False)
        self.layout.add_widget(self.username)

        self.layout.add_widget(Label(text='Password:', halign='right'))
        self.password = TextInput(multiline=False, password=True)
        self.layout.add_widget(self.password)

        self.login_button = Button(text='Login')
        self.login_button.bind(on_press=self.login)
        self.layout.add_widget(self.login_button)

        self.add_widget(self.layout)

    def login(self, instance):
        username = self.username.text
        password = self.password.text

        # Add your login logic here (e.g., check against a database)
        print(f"Username: {username}, Password: {password}")


class MyApp(App):
    def build(self):
        self.title = 'TechSTARS'
        self.screen_manager = ScreenManager()

        self.signup_page = SignUpPage(name='signup')
        self.login_page = LoginPage(name='login')

        self.screen_manager.add_widget(self.signup_page)
        self.screen_manager.add_widget(self.login_page)

        Window.size = (360, 640)  # Set window size to match Android phone screen (e.g., 720x1280)

        return self.screen_manager

    def switch_to_login(self):
        self.screen_manager.current = 'login'  # Switch to the login page


if __name__ == '__main__':
    MyApp().run()
