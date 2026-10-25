[app]

title = Omid Edge Installer
package.name = omidedgeinstaller
package.domain = org.omid

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,xml

version = 1.0

# پکیج‌های ضروری و سبک
requirements = python3,kivy,requests,urllib3,certifi,idna,charset-normalizer

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE

android.api = 33
android.min_api = 21
android.sdk = 33
android.ndk = 25c
android.ndk_api = 21
android.archs = arm64-v8a
android.accept_sdk_license = True

p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
bin_dir = ./bin
# محدود کردن پردازش موازی برای جلوگیری از کرش کردن کامپایلر در گیت‌هاب
# parallel_jobs مخفی یا تنظیمات ساخت در صورت نیاز
