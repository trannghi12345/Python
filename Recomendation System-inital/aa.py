import tkinter as tk

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Đào, Phở và Piano")

# Thêm logo
logo_image = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(window, image=logo_image)
logo_label.pack(side=tk.LEFT)

# Thêm tiêu đề
title_label = tk.Label(window, text="Đào, Phở và Piano")
title_label.pack(side=tk.TOP)

# Thêm khu vực tìm kiếm
search_entry = tk.Entry(window)
search_entry.pack(side=tk.TOP)

# Thêm khu vực gợi ý
suggestions_frame = tk.Frame(window)
suggestions_frame.pack(side=tk.LEFT)

# Thêm khu vực nội dung
content_frame = tk.Frame(window)
content_frame.pack(side=tk.RIGHT)

# Thêm các widget khác
# ...

# Khởi động vòng lặp sự kiện
window.mainloop()
