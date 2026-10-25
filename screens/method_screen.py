from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.metrics import dp
from kivy.uix.behaviors import ButtonBehavior

class SelectableCard(ButtonBehavior, MDCard):
    def __init__(self, title, description, method, **kwargs):
        super().__init__(**kwargs)
        self.method = method
        self.orientation = "vertical"
        self.padding = dp(15)
        self.spacing = dp(8)
        self.size_hint_y = None
        self.height = dp(110)
        self.radius = [12]
        self.elevation = 1
        self.md_bg_color = (1, 1, 1, 1)

        self.title_label = MDLabel(
            text=title,
            font_style="H6",
            size_hint_y=None,
            height=dp(30)
        )
        self.add_widget(self.title_label)

        self.desc_label = MDLabel(
            text=description,
            font_style="Body2",
            theme_text_color="Secondary",
            size_hint_y=None,
            height=dp(50)
        )
        self.add_widget(self.desc_label)

class MethodScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.token = ""
        self.selected_method = "workers"
        self.build_ui()

    def build_ui(self):
        layout = MDBoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(15),
            md_bg_color=(0.96, 0.97, 0.96, 1)
        )

        title = MDLabel(
            text="انتخاب روش نصب",
            font_style="H5",
            halign="center",
            theme_text_color="Custom",
            text_color=(0.13, 0.55, 0.13, 1),
            size_hint_y=None,
            height=dp(40)
        )
        layout.add_widget(title)

        # کارت Workers
        self.card_workers = SelectableCard(
            title="Workers (پیشنهادی)",
            description="سریع‌تر و ساده‌تر • مناسب استفاده شخصی",
            method="workers"
        )
        self.card_workers.bind(on_release=lambda x: self.select_method("workers"))
        layout.add_widget(self.card_workers)

        # کارت Pages
        self.card_pages = SelectableCard(
            title="Pages",
            description="پایدارتر برای استفاده طولانی • مناسب اشتراک‌گذاری",
            method="pages"
        )
        self.card_pages.bind(on_release=lambda x: self.select_method("pages"))
        layout.add_widget(self.card_pages)

        # دکمه ادامه
        btn_next = MDRaisedButton(
            text="شروع نصب",
            md_bg_color=(0.13, 0.55, 0.13, 1),
            size_hint_x=1,
            size_hint_y=None,
            height=dp(48),
            on_release=self.start_install
        )
        layout.add_widget(btn_next)

        # دکمه برگشت
        btn_back = MDFlatButton(
            text="بازگشت",
            size_hint_x=1,
            on_release=lambda x: setattr(self.manager, "current", "token")
        )
        layout.add_widget(btn_back)

        layout.add_widget(MDLabel(size_hint_y=1))
        self.add_widget(layout)

        # پیش‌فرض Workers انتخاب شده
        self.select_method("workers")

    def select_method(self, method):
        self.selected_method = method

        if method == "workers":
            self.card_workers.md_bg_color = (0.85, 0.95, 0.85, 1)
            self.card_pages.md_bg_color = (1, 1, 1, 1)
        else:
            self.card_pages.md_bg_color = (0.85, 0.95, 0.85, 1)
            self.card_workers.md_bg_color = (1, 1, 1, 1)

    def start_install(self, instance):
        progress_screen = self.manager.get_screen("progress")
        progress_screen.token = self.token
        progress_screen.method = self.selected_method
        self.manager.current = "progress"
        progress_screen.start_deployment()
