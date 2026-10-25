from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from screens.token_screen import TokenScreen
from screens.method_screen import MethodScreen
from screens.progress_screen import ProgressScreen
from screens.result_screen import ResultScreen

class OmidEdgeApp(MDApp):
    def build(self):
        self.title = "Omid Edge"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_hue = "700"

        sm = ScreenManager()
        sm.add_widget(TokenScreen(name="token"))
        sm.add_widget(MethodScreen(name="method"))
        sm.add_widget(ProgressScreen(name="progress"))
        sm.add_widget(ResultScreen(name="result"))
        return sm

if __name__ == "__main__":
    OmidEdgeApp().run()
