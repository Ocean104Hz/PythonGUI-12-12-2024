import requests
from bs4 import BeautifulSoup

# รับ URL ของโปรไฟล์จากผู้ใช้
profile_url = input("Enter the Facebook profile URL: ")

# ส่งคำขอ HTTP ไปที่ URL ของโปรไฟล์
response = requests.get(profile_url)

# ตรวจสอบสถานะการตอบกลับ
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # ค้นหาแท็กที่มีข้อมูล UID (การค้นหาอาจแตกต่างไปตามโครงสร้างของหน้า)
    try:
        # ตัวอย่างการดึง UID จากหน้าโปรไฟล์ (อาจต้องปรับตามจริง)
        user_id = soup.find('meta', {'property': 'al:ios:url'})['content'].split('/')[-1]
        print(f"UID ของผู้ใช้คือ: {user_id}")
    except Exception as e:
        print(f"ไม่สามารถหาหมายเลข UID ได้: {e}")
else:
    print("ไม่สามารถเข้าถึงหน้าโปรไฟล์ได้")
