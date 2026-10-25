[app]

title = Omid Edge Installer
package.name = omidedgeinstaller
package.domain = org.omid

# مسیر فایل‌های سورس
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,xml

version = 1.0

# پکیج‌های کامل و استاندارد مورد نیاز برای درخواست‌های کلادفلر و رابط کاربری
requirements = python3,kivy,requests,urllib3,certifi,idna,charset-normalizer,setuptools

orientation = portrait
fullscreen = 0

# دسترسی‌های مورد نیاز اندروید برای اینترنت و شبکه
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE

# تنظیمات پایدار نسخه اندروید، SDK و NDK (مطابق الگوی موفق)
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
