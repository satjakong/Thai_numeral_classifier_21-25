# Thai Numeral Classifier (๒๑-๒๕) 🇹🇭

Member:
1) คชภัค ชีพสัตยากร  1660701325
2) สัจจา กองรัมย์ 1660703156
3) ณัฐนันท์ ปิ่นทอง 1660704154
4) ธิติวุฒิ ทางธนกุล 1660704642
5) เดชาธร ธรรมชัชวาล 1660707215

Features
- User Page (ทำนายผล): รองรับการวาดตัวเลขไทย (๒๑-๒๕) ผ่าน HTML5 Canvas และแสดงผลคำทำนายพร้อมค่าความมั่นใจ (Confidence) แบบ Real-time ผู้ใช้สามารถสลับเวอร์ชันของโมเดลได้
- Admin Dashboard (ระบบจัดการหลังบ้าน): แบ่งการทำงานเป็น 2 ส่วนหลัก
- Model Management: อัปโหลดและอัปเดตโมเดล AI (.h5) เข้าสู่ระบบโดยไม่ต้องรีสตาร์ทเซิร์ฟเวอร์
- Data Collection Tool: เครื่องมือวาดเขียนเพื่อเก็บข้อมูลลายมือใหม่ๆ โดยระบบจะทำการย่อภาพเป็น 28x28 พิกเซล และเซฟจัดหมวดหมู่ลงโฟลเดอร์ dataset ในเครื่องเซิร์ฟเวอร์โดยอัตโนมัติ เพื่อเตรียมพร้อมสำหรับการ Train รอบต่อไป

Tech Stack
- Frontend: HTML, CSS, JavaScript (Canvas API, Fetch API)
- Backend: Python (Flask Framework)
- Machine Learning: TensorFlow / Keras (CNN Architecture)
- Image Processing: OpenCV, Pillow, NumPy

Installation & Setup

1. Clone โปรเจกต์นี้ลงเครื่อง
   
2.ติดตั้ง Library ที่จำเป็น
pip install flask tensorflow opencv-python numpy pillow

3.รันเซิร์ฟเวอร์ Web Application
python app.py

4. เปิด Web Browser และเข้าไปที่ http://127.0.0.1:5000

MLOps Workflow
โปรเจกต์นี้ออกแบบมาให้สามารถพัฒนาความแม่นยำของโมเดลได้อย่างต่อเนื่อง
1. เข้าไปที่หน้า Admin ฝั่งขวามือ เพื่อวาดและบันทึกข้อมูลลายมือใหม่ๆ ข้อมูลจะถูกบันทึกลงโฟลเดอร์ dataset อัตโนมัติ
2. ปิดเซิร์ฟเวอร์เว็บ และรันสคริปต์ python train.py เพื่อนำข้อมูลใหม่ไปสอนโมเดลให้ฉลาดขึ้น
3. นำไฟล์โมเดลตัวใหม่ที่ได้ (ในโฟลเดอร์ models) ไปอัปโหลดผ่านหน้า Admin ฝั่งซ้ายมือ เพื่ออัปเดตระบบให้ผู้ใช้งานทันที

Model Performance
โมเดล Convolutional Neural Network (CNN) ได้รับการฝึกสอนด้วยชุดข้อมูลภาพตัวเลขไทยที่สร้างขึ้นมาใหม่ ขนาด 28x28 พิกเซล จำนวนกว่า 900 รูปต่อคลาส ผสมผสานระหว่างฟอนต์คอมพิวเตอร์แบบดั้งเดิม (Traditional loop fonts) และลายมือเขียนจริง 
Accuracy: 99%
F1-Score: 0.98 - 1.00 ในทุกคลาส (๒๑, ๒๒, ๒๓, ๒๔, ๒๕)

Project Structure
- app.py - โค้ดหลักของ Backend และ API (รวมถึง API สำหรับ Save Dataset)
- train.py - สคริปต์สำหรับสร้างสถาปัตยกรรม CNN และเทรนโมเดล
- generate_data.py - สคริปต์สร้าง Synthetic Dataset จากไฟล์ฟอนต์
- models/ - โฟลเดอร์เก็บไฟล์โมเดลที่ผ่านการเทรน (.h5)
- templates/ - โฟลเดอร์เก็บไฟล์ UI ของหน้าเว็บ (index.html, admin.html)
- dataset/ - ฐานข้อมูลรูปภาพที่จัดหมวดหมู่ตามคลาส 21-25
