from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox


class SignUpPage(GridLayout):
    def __init__(self, **kwargs):
        super(SignUpPage, self).__init__(**kwargs)
        self.cols = 1
        self.spacing = [10]
        self.padding = [20, 20]

        self.add_widget(Label(text='Create Account', font_size='24sp'))

        self.checkbox1 = CheckBox(active=True)
        self.add_widget(self.checkbox1)
        self.add_widget(Label(text='I agree to the terms and conditions'))

        self.add_widget(Label(text='Username:'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password:'))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

        self.add_widget(Label(text='Confirm Password:'))
        self.confirm_password = TextInput(multiline=False, password=True)
        self.add_widget(self.confirm_password)

        self.next_button = Button(text='Next')
        self.next_button.bind(on_press=self.next_page)
        self.add_widget(self.next_button)

    def next_page(self, instance):
        if self.checkbox1.active:
            username = self.username.text
            password = self.password.text
            confirm_password = self.confirm_password.text

            if password == confirm_password:
                # Add your signup logic here (e.g., saving to a database)
                print(f"Username: {username}, Password: {password}")
                app.root.current = 'login'
            else:
                print("Passwords do not match")
        else:
            print("Please agree to the terms and conditions")


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
        self.title = 'TechSTARS'
        self.signup_page = SignUpPage()
        self.login_page = LoginPage()
        Window.size = (360, 640)  # Set window size to match Android phone screen (e.g., 720x1280)
        self.root = GridLayout(cols=1)  # Create a GridLayout as the root
        self.root.add_widget(self.signup_page)  # Add the signup page to the root
        self.root.add_widget(self.login_page)  # Add the login page to the root
        return self.root

    def switch_to_login(self):
        self.root.current = 'login'  # Switch to the login page


if __name__ == '__main__':
    MyApp().run()
