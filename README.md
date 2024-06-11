# recognize_qr_code
PoC - recognizing if an image has a QR code or not

## main.py

This is console/desktop app that detects QE codes in an image, and writes the QR code value to console.

## api_app.py

This is a web api, that allows to upload an image, and detects if there is any QR code in the uploaded image.

Sample use:

```shell
curl -X POST -F "image=@test_images/sample_qr_1.png" http://localhost:8800/detect/qr
curl -X POST -F "image=@test_images/sample_not_qr_1.png" http://localhost:8800/detect/qr
```
