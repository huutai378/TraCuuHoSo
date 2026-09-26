import os
import sqlite3
import unicodedata
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

# Đường dẫn chính xác tới file database.db nằm cùng thư mục
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(CURRENT_DIR, 'database.db')

def remove_accents(input_str):
    if not isinstance(input_str, str):
        input_str = str(input_str) if input_str is not None else ""
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)]).replace('đ', 'd').replace('Đ', 'D').lower().strip()

KV = '''
<MainLayout>:
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: 0.94, 0.95, 0.97, 1
        Rectangle:
            pos: self.pos
            size: self.size

    # 1. Header tiêu đề
    BoxLayout:
        size_hint_y: None
        height: '56dp'
        canvas.before:
            Color:
                rgba: 0.08, 0.25, 0.45, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: "HỆ THỐNG TRA CỨU HỒ SƠ"
            font_size: '18sp'
            bold: True
            color: 1, 1, 1, 1

    # 2. Vùng tìm kiếm
    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: '135dp'
        padding: ['12dp', '10dp', '12dp', '6dp']
        spacing: '10dp'

        # Ô nhập chữ lớn, không bị che mất phông chữ
        TextInput:
            id: txt_search
            hint_text: "Nhập họ tên cần tra cứu (có dấu hoặc không dấu)..."
            font_size: '17sp'
            size_hint_y: None
            height: '52dp'
            multiline: False
            padding: ['12dp', '14dp', '12dp', '10dp']

        # Hàng nút bấm chức năng
        BoxLayout:
            size_hint_y: None
            height: '46dp'
            spacing: '10dp'

            Button:
                text: "TÌM KIẾM"
                font_size: '16sp'
                bold: True
                background_normal: ''
                background_color: 0.12, 0.53, 0.90, 1
                on_release: root.search_record()

            Button:
                text: "XÓA DỮ LIỆU"
                font_size: '16sp'
                bold: True
                background_normal: ''
                background_color: 0.85, 0.25, 0.20, 1
                on_release: root.clear_search()

    # 3. Kết quả tra cứu
    BoxLayout:
        orientation: 'vertical'
        padding: ['12dp', '4dp', '12dp', '6dp']
        
        Label:
            id: lbl_status
            text: "Sẵn sàng tra cứu."
            size_hint_y: None
            height: '24dp'
            font_size: '13sp'
            color: 0.3, 0.3, 0.3, 1
            halign: 'left'
            text_size: self.size

        ScrollView:
            do_scroll_x: False
            Label:
                id: lbl_result
                text: ""
                font_size: '15sp'
                color: 0.1, 0.1, 0.1, 1
                size_hint_y: None
                height: self.texture_size[1] + 20
                text_size: self.width, None
                markup: True

    # 4. Khu vực thống kê theo từng file
    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: '115dp'
        padding: ['12dp', '6dp', '12dp', '8dp']
        canvas.before:
            Color:
                rgba: 0.88, 0.90, 0.94, 1
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: "[b]THỐNG KÊ HỒ SƠ THEO TỪNG FILE[/b]"
            markup: True
            font_size: '13sp'
            size_hint_y: None
            height: '20dp'
            color: 0.1, 0.2, 0.3, 1

        ScrollView:
            do_scroll_x: False
            Label:
                id: lbl_stats
                text: "Đang tải dữ liệu..."
                font_size: '12sp'
                color: 0.2, 0.2, 0.2, 1
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None
                markup: True
'''

class MainLayout(BoxLayout):
    def on_parent(self, *args):
        self.load_statistics()

    def get_db(self):
        return sqlite3.connect(DB_PATH)

    def load_statistics(self):
        if not os.path.exists(DB_PATH):
            self.ids.lbl_stats.text = f"Không tìm thấy file database tại:\n{DB_PATH}"
            return

        try:
            conn = self.get_db()
            cur = conn.cursor()
            cur.execute("SELECT ten_file, so_luong FROM thong_ke ORDER BY ten_file ASC")
            rows = cur.fetchall()
            conn.close()

            if not rows:
                self.ids.lbl_stats.text = "Database chưa có dữ liệu bảng thong_ke."
                return

            total = sum(r[1] for r in rows)
            lines = [f"• [b]{r[0]}[/b]: {r[1]:,} hồ sơ" for r in rows]
            lines.append(f"-> [b]TỔNG CỘNG: {total:,} hồ sơ[/b]")
            self.ids.lbl_stats.text = "\n".join(lines)
        except Exception as e:
            self.ids.lbl_stats.text = f"Lỗi đọc thống kê: {e}"

    def search_record(self):
        raw_keyword = self.ids.txt_search.text.strip()
        if not raw_keyword:
            self.ids.lbl_status.text = "Vui lòng nhập họ tên hoặc từ khóa cần tìm!"
            return

        kw_kd = remove_accents(raw_keyword)
        
        try:
            conn = self.get_db()
            cur = conn.cursor()
            
            # Quét cả cột họ tên lẫn toàn văn thông tin chi tiết (cả có dấu và không dấu)
            query = '''
                SELECT ho_ten, thong_tin_chi_tiet, ten_file 
                FROM ho_so 
                WHERE ho_ten_khong_dau LIKE ? 
                   OR ho_ten LIKE ? 
                   OR thong_tin_khong_dau LIKE ? 
                   OR thong_tin_chi_tiet LIKE ?
                LIMIT 100
            '''
            cur.execute(query, (f"%{kw_kd}%", f"%{raw_keyword}%", f"%{kw_kd}%", f"%{raw_keyword}%"))
            rows = cur.fetchall()
            conn.close()

            count = len(rows)
            self.ids.lbl_status.text = f"Tìm thấy {count} kết quả cho '{raw_keyword}':"

            if count == 0:
                self.ids.lbl_result.text = "[color=#c0392b]Không tìm thấy hồ sơ phù hợp.[/color]"
            else:
                out = []
                for i, r in enumerate(rows, 1):
                    card = (
                        f"[b]{i}. {r[0]}[/b] [size=12sp][i](Nguồn: {r[2]})[/i][/size]\n"
                        f"{r[1]}\n"
                        f"----------------------------------------"
                    )
                    out.append(card)
                self.ids.lbl_result.text = "\n\n".join(out)
        except Exception as e:
            self.ids.lbl_status.text = f"Lỗi truy vấn: {e}"

    def clear_search(self):
        self.ids.txt_search.text = ""
        self.ids.lbl_status.text = "Đã xóa nội dung."
        self.ids.lbl_result.text = ""

class TraCuuApp(App):
    def build(self):
        Builder.load_string(KV)
        return MainLayout()

if __name__ == '__main__':
    TraCuuApp().run()
