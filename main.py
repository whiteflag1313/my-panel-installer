from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import threading
import requests

class PanelInstallerApp(App):
    def build(self):
        self.title = "Omid Edge Panel Installer"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        layout.add_widget(Label(text="ایمیل کلادفلر:", font_size=18))
        self.email_input = TextInput(text='', multiline=False, font_size=16)
        layout.add_widget(self.email_input)

        layout.add_widget(Label(text="توکن / API Key کلادفلر:", font_size=18))
        self.token_input = TextInput(text='', password=True, multiline=False, font_size=16)
        layout.add_widget(self.token_input)

        layout.add_widget(Label(text="آدرس دامنه:", font_size=18))
        self.domain_input = TextInput(text='', multiline=False, font_size=16)
        layout.add_widget(self.domain_input)

        self.status_label = Label(text="وضعیت: آماده", font_size=16)
        layout.add_widget(self.status_label)

        self.btn = Button(text="شروع عملیات نصب و تنظیم", font_size=18, background_color=(0.1, 0.6, 0.3, 1))
        self.btn.bind(on_press=self.start_installation)
        layout.add_widget(self.btn)

        return layout

    def start_installation(self, instance):
        email = self.email_input.text.strip()
        token = self.token_input.text.strip()
        domain = self.domain_input.text.strip()

        if not email or not token or not domain:
            self.status_label.text = "خطا: تمام فیلدها باید پر شوند!"
            return

        self.status_label.text = "در حال اتصال و ارسال درخواست..."
        threading.Thread(target=self.run_process, args=(email, token, domain)).arg = True
        threading.Thread(target=self.run_process, args=(email, token, domain)).start()

    def run_process(self, email, token, domain):
        try:
            headers = {
                "X-Auth-Email": email,
                "X-Auth-Key": token,
                "Content-Type": "application/json"
            }
            # تست اتصال به کلادفلر
            response = requests.get("https://api.cloudflare.com/client/v4/user", headers=headers)
            if response.status_code == 200:
                self.status_label.text = "تایید شد! در حال پیکربندی دامنه..."
                # اینجا منطق اتصال به سرور یا تنظیمات سابدامنه اضافه می‌شود
            else:
                self.status_label.text = "خطا: اطلاعات کلادفلر نامعتبر است."
        except Exception as e:
            self.status_label.text = f"خطا در ارتباط: {str(e)}"

if __name__ == '__main__':
    PanelInstallerApp().run()

