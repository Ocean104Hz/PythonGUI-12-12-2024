import customtkinter as ctk

class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("โปรแกรมตรวจสอบคำ")
        self.geometry("900x800")
        self.content_frame = ctk.CTkFrame(self, width=880, height=780)
        self.content_frame.pack(padx=10, pady=10)
        self.show_page4()

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_page4(self):
        self.clear_content()

        # กล่องข้อความที่ 1
        label1 = ctk.CTkLabel(self.content_frame, text="กล่องข้อความที่ 1:")
        label1.place(x=10, y=2)
        self.textbox1 = ctk.CTkTextbox(self.content_frame, width=275, height=150, fg_color="#eaecea", font=("TH Sarabun New", 10))
        self.textbox1.place(x=10, y=30)
        self.label_text1_count = ctk.CTkLabel(self.content_frame, text="คำในช่อง 1: 0 คำ")
        self.label_text1_count.place(x=10, y=190)

        # กล่องข้อความที่ 2
        label2 = ctk.CTkLabel(self.content_frame, text="กล่องข้อความที่ 2:")
        label2.place(x=290, y=2)
        self.textbox2 = ctk.CTkTextbox(self.content_frame, width=275, height=150, fg_color="#eaecea", font=("TH Sarabun New", 10))
        self.textbox2.place(x=290, y=30)
        self.label_text2_count = ctk.CTkLabel(self.content_frame, text="คำในช่อง 2: 0 คำ")
        self.label_text2_count.place(x=290, y=190)

        # กล่องข้อความที่ 3
        label3 = ctk.CTkLabel(self.content_frame, text="กล่องข้อความที่ 3:")
        label3.place(x=570, y=2)
        self.textbox3 = ctk.CTkTextbox(self.content_frame, width=275, height=150, fg_color="#eaecea", font=("TH Sarabun New", 10))
        self.textbox3.place(x=570, y=30)
        self.label_text3_count = ctk.CTkLabel(self.content_frame, text="คำที่เหมือนกัน: 0 คำ")
        self.label_text3_count.place(x=570, y=190)

        # กล่องข้อความที่ 4
        label4 = ctk.CTkLabel(self.content_frame, text="กล่องข้อความที่ 4:")
        label4.place(x=10, y=220)
        self.textbox4 = ctk.CTkTextbox(self.content_frame, width=555, height=220, fg_color="#eaecea", font=("TH Sarabun New", 10))
        self.textbox4.place(x=10, y=250)
        self.label_text4_count = ctk.CTkLabel(self.content_frame, text="คำที่ไม่ซ้ำในช่อง 2: 0 คำ")
        self.label_text4_count.place(x=10, y=480)

        # การจัดการเรียลไทม์
        self.textbox1.bind("<KeyRelease>", self.update_results)
        self.textbox2.bind("<KeyRelease>", self.update_results)

    def update_results(self, event=None):
        # ดึงข้อความจาก Textbox1 และ Textbox2
        text1 = self.textbox1.get("1.0", "end").strip()
        text2 = self.textbox2.get("1.0", "end").strip()

        # แยกคำในแต่ละช่อง
        words1 = set(text1.split())
        words2 = set(text2.split())

        # คำที่เหมือนกันใน Textbox1 และ Textbox2
        common_words = words1.intersection(words2)
        self.textbox3.delete("1.0", "end")
        self.textbox3.insert("1.0", "\n".join(common_words))

        # คำที่ไม่ซ้ำใน Textbox2 เมื่อเทียบกับ Textbox3
        unique_words = words2 - common_words
        self.textbox4.delete("1.0", "end")
        self.textbox4.insert("1.0", "\n".join(unique_words))

        # อัปเดตจำนวนคำ
        self.label_text1_count.configure(text=f"คำในช่อง 1: {len(words1)} คำ")
        self.label_text2_count.configure(text=f"คำในช่อง 2: {len(words2)} คำ")
        self.label_text3_count.configure(text=f"คำที่เหมือนกัน: {len(common_words)} คำ")
        self.label_text4_count.configure(text=f"คำที่ไม่ซ้ำในช่อง 2: {len(unique_words)} คำ")

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
