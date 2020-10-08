from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    status_text = StringProperty

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Mitchell", "Lucas", "Bill", "David", "Desmond", "Jack"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicLabelsApp().run()
