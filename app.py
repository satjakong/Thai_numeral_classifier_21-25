from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import cv2
import base64
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
MODEL_DIR = 'models'
CLASS_NAMES = ['๒๑', '๒๒', '๒๓', '๒๔', '๒๕']

loaded_models = {}

def get_model(filename):
    if filename not in loaded_models:
        filepath = os.path.join(MODEL_DIR, filename)
        if os.path.exists(filepath):
            loaded_models[filename] = tf.keras.models.load_model(filepath)
        else:
            return None
    return loaded_models[filename]

@app.route('/')
def user_page():
    return render_template('index.html')

@app.route('/admin')
def admin_page():
    return render_template('admin.html')

@app.route('/get_models', methods=['GET'])
def get_models():
    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR)
    files = [f for f in os.listdir(MODEL_DIR) if f.endswith('.h5')]
    return jsonify(files)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    img_data_b64 = data['image']
    selected_model_name = data.get('model') 

    if not selected_model_name:
        return jsonify({'error': 'กรุณาเลือกโมเดลก่อนทำนาย'})

    model = get_model(selected_model_name)
    if model is None:
        return jsonify({'error': f'ไม่พบโมเดล {selected_model_name} ในระบบ'})
    
    img_data = base64.b64decode(img_data_b64.split(',')[1])
    np_arr = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_GRAYSCALE)
    
    img = cv2.resize(img, (28, 28))
    img = img / 255.0
    img = img.reshape(1, 28, 28, 1)
    
    prediction = model.predict(img)
    class_idx = np.argmax(prediction)
    confidence = float(np.max(prediction) * 100)
    
    return jsonify({
        'prediction': CLASS_NAMES[class_idx],
        'confidence': f"{confidence:.2f}%"
    })

@app.route('/upload_model', methods=['POST'])
def upload_model():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
        
    if file and file.filename.endswith('.h5'):
        if not os.path.exists(MODEL_DIR):
            os.makedirs(MODEL_DIR)
            
        filename = secure_filename(file.filename)
        filepath = os.path.join(MODEL_DIR, filename)
        file.save(filepath)
        
        loaded_models[filename] = tf.keras.models.load_model(filepath)
        
        return jsonify({'message': f'อัปโหลดโมเดล "{filename}" สำเร็จ!'})
        
    return jsonify({'message': 'Invalid file type. Must be .h5'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)