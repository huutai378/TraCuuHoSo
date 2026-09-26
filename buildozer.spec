[app]

# (str) Tiêu đề ứng dụng hiển thị trên điện thoại
title = Tra Cuu Ho So

# (str) Tên gói (viết liền không dấu)
package.name = tracuuhoso

# (str) Tên miền gói (định danh ứng dụng)
package.domain = org.tracuu

# (str) Thư mục chứa file main.py
source.dir = .

# (list) Các định dạng file cần đóng gói vào APK
source.include_exts = py,png,jpg,kv,atlas,json,txt,db,sqlite3

# (str) Phiên bản ứng dụng
version = 0.1

# (list) Danh sách các thư viện Python cần dùng (cách nhau bởi dấu phẩy)
# Nếu app có dùng thêm requests, sqlite3,... hãy thêm vào sau: ví dụ python3,kivy,requests
requirements = python3,kivy

# (str) Hướng màn hình (portrait: dọc, landscape: ngang)
orientation = portrait

# (bool) Chế độ toàn màn hình
fullscreen = 0

# (list) Quyền ứng dụng (mở ghi chú nếu cần truy cập mạng hoặc bộ nhớ)
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API hỗ trợ
android.minapi = 21

# (str) Phiên bản Android NDK tối ưu cho Python 3.11
android.ndk = 25b

# (bool) Bỏ qua cập nhật SDK không cần thiết để tiết kiệm thời gian
android.skip_update = False

# (bool) TỰ ĐỘNG CHẤP NHẬN LICENSE CỦA GOOGLE (Rất quan trọng trên CI/CD GitHub)
android.accept_sdk_license = True

# (list) Kiến trúc chip hỗ trợ (chọn 2 kiến trúc phổ biến nhất hiện nay)
android.archs = arm64-v8a, armeabi-v7a

# (bool) Cho phép sao lưu dữ liệu
android.allow_backup = True

[buildozer]

# (int) Mức độ chi tiết của log (2 là đầy đủ nhất để dễ xem lỗi nếu có)
log_level = 2

# (int) Cảnh báo khi chạy quyền root
warn_on_root = 1
