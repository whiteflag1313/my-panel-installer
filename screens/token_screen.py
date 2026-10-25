from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.card import MDCard
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
import webbrowser

class TokenScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        layout = MDBoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(15),
            md_bg_color=(0.96, 0.97, 0.96, 1)
        )

        # عنوان
        title = MDLabel(
            text="Omid Edge",
            font_style="H4",
            halign="center",
            theme_text_color="Custom",
            text_color=(0.13, 0.55, 0.13, 1),
            size_hint_y=None,
            height=dp(50)
        )
        layout.add_widget(title)

        subtitle = MDLabel(
            text="نصب آسان پنل روی Cloudflare",
            font_style="Subtitle1",
            halign="center",
            theme_text_color="Secondary",
            size_hint_y=None,
            height=dp(30)
        )
        layout.add_widget(subtitle)

        # کارت توکن
        card = MDCard(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(15),
            size_hint_y=None,
            height=dp(280),
            radius=[15],
            elevation=2
        )

        card.add_widget(MDLabel(
            text="۱. ساخت توکن Cloudflare",
            font_style="H6",
            size_hint_y=None,
            height=dp(30)
        ))

        card.add_widget(MDLabel(
            text="روی دکمه زیر بزن تا صفحه ساخت توکن باز شود.\nبعد از ساخت، توکن را کپی کن و اینجا پیست کن.",
            font_style="Body2",
            theme_text_color="Secondary",
            size_hint_y=None,
            height=dp(60)
        ))

        # دکمه ساخت توکن
        btn_create_token = MDRaisedButton(
            text="ساخت توکن Cloudflare",
            md_bg_color=(0.13, 0.55, 0.13, 1),
            size_hint_x=1,
            on_release=self.open_token_page
        )
        card.add_widget(btn_create_token)

        # فیلد توکن
        self.token_input = MDTextField(
            hint_text="توکن را اینجا پیست کنید",
            mode="rectangle",
            multiline=False,
            size_hint_y=None,
            height=dp(50)
        )
        card.add_widget(self.token_input)

        layout.add_widget(card)

        # دکمه ادامه
        btn_next = MDRaisedButton(
            text="ادامه",
            md_bg_color=(0.13, 0.55, 0.13, 1),
            size_hint_x=1,
            size_hint_y=None,
            height=dp(48),
            on_release=self.go_next
        )
        layout.add_widget(btn_next)

        # فضای خالی پایین
        layout.add_widget(MDLabel(size_hint_y=1))

        self.add_widget(layout)

    def open_token_page(self, instance):
        # لینک آماده ساخت توکن با دسترسی‌های لازم
        url = "https://dash.cloudflare.com/profile/api-tokens?permissionGroupKeys=%5B%7B%22key%22%3A%22workers_scripts%22%2C%22type%22%3A%22edit%22%7D%2C%7B%22key%22%3A%22workers_kv_storage%22%2C%22type%22%3A%22edit%22%7D%2C%7B%22key%22%3A%22account_settings%22%2C%22type%22%3A%22read%22%7D%5D&accountId=%2A&zoneId=all&name=Omid%20Edge%20Token"
        webbrowser.open(url)

    def go_next(self, instance):
        token = self.token_input.text.strip()
        if not token:
            self.token_input.error = True
            self.token_input.helper_text = "لطفاً توکن را وارد کنید"
            self.token_input.helper_text_mode = "on_error"
            return

        # ذخیره توکن برای صفحات بعدی
        self.manager.get_screen("method").token = token
        self.manager.current = "method"
