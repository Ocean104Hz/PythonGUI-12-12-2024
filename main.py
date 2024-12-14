import customtkinter as ctk
import requests
import pyperclip
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("แอปพลิเคชันพร้อม Sidebar")
        self.geometry("1020x450")
        self.resizable(False, False)

        # สร้าง frame สำหรับ sidebar
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color='#4eb0f5')
        self.sidebar.pack(side="left", fill="y")

        # เพิ่มปุ่มใน sidebar
        self.btn1 = ctk.CTkButton(self.sidebar, text="YouTube", command=self.show_page1)  #fg_color="#FF0000", text_color="#ffffff", hover_color="#AA0114"
        self.btn1.pack(pady=10, padx=10)

        self.btn2 = ctk.CTkButton(self.sidebar, text="โปรแกรมคัดตัว", command=self.show_page2)
        self.btn2.pack(pady=10, padx=10)

        self.btn3 = ctk.CTkButton(self.sidebar, text="โปรแกรมค้นหาไอดี", command=self.show_page3)
        self.btn3.pack(pady=10, padx=10)

        self.btn4 = ctk.CTkButton(self.sidebar, text="โปรแกรมคัดคำผิด", command=self.show_page4)
        self.btn4.pack(pady=10, padx=10)

        self.btn5 = ctk.CTkButton(self.sidebar, text="Coming Soon", command=self.show_page5)
        self.btn5.pack(pady=10, padx=10)

        # สร้าง frame สำหรับเนื้อหาหลัก
        self.content_frame = ctk.CTkFrame(self, fg_color='#ffffff')
        self.content_frame.pack(side="right", fill="both", expand=True)

        # เริ่มต้นด้วยหน้าแรก
        self.show_page1()

    def clear_content(self):
        """ ลบ widget ทุกตัวที่อยู่ใน content_frame """
        for widget in self.content_frame.winfo_children():
            widget.destroy()    

    def show_page1(self):
        self.clear_content()

        self.content_frame.configure(fg_color='#ffffff')

        # Label สำหรับ input_textbox
        input_label = ctk.CTkLabel(self.content_frame, text="input_text:")
        input_label.place(x=10, y=0)

        # Textbox สำหรับรับข้อมูล
        self.input_textbox = ctk.CTkTextbox(self.content_frame, width=400, height=350, fg_color="#eaecea",font=("TH Sarabun New", 12))
        self.input_textbox.place(x=10, y=30)

        # Label สำหรับ output_textbox
        output_label = ctk.CTkLabel(self.content_frame, text="output_text:")
        output_label.place(x=420, y=0)

        # Textbox สำหรับแสดงผล
        self.output_textbox = ctk.CTkTextbox(self.content_frame, width=430, height=350, fg_color="#eaecea",font=("TH Sarabun New", 12))
        self.output_textbox.place(x=420, y=30)

        # ปุ่มอยู่ด้านล่าง
        button1 = ctk.CTkButton(self.content_frame, text="Start", command=self.button_test1, width=200, height=30, fg_color="#5bcf40", hover_color="#45a92d")
        button1.place(x=10, y=400)

        button2 = ctk.CTkButton(self.content_frame, text="Delete", command=self.button_test2, width=200, height=30, fg_color="#ce3432", hover_color="#b42827")
        button2.place(x=320, y=400)

        button3 = ctk.CTkButton(self.content_frame, text="Copy", command=self.button_test3, width=200, height=30, fg_color="#5bcf40", hover_color="#45a92d")
        button3.place(x=650, y=400)


    def button_test1(self):
        # ดึงข้อมูลจาก Textbox สำหรับรับข้อมูล
        text_input = self.input_textbox.get("1.0", "end-1c").strip()

        # สร้างรายการบรรทัดใหม่จากข้อความที่กรอก
        new_lines = text_input.splitlines()
        new_lines = [line.strip() + '|\n' for line in new_lines if line.strip()]  # เพิ่ม | และกำจัดบรรทัดว่าง

        # เพิ่มบรรทัดเริ่มต้นและสิ้นสุด
        new_lines.insert(0, '{\n')  
        new_lines.append('}')

        # แสดงผลใน Textbox สำหรับแสดงผล
        self.output_textbox.delete("1.0", "end")  # ล้างข้อมูลเดิม
        self.output_textbox.insert("1.0", ''.join(new_lines))  # แสดงข้อมูลใหม่

    def button_test2(self):
        self.output_textbox.delete("1.0", "end")
        self.input_textbox.delete("1.0", "end")

    def button_test3(self):
        Copy_Text = self.output_textbox.get("0.1", "end-1c")
        pyperclip.copy(Copy_Text)


    def show_page2(self):
        self.clear_content()

        # Textbox สำหรับรับข้อมูล
        self.input_textbox = ctk.CTkTextbox(self.content_frame, width=400, height=350, fg_color="#eaecea",font=("TH Sarabun New", 18))
        self.input_textbox.place(x=10, y=30)
       
       # ปุ่มอยู่ด้านล่าง
        button1 = ctk.CTkButton(self.content_frame, text="Open", command=self.open_links, width=200, height=30, fg_color="#5bcf40", hover_color="#45a92d")
        button1.place(x=10, y=400)

    def open_links(self):
        # รับข้อมูลจากช่องข้อความ
        input_data = self.input_textbox.get("1.0", ctk.END).strip()
        
        # แปลงข้อมูลเป็นลิสต์โดยใช้ splitlines
        search_texts = input_data.splitlines()
        
        # ลิงก์ Facebook
        link = "https://www.facebook.com/"
        
        # สร้างลิงก์และเปิดในเบราว์เซอร์
        for text in search_texts:
            full_link = link + text.strip()  # รวมลิงก์กับหมายเลข
            webbrowser.open(full_link)
            time.sleep(1)
        

    def show_page3(self):
        self.clear_content()

          # เลย์เอาท์ส่วน URL
        url_label = ctk.CTkLabel(self.content_frame, text="ใส่ลิ้ง-Facebook :")
        url_label.place(x=10, y=10)

        self.url_entry = ctk.CTkEntry(self.content_frame, width=635)
        self.url_entry.place(x=110, y=10)

        url_label = ctk.CTkLabel(self.content_frame, text="ใส่ลิ้ง-Instagram :")
        url_label.place(x=10, y=50)

        self.url_instadram = ctk.CTkEntry(self.content_frame, width=635)
        self.url_instadram.place(x=110, y=50)


        # Fetch button
        self.fetch_button = ctk.CTkButton(self.content_frame, text="ค้นหา", width=100, command=self.fetch_data)
        self.fetch_button.place(x=750, y=10)

        self.fetch_button = ctk.CTkButton(self.content_frame, text="ค้นหา", width=100, command=self.fetch_instagram_data)
        self.fetch_button.place(x=750, y=50)

        # Clear button
        self.clear_button = ctk.CTkButton(self.content_frame, text="ลบข้อความ", width=100, command=self.clear_data)
        self.clear_button.place(x=10, y=410)

        # Textbox สำหรับแสดงข้อมูล UID
        self.output_textbox = ctk.CTkTextbox(self.content_frame, width=840, height=280, fg_color="#eaecea", font=("TH Sarabun New", 12))
        self.output_textbox.place(x=10, y=120)

        # Text
        url_label = ctk.CTkLabel(self.content_frame, text="คำแนะนำในการใช้ : เข้าไปที่หน้าโปรไฟล์ที่ต้องการหาไอดีจากนั้นคัดลอกลิ้งมาใส่")
        url_label.place(x=10, y=90)

    def fetch_data(self):
        # รับ URL ที่ผู้ใช้กรอก
        url = self.url_entry.get().strip()
        if url:
            try:
                # ส่งคำขอ HTTP ไปที่ URL ของโปรไฟล์
                response = requests.get(url)

                # ตรวจสอบสถานะการตอบกลับ
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')

                    # ค้นหาแท็กที่มีข้อมูล UID
                    try:
                        # ดึง UID จาก meta tag (ต้องปรับให้ตรงตามโครงสร้างของหน้า Facebook จริง)
                        user_id = soup.find('meta', {'property': 'al:ios:url'})['content'].split('/')[-1]
                        user_name = soup.title.string.strip()  # ดึงชื่อจาก title ของหน้า
                        
                        # แสดงผลใน Textbox
                        self.output_textbox.insert("end", f"ชื่อผู้ใช้: {user_name}\nUID ของผู้ใช้คือ: {user_id}\n\n")
                    except Exception as e:
                        self.output_textbox.insert("end", f"ไม่สามารถหาหมายเลข UID ได้: {e}\n")
                else:
                    self.output_textbox.insert("end", "ไม่สามารถเข้าถึงหน้าโปรไฟล์ได้\n")
            except Exception as e:
                self.output_textbox.insert("end", f"เกิดข้อผิดพลาด: {e}\n")

    def clear_data(self):
        self.output_textbox.delete("1.0", "end")

    def fetch_instagram_data(self):
        # รับ URL ที่ผู้ใช้กรอก
        instagram_url = self.url_instadram.get().strip()
        if not instagram_url:
            self.output_textbox.insert("end", "กรุณาใส่ลิงก์ Instagram\n")
            return

        try:
            # ใช้ Selenium เพื่อดึง UID
            self.output_textbox.insert("end", "กำลังโหลดข้อมูล...\n")
            driver = webdriver.Chrome()  # กำหนด WebDriver (ต้องมี chromedriver ใน PATH)
            driver.get(instagram_url)
            time.sleep(3)  # รอให้หน้าเว็บโหลด

            try:
                # ดึง UID จาก script ที่เก็บ JSON
                script = driver.find_element(By.XPATH, "//script[contains(text(), 'profilePage_')]")
                uid = script.get_attribute('innerHTML').split('profilePage_')[1].split('"')[0]

                # ดึงชื่อโปรไฟล์จาก title ของหน้า
                title = driver.title  # ดึงค่า Title ของหน้า
                profile_name = title.split("•")[0].strip()  # ชื่อโปรไฟล์มักอยู่ก่อน •

                # แสดง UID ใน Textbox
                self.output_textbox.insert("end", f"Instagram UID: {uid}\n")
                self.output_textbox.insert("end", f"ชื่อโปรไฟล์: {profile_name}\n\n")
            except Exception as e:
                self.output_textbox.insert("end", f"ไม่สามารถดึง UID ได้: {e}\n")
            finally:
                driver.quit()

        except Exception as e:
            self.output_textbox.insert("end", f"เกิดข้อผิดพลาด: {e}\n")







    def show_page4(self):
        self.clear_content()
        label = ctk.CTkLabel(self.content_frame, text="Coming Soon IG-Uid")
        label.place(x=400, y=200)


    def show_page5(self):
        self.clear_content()
        label = ctk.CTkLabel(self.content_frame, text="Coming Soon")
        label.place(x=400, y=200)


if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    app = MyApp()
    app.mainloop()
