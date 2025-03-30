from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Charlend", "Haziq", "Sarah"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        main_layout = self.root.ids.main
        for name in self.names:
            label = Label(text=name, font_size=30, size_hint_y=0.5, height=50, halign="center", valign="middle")
            main_layout.add_widget(label)
        return self.root

DynamicLabelsApp().run()
