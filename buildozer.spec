[app]

title = Amir6
package.name = amir6
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,xml

version = 0.1

# اصلاح وابستگی‌ها برای جلوگیری از خطای نسخه‌های سخت‌گیرانه در بیلد
requirements = python3,kivy,openssl,certifi,requests,urllib3,idna,charset-normalizer

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

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
