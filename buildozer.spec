[app]

# Tên hiển thị của ứng dụng
title = My Application

# Tên gói ứng dụng (viết liền không dấu, chữ thường)
package.name = myapp

# Định danh domain gói
package.domain = org.test

# Thư mục chứa mã nguồn (thường là thư mục hiện tại)
source.dir = .

# Các định dạng file đưa vào bản build
source.include_exts = py,png,jpg,kv,atlas,json,txt

# Phiên bản ứng dụng
version = 0.1

# Danh sách thư viện Python cần thiết (thêm các thư viện khác nếu có dùng)
requirements = python3,kivy

# Hướng màn hình (all, portrait, landscape, sensorLandscape, ...)
orientation = portrait

# Chế độ toàn màn hình (0: hiện thanh thông báo pin/sóng, 1: ẩn)
fullscreen = 0


# --------------------------------------------------
# CẤU HÌNH ANDROID (Đã khóa phiên bản chuẩn để không lỗi)
# --------------------------------------------------
[buildozer]

# Mức độ chi tiết của log (2 là đầy đủ nhất)
log_level = 2

# Cảnh báo nếu chạy dưới quyền root
warn_on_root = 1


# Thiết lập SDK / NDK cho Android
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.2

# Tự động đồng ý điều khoản giấy phép của Google SDK
android.accept_sdk_license = True

# Quyền hạn cơ bản (INTERNET)
android.permissions = INTERNET

# Kiến trúc CPU xuất ra (chạy tốt trên hầu hết máy Android hiện nay)
android.archs = arm64-v8a, armeabi-v7a

# Tự động tải Android SDK nếu chưa có
android.skip_update = False
