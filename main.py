from kivy.lang import Builder
from kivymd.app import MDApp
from safespace_layout import SafeSpaceLayout, FilterDialogContent
from kivymd.uix.dialog import MDDialog

class SafeSpaceApp(MDApp):
    safe_space_layout = SafeSpaceLayout()

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "200"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('safespace.kv')

    def show_filter_dialog(self):
        content = FilterDialogContent()
        dialog = MDDialog(title="Filters", type="custom", content_cls=content, size_hint=(.9, .9))
        dialog.open()

if __name__ == "__main__":
    SafeSpaceApp().run()
