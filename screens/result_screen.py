from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.card import MDCard
from kivy.metrics import dp
from kivy.core.clipboard import Clipboard
from kivymd.toast import toast

class ResultScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.panel_url = ""
        self.password = ""
        self.method = ""
        self.build_ui()

    def build_ui(self):
        layout = MDBoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(15),
            md_bg_color=(0.96, 0.97, 0.96, 1)
        )

        title = MDLabel(
            text="نصب با موفقیت انجام شد!",
            font_style="H5",
            halign="center",
            theme_text_color="Custom",
            text_color=(0.13, 0.55, 0.13, 1),
            size_hint_y=None,
            height=dp(45)
        )
        layout.add_widget(title)

        # کارت اطلاعات
        card = MDCard(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(12),
            size_hint_y=None,
            height=dp(260),
            radius=[15],
            elevation=2
        )

        card.add_widget(MDLabel(
            text="اطلاعات پنل شما:",
            font_style="H6",
            size_hint_y=None,
            height=dp(30)
        ))

        self.url_label = MDLabel(
            text="آدرس پنل:\n-",
            font_style="Body1",
            size_hint_y=None,
            height=dp(60)
        )
        card.add_widget(self.url_label)

        self.pass_label = MDLabel(
            text="رمز عبور:\n-",
            font_style="Body1",
            size_hint_y=None,
            height=dp(50)
        )
        card.add_widget(self.pass_label)

        self.method_label = MDLabel(
            text="روش نصب: -",
            font_style="Caption",
            theme_text_color="Secondary",
            size_hint_y=None,
            height=dp(25)
        )
        card.add_widget(self.method_label)

        layout.add_widget(card)

        # دکمه‌ها
        btn_copy_url = MDRaisedButton(
            text="کپی آدرس پنل",
            md_bg_color=(0.13, 0.55, 0.13, 1),
            size_hint_x=1,
            size_hint_y=None,
            height=dp(45),
            on_release=self.copy_url
        )
        layout.add_widget(btn_copy_url)

        btn_copy_pass = MDRaisedButton(
            text="کپی رمز عبور",
            md_bg_color=(0.2, 0.6, 0.3, 1),
            size_hint_x=1,
            size_hint_y=None,
            height=dp(45),
            on_release=self.copy_password
        )
        layout.add_widget(btn_copy_pass)

        btn_new = MDFlatButton(
            text="نصب پنل جدید",
            size_hint_x=1,
            on_release=self.new_install
        )
        layout.add_widget(btn_new)

        layout.add_widget(MDLabel(size_hint_y=1))
        self.add_widget(layout)

    def set_result(self, url, password, method):
        self.panel_url = url
        self.password = password
        self.method = method

        self.url_label.text = f"آدرس پنل:\n{url}"
        self.pass_label.text = f"رمز عبور:\n{password}"
        self.method_label.text = f"روش نصب: {method.upper()}"

    def copy_url(self, instance):
        Clipboard.copy(self.panel_url)
        toast("آدرس پنل کپی شد")

    def copy_password(self, instance):
        Clipboard.copy(self.password)
        toast("رمز عبور کپی شد")

    def new_install(self, instance):
        self.manager.current = "token"
