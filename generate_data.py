import os
import random
from PIL import Image, ImageDraw, ImageFont

# ตั้งค่า
CLASSES = ['๒๑', '๒๒', '๒๓', '๒๔', '๒๕']
DATA_DIR = 'dataset'
FONTS_DIR = 'fonts'
NUM_SAMPLES_PER_CLASS = 800 

if not os.path.exists(FONTS_DIR):
    print(f"ไม่พบโฟลเดอร์ '{FONTS_DIR}' กรุณาสร้างโฟลเดอร์และนำไฟล์ .ttf ไปใส่ไว้ครับ")
    exit()

font_paths = [os.path.join(FONTS_DIR, f) for f in os.listdir(FONTS_DIR) if f.endswith('.ttf')]

if not font_paths:
    print(f"ไม่พบไฟล์ฟอนต์ (.ttf) ในโฟลเดอร์ '{FONTS_DIR}' เลยครับ")
    exit()

print(f"พบฟอนต์ทั้งหมด {len(font_paths)} แบบ")

for c in CLASSES:
    path = os.path.join(DATA_DIR, c) 
    os.makedirs(path, exist_ok=True)

def create_image(text, save_path):
    img = Image.new('L', (28, 28), color=0)
    draw = ImageDraw.Draw(img)
    
    font_size = random.randint(14, 20)
    
    selected_font = random.choice(font_paths)
    
    try:
        font = ImageFont.truetype(selected_font, font_size)
    except Exception as e:
        print(f"มีปัญหาในการโหลดฟอนต์ {selected_font}: {e}")
        return
        
    x = random.randint(0, 5)
    y = random.randint(0, 5)
    
    draw.text((x, y), text, fill=255, font=font)
    
    img.save(save_path)

print("กำลังสร้างชุดข้อมูล...")
for idx, text in enumerate(CLASSES):
    folder = os.path.join(DATA_DIR, text)
    os.makedirs(folder, exist_ok=True)
    
    for i in range(NUM_SAMPLES_PER_CLASS):
        save_path = os.path.join(folder, f"{text}_{i}.png")
        create_image(text, save_path)
        
print(f"สร้างข้อมูลเสร็จสิ้น!{DATA_DIR}")