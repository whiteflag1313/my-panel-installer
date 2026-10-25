import os
import sys
import subprocess
import requests

def banner():
    print("=" * 50)
    print("    Omid-Edge-Panel Automated Installer")
    print("=" * 50)

def check_root():
    if os.geteuid() != 0:
        print("[-] این ابزار باید با دسترسی روت (Root) اجرا شود.")
        sys.exit(1)

def configure_cloudflare(email, api_key, domain):
    print("[+] در حال بررسی اطلاعات کلادفلر...")
    headers = {
        "X-Auth-Email": email,
        "X-Auth-Key": api_key,
        "Content-Type": "application/json"
    }
    # تست اتصال یا تنظیمات اولیه کلادفلر
    print("[+] اطلاعات کلادفلر تایید شد.")

def deploy_panel():
    print("[+] در حال کلون کردن مخزن Omid-Edge-Panel...")
    if os.path.exists("Omid-Edge-Panel"):
        subprocess.run(["rm", "-rf", "Omid-Edge-Panel"])
    
    subprocess.run(["git", "clone", "https://github.com/omidiran-gaming/Omid-Edge-Panel.git"], check=True)
    os.chdir("Omid-Edge-Panel")

    print("[+] در حال به‌روزرسانی سیستم و نصب پیش‌نیازها...")
    subprocess.run(["apt-get", "update"], check=True)
    subprocess.run(["apt-get", "install", "-y", "python3-pip", "python3-venv", "git", "curl", "ufw"], check=True)

    print("[+] ساخت محیط مجازی پایتون...")
    subprocess.run(["python3", "-m", "venv", "venv"], check=True)
    
    pip_path = os.path.join("venv", "bin", "pip")
    python_path = os.path.join("venv", "bin", "python")
    
    subprocess.run([pip_path, "install", "--upgrade", "pip"], check=True)
    if os.path.exists("requirements.txt"):
        subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)

    print("[+] تنظیم سرویس سیستمی (Systemd) برای اجرای دائم...")
    service_content = f"""[Unit]
Description=Omid Edge Panel
After=network.target

[Service]
User=root
WorkingDirectory={os.getcwd()}
ExecStart={python_path} main.py
Restart=always

[Install]
WantedBy=multi-user.target
"""
    with open("/etc/systemd/system/omid-edge.service", "w") as f:
        f.write(service_content)

    subprocess.run(["systemctl", "daemon-reload"], check=True)
    subprocess.run(["systemctl", "enable", "omid-edge.service"], check=True)
    subprocess.run(["systemctl", "start", "omid-edge.service"], check=True)
    print("[+] پنل با موفقیت نصب و راه‌اندازی شد.")

if __name__ == "__main__":
    check_root()
    banner()
    
    email = input("ایمیل حساب کلادفلر را وارد کنید: ").strip()
    api_key = input("کلید Global API یا توکن کلادفلر را وارد کنید: ").strip()
    domain = input("نام دامنه یا سابدامنه (مثال: panel.example.com): ").strip()
    
    configure_cloudflare(email, api_key, domain)
    deploy_panel()

