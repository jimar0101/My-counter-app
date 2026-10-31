from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyCounterApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.count = 0
        self.my_label = Label(text="Clicks: 0", font_size='30sp', color=(0, 1, 1, 1))
        my_button = Button(text="Tap Me!", font_size='24sp', background_color=(0, 0.7, 0.9, 1))
        my_button.bind(on_press=self.increment_counter)
        layout.add_widget(self.my_label)
        layout.add_widget(my_button)
        return layout

    def increment_counter(self, instance):
        self.count += 1
        self.my_label.text = f"Clicks: {self.count}"

if __name__ == '__main__':
    MyCounterApp().run()
  
