from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class MilesToKmApp(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_calculation(self):
        number = float(self.root.ids.input_miles.text)
        result = number * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

MilesToKmApp().run()