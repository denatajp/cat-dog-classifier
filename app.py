from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

# Konfigurasi
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MODEL_PATH = 'model/cat_dog_classifier.h5'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

# Load model saat aplikasi dimulai
model = tf.keras.models.load_model(MODEL_PATH)
print("Model berhasil dimuat!")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predict_image(img_path):
    # Preprocessing gambar
    img = Image.open(img_path)
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    # Prediksi
    prediction = model.predict(img_array)[0][0]
    label = 'dog' if prediction > 0.5 else 'cat'
    confidence = prediction if label == 'dog' else 1 - prediction
    confidence = float(confidence * 100)
    
    return label, confidence

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Cek jika ada file yang diupload
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            # Simpan file
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)
            
            # Lakukan prediksi
            label, confidence = predict_image(save_path)
            
            return render_template('index.html', 
                                   filename=filename,
                                   label=label,
                                   confidence=confidence)
    
    return render_template('index.html')

# Endpoint baru untuk prediksi AJAX
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
        
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
        
    if file and allowed_file(file.filename):
        # Simpan file sementara
        filename = secure_filename(file.filename)
        temp_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(temp_path)
        
        # Lakukan prediksi
        label, confidence = predict_image(temp_path)
        
        # Hapus file setelah prediksi
        os.remove(temp_path)
        
        print(confidence)

        return jsonify({
            'label': label,
            'confidence': confidence
        })
    
    return jsonify({'error': 'File not allowed'}), 400

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)