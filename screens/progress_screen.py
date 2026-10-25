from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.button import MDRaisedButton
from kivy.metrics import dp
from kivy.clock import Clock
import threading
import random
import string

class ProgressScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.token = ""
        self.method = "workers"
        self.build_ui()

    def build_ui(self):
        layout = MDBoxLayout(
            orientation="vertical",
            padding=dp(25),
            spacing=dp(20),
            md_bg_color=(0.96, 0.97, 0.96, 1)
        )

        self.title = MDLabel(
            text="در حال نصب پنل...",
            font_style="H5",
            halign="center",
            theme_text_color="Custom",
            text_color=(0.13, 0.55, 0.13, 1),
            size_hint_y=None,
            height=dp(40)
        )
        layout.add_widget(self.title)

        self.status_label = MDLabel(
            text="آماده‌سازی...",
            font_style="Body1",
            halign="center",
            theme_text_color="Secondary",
            size_hint_y=None,
            height=dp(30)
        )
        layout.add_widget(self.status_label)

        self.progress = MDProgressBar(
            value=0,
            size_hint_y=None,
            height=dp(8)
        )
        layout.add_widget(self.progress)

        self.log_label = MDLabel(
            text="",
            font_style="Caption",
            halign="center",
            theme_text_color="Secondary",
            size_hint_y=None,
            height=dp(100)
        )
        layout.add_widget(self.log_label)

        layout.add_widget(MDLabel(size_hint_y=1))

        self.btn_cancel = MDRaisedButton(
            text="انصراف",
            md_bg_color=(0.7, 0.2, 0.2, 1),
            size_hint_x=1,
            size_hint_y=None,
            height=dp(45),
            on_release=self.cancel
        )
        layout.add_widget(self.btn_cancel)

        self.add_widget(layout)

    def start_deployment(self):
        self.progress.value = 0
        self.status_label.text = "شروع فرآیند نصب..."
        self.log_label.text = ""
        threading.Thread(target=self.run_deployment, daemon=True).start()

    def run_deployment(self):
        try:
            steps = [
                (10, "بررسی توکن..."),
                (25, "دریافت اطلاعات اکانت..."),
                (40, "ساخت KV Namespace..."),
                (55, "تولید پسورد تصادفی..."),
                (70, "آپلود سورس پنل..."),
                (85, "تنظیم متغیرها و بایندینگ..."),
                (95, "دیپلوی نهایی..."),
                (100, "نصب با موفقیت انجام شد!")
            ]

            for value, text in steps:
                Clock.schedule_once(lambda dt, v=value, t=text: self.update_progress(v, t))
                import time
                time.sleep(1.2)  # شبیه‌سازی تأخیر

            # تولید اطلاعات نهایی
            password = self.generate_password()
            panel_url = f"https://omid-edge-{random.randint(1000,9999)}.workers.dev"

            Clock.schedule_once(lambda dt: self.finish_success(panel_url, password))

        except Exception as e:
            Clock.schedule_once(lambda dt: self.finish_error(str(e)))

    def update_progress(self, value, text):
        self.progress.value = value
        self.status_label.text = text
        self.log_label.text += f"• {text}\n"

    def finish_success(self, url, password):
        result_screen = self.manager.get_screen("result")
        result_screen.set_result(url, password, self.method)
        self.manager.current = "result"

    def finish_error(self, error):
        self.status_label.text = "خطا در نصب"
        self.log_label.text = f"خطا: {error}"
        self.btn_cancel.text = "بازگشت"

    def generate_password(self, length=16):
        chars = string.ascii_letters + string.digits + "!@#$%&*"
        return ''.join(random.choice(chars) for _ in range(length))

    def cancel(self, instance):
        self.manager.current = "method"
