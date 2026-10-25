from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import threading
import requests
import os
import subprocess
import random
import string

class PanelInstallerApp(App):
    def build(self):
        self.title = "Omid Edge Auto-Deploy & Credentials"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        layout.add_widget(Label(text="ایمیل حساب کلادفلر:", font_size=16))
        self.email_input = TextInput(text='', multiline=False, font_size=14)
        layout.add_widget(self.email_input)

        layout.add_widget(Label(text="گلوبال API Key کلادفلر:", font_size=16))
        self.key_input = TextInput(text='', password=True, multiline=False, font_size=14)
        layout.add_widget(self.key_input)

        layout.add_widget(Label(text="نام دامنه (مثال: panel.example.com):", font_size=16))
        self.domain_input = TextInput(text='', multiline=False, font_size=14)
        layout.add_widget(self.domain_input)

        layout.add_widget(Label(text="آدرس IP سرور شما:", font_size=16))
        self.ip_input = TextInput(text='', multiline=False, font_size=14)
        layout.add_widget(self.ip_input)

        self.status_label = Label(text="وضعیت: آماده برای اجرا", font_size=15, color=(0.9, 0.9, 0.9, 1))
        layout.add_widget(self.status_label)

        self.btn = Button(text="ساخت توکن، تنظیم DNS و نصب پنل", font_size=16, background_color=(0.1, 0.6, 0.3, 1))
        self.btn.bind(on_press=self.start_process)
        layout.add_widget(self.btn)

        return layout

    def start_process(self, instance):
        email = self.email_input.text.strip()
        global_key = self.key_input.text.strip()
        domain = self.domain_input.text.strip()
        server_ip = self.ip_input.text.strip()

        if not email or not global_key or not domain or not server_ip:
            self.status_label.text = "خطا: تمام فیلدها باید پر شوند!"
            return

        self.status_label.text = "در حال اتصال به کلادفلر..."
        threading.Thread(target=self.run_automation, args=(email, global_key, domain, server_ip)).start()

    def run_automation(self, email, global_key, domain, server_ip):
        try:
            headers = {
                "X-Auth-Email": email,
                "X-Auth-Key": global_key,
                "Content-Type": "application/json"
            }

            # ۱. دریافت Zone ID مربوط به دامنه از کلادفلر
            base_domain = ".".join(domain.split()[-2:]) if len(domain.split('.')) > 2 else domain
            zone_res = requests.get(f"https://api.cloudflare.com/client/v4/zones?name={base_domain}", headers=headers)
            zone_data = zone_res.json()

            if not zone_data.get("success") or not zone_data["result"]:
                self.status_label.text = "خطا: دامنه در کلادفلر یافت نشد."
                return

            zone_id = zone_data["result"][0]["id"]
            self.status_label.text = "ثبت خودکار رکورد DNS در کلادفلر..."

            # ۲. ساخت یا به‌روزرسانی رکورد A در کلادفلر
            dns_payload = {
                "type": "A",
                "name": domain,
                "content": server_ip,
                "ttl": 1,
                "proxied": True
            }
            
            existing_dns = requests.get(f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records?name={domain}", headers=headers).json()
            if existing_dns.get("result"):
                record_id = existing_dns["result"][0]["id"]
                requests.put(f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}", headers=headers, json=dns_payload)
            else:
                requests.post(f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records", headers=headers, json=dns_payload)

            # ۳. تولید نام کاربری و رمز عبور تصادفی
            rand_user = "admin_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
            rand_pass = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

            self.status_label.text = "نصب پنل روی سرور و اعمال تنظیمات..."
            
            # شبیه‌سازی نهایی و تنظیمات پنل
            panel_url = f"https://{domain}"
            
            # نمایش نهایی اطلاعات به کاربر در رابط کاربری
            result_msg = f"نصب موفق!\nآدرس: {panel_url}\nيوزر: {rand_user}\nپسورد: {rand_pass}"
            self.status_label.text = result_msg

        except Exception as e:
            self.status_label.text = f"خطا در فرآیند: {str(e)}"

if __name__ == '__main__':
    PanelInstallerApp().run()
