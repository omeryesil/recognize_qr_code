from flask import Flask, request, jsonify, send_file
import cv2
import numpy as np
from pyzbar import pyzbar
import io
from PIL import Image
import requests

app = Flask(__name__)

def detect_qr_code(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect QR codes in the image
    qr_codes = pyzbar.decode(gray_image)

    qr_data = []
    for qr_code in qr_codes:
        print("---------------------------------")
        print(f"INFO: QR Data: {qr_code}")
        qr_code_data = qr_code.data.decode("utf-8")
        qr_data.append(qr_code_data)

        # Draw rectangle around the QR code
        (x, y, w, h) = qr_code.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return qr_data, image

# ------------------------------------------------------
# Upload an image, detect QR code and values
@app.route('/detect/qr', methods=['POST'])
def detect_qr_post():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    image_np = np.frombuffer(image_file.read(), np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    qr_data, _ = detect_qr_code(image)

    return jsonify({'data': qr_data})

# ------------------------------------------------------
# Detect QR in an image (http link)
@app.route('/detect/qr', methods=['GET'])
def detect_qr_get():
    if 'image' not in request.args:
        return jsonify({'error': 'No image URL provided'}), 400

    image_url = request.args.get('image')

    # Read image from the URL
    resp = requests.get(image_url, stream=True).raw
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    _, image_with_rects = detect_qr_code(image)

    # Convert image to RGB (OpenCV uses BGR by default)
    image_with_rects = cv2.cvtColor(image_with_rects, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image_with_rects)

    # Create an in-memory bytes buffer
    img_io = io.BytesIO()
    pil_image.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8800)
