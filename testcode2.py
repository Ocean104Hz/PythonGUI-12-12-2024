# import requests
# from bs4 import BeautifulSoup

# # รับ URL ของโปรไฟล์จากผู้ใช้
# profile_url = input("Enter the Facebook profile URL: ")

# # ส่งคำขอ HTTP ไปที่ URL ของโปรไฟล์
# response = requests.get(profile_url)

# # ตรวจสอบสถานะการตอบกลับ
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # ค้นหาแท็กที่มีข้อมูล UID (การค้นหาอาจแตกต่างไปตามโครงสร้างของหน้า)
#     try:
#         # ตัวอย่างการดึง UID จากหน้าโปรไฟล์ (อาจต้องปรับตามจริง)
#         user_id = soup.find('meta', {'property': 'al:ios:url'})['content'].split('/')[-1]
#         print(f"UID ของผู้ใช้คือ: {user_id}")
#     except Exception as e:
#         print(f"ไม่สามารถหาหมายเลข UID ได้: {e}")
# else:
#     print("ไม่สามารถเข้าถึงหน้าโปรไฟล์ได้")




from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_instagram_uid_selenium(profile_link):
    driver = webdriver.Chrome()  # ใช้ ChromeDriver
    driver.get(profile_link)
    time.sleep(5)  # รอให้หน้าโหลดเสร็จ

    try:
        # ค้นหา script ที่เก็บข้อมูล JSON
        script = driver.find_element(By.XPATH, "//script[contains(text(), 'profilePage_')]")
        uid = script.get_attribute('innerHTML').split('profilePage_')[1].split('"')[0]
        return uid
    except Exception as e:
        return f"Error: {e}"
    finally:
        driver.quit()

profile_link = input("กรุณาใส่ลิงก์โปรไฟล์ Instagram: ").strip()
user_id = get_instagram_uid_selenium(profile_link)
print("Instagram UID:", user_id)



