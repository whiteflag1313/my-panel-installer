[app]

title = Omid Edge Installer
package.name = omidedgeinstaller
package.domain = org.omid

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy,requests,urllib3,certifi,idna,charset-normalizer

orientation = portrait
android.permissions = INTERNET, ACCESS_NETWORK_STATE

android.archs = arm64-v8a

android.api = 31
android.min_api = 21
android.sdk = 31

# تغییر نسخه NDK به r25c برای سازگاری کامل با کامپایلر Clang
android.ndk = 25c
android.accept_sdk_license = True

[buildozer]
log_level = 2
bin_dir = ./bin
