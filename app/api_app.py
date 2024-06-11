from flask import Flask, request, jsonify
import cv2
import numpy as np
from pyzbar import pyzbar

app = Flask(__name__)

def detect_qr_code(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect QR codes in the image
    qr_codes = pyzbar.decode(gray_image)

    qr_data = []
    for qr_code in qr_codes:
        qr_code_data = qr_code.data.decode("utf-8")
        qr_data.append(qr_code_data)

    return qr_data

@app.route('/detect/qr', methods=['POST'])
def detect_qr():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    image_np = np.frombuffer(image_file.read(), np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    qr_data = detect_qr_code(image)

    return jsonify({'data': qr_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8800)
