import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

DATA_DIR = 'dataset'
MODEL_DIR = 'models'
CLASS_NAMES = ['๒๑', '๒๒', '๒๓', '๒๔', '๒๕']

def load_data():
    images = []
    labels = []
    for idx, label in enumerate(CLASS_NAMES):
        path = os.path.join(DATA_DIR, label)
        if not os.path.exists(path):
            continue
        for img_name in os.listdir(path):
            img_path = os.path.join(path, img_name)
            
            img_array = np.fromfile(img_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)
            # ------------------------------------

            if img is not None:
                img = cv2.resize(img, (28, 28))
                images.append(img)
                labels.append(idx)
    return np.array(images), np.array(labels)

print("กำลังโหลดข้อมูล...")
X, y = load_data()

if len(X) == 0:
    print("ไม่พบข้อมูล! โปรดใช้ collect_data.html วาดรูปแล้วเซฟใส่โฟลเดอร์ dataset/21, dataset/22 ... ก่อนครับ")
    exit()

X = X / 255.0 
X = X.reshape(-1, 28, 28, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(5, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

print("เริ่มการ Train โมเดล...")
model.fit(X_train, y_train, epochs=50, validation_data=(X_test, y_test))

print("\n--- ผลการประเมินประสิทธิภาพ (Performance Metrics) ---")
y_pred = np.argmax(model.predict(X_test), axis=1)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report (Accuracy, Precision, Recall, F1-Score):")
print(classification_report(y_test, y_pred, target_names=CLASS_NAMES))

if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)
model_path = os.path.join(MODEL_DIR, 'thai_num_model.h5')
model.save(model_path)
print(f"บันทึกโมเดลเรียบร้อยที่: {model_path}")