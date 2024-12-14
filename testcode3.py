import tkinter as tk

# ฟังก์ชันจัดการข้อความจากเฟสบุ๊ก
def process_facebook_data(raw_text):
    lines = raw_text.splitlines()
    processed_lines = [line for line in lines if not line.startswith(("1 สัปดาห์", "ตอบกลับ", "แฟนตัวยง"))]
    return [line.strip() for line in processed_lines if line.strip()]

# ฟังก์ชันประมวลผลจากเฟสบุ๊กและชีต
def process():
    facebook_text = facebook_textbox.get("1.0", tk.END).strip()
    sheet_words = sheet_textbox.get("1.0", tk.END).strip().splitlines()

    if not facebook_text or not sheet_words:
        result_textbox.delete("1.0", tk.END)
        result_textbox.insert(tk.END, "กรุณาใส่ข้อมูลในทุกช่อง")
        return

    # แยกข้อความจาก Facebook
    facebook_messages = process_facebook_data(facebook_text)

    # กรองข้อความ: เก็บข้อความที่มีคำในชีต และไม่มีคำซ้ำในชีต
    filtered_messages = []
    for message in facebook_messages:
        if any(word in sheet_words for word in message.split()):  # มีคำในชีต
            if not any(message == sheet_word for sheet_word in sheet_words):  # ไม่มีคำซ้ำ
                filtered_messages.append(message)

    result_textbox.delete("1.0", tk.END)
    result_textbox.insert(tk.END, "\n".join(filtered_messages))

# ฟังก์ชันประมวลผลจากช่องผลลัพธ์และช่องชีตใหม่
def process_result_with_sheet2():
    result_text = result_textbox.get("1.0", tk.END).strip()
    sheet2_words = sheet2_textbox.get("1.0", tk.END).strip().splitlines()

    if not result_text or not sheet2_words:
        result2_textbox.delete("1.0", tk.END)
        result2_textbox.insert(tk.END, "กรุณาใส่ข้อมูลในช่องผลลัพธ์และชีต 2")
        return

    # แยกข้อความจากผลลัพธ์
    result_messages = result_text.splitlines()

    # กรองข้อความ: ลบข้อความที่ซ้ำกับคำในชีต 2
    filtered_messages = [message for message in result_messages if not any(word in sheet2_words for word in message.split())]

    result2_textbox.delete("1.0", tk.END)
    result2_textbox.insert(tk.END, "\n".join(filtered_messages))

# สร้างหน้าต่าง GUI
root = tk.Tk()
root.title("โปรแกรมกรองข้อความ")

# ช่องกรอกข้อความ Facebook
tk.Label(root, text="ข้อความจาก Facebook:").pack(anchor="w", padx=10, pady=5)
facebook_textbox = tk.Text(root, height=10, width=70)
facebook_textbox.pack(padx=10, pady=5)

# ช่องกรอกคำจากชีต
tk.Label(root, text="คำจากชีต:").pack(anchor="w", padx=10, pady=5)
sheet_textbox = tk.Text(root, height=10, width=70)
sheet_textbox.pack(padx=10, pady=5)

# ปุ่มประมวลผลจาก Facebook และชีต
tk.Button(root, text="ประมวลผลจาก Facebook และชีต", command=process).pack(padx=10, pady=5)

# ช่องแสดงผลลัพธ์
tk.Label(root, text="ผลลัพธ์ (ข้อความที่เหลือ):").pack(anchor="w", padx=10, pady=5)
result_textbox = tk.Text(root, height=10, width=70)
result_textbox.pack(padx=10, pady=5)

# ช่องกรอกคำจากชีต 2
tk.Label(root, text="คำจากชีต 2:").pack(anchor="w", padx=10, pady=5)
sheet2_textbox = tk.Text(root, height=10, width=70)
sheet2_textbox.pack(padx=10, pady=5)

# ปุ่มประมวลผลจากผลลัพธ์และชีต 2
tk.Button(root, text="ประมวลผลจากผลลัพธ์และชีต 2", command=process_result_with_sheet2).pack(padx=10, pady=5)

# ช่องแสดงผลลัพธ์ 2
tk.Label(root, text="ผลลัพธ์ 2 (ข้อความที่เหลือ):").pack(anchor="w", padx=10, pady=5)
result2_textbox = tk.Text(root, height=10, width=70)
result2_textbox.pack(padx=10, pady=5)

# เริ่มต้นโปรแกรม
root.mainloop()
