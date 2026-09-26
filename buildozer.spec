[app]

# Tên ứng dụng hiển thị trên điện thoại
title = Tra Cuu Ho So

# Tên package (chữ thường, không dấu, không khoảng trắng)
package.name = tracuuhoso

# Domain định danh
package.domain = org.test

# Thư mục chứa file mã nguồn chính (main.py)
source.dir = .

# Các phần mở rộng tập tin cần đóng gói
source.include_exts = py,png,jpg,kv,atlas,json,txt,csv,xlsx

# Phiên bản ứng dụng
version = 0.1

# Danh sách thư viện cần thiết (Đã khóa phiên bản chuẩn để tránh lỗi C-API)
requirements = python3==3.11.5,kivy==2.3.0

# Hướng màn hình (portrait: dọc, landscape: ngang, all: tự xoay)
orientation = portrait

# Chế độ toàn màn hình (0: tắt, 1: bật)
fullscreen = 0


[buildozer]

# Mức độ chi tiết của log (2 là đầy đủ nhất để kiểm tra khi cần)
log_level = 2

# Cảnh báo khi chạy quyền root
warn_on_root = 1


# --- CẤU HÌNH ANDROID ---
[app:android]

# Phiên bản Android API mục tiêu và tối thiểu
android.api = 33
android.minapi = 21

# Phiên bản NDK tương thích ổn định nhất
android.ndk = 25b

# Tự động đồng ý giấy phép Android SDK (bắt buộc để không bị dừng)
android.accept_sdk_license = True

# Kiến trúc CPU hỗ trợ cho các dòng máy Android hiện nay
android.archs = arm64-v8a, armeabi-v7a

# Cho phép ứng dụng truy cập Internet và bộ nhớ (nếu cần)
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
