from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class ThreatUpdatesInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [20, 10]

        self.add_widget(Label(text="Real-time Threat Updates", font_size=24, size_hint=(1, 0.2)))

        # Display real-time threat updates
        self.add_widget(Label(text="New threat detected!", size_hint=(1, 0.1)))
        self.add_widget(Label(text="Malicious link blocked.", size_hint=(1, 0.1)))

        back_button = Button(text="Back", size_hint=(1, 0.1))
        back_button.bind(on_press=self.go_back)
        self.add_widget(back_button)

    def go_back(self, instance):
        # Navigate back to the previous screen
        print("Going back to previous screen...")

class ThreatUpdatesApp(App):
    def build(self):
        return ThreatUpdatesInterface()

if __name__ == "__main__":
    ThreatUpdatesApp().run()
