# recognize_qr_code
PoC - recognizing if an image has a QR code or not

## main.py

This is console/desktop app that detects QE codes in an image, and writes the QR code value to console.

## api_app.py

This is a web api, that allows to upload an image, and detects if there is any QR code in the uploaded image.

Sample use to get QR data:

```shell
# Upload image, and return QR value
curl -X POST -F "image=@test_images/sample_qr_1.png" http://localhost:8800/detect/qr
curl -X POST -F "image=@test_images/sample_not_qr_1.png" http://localhost:8800/detect/qr

# Detects image only / does not return QR value
curl -X GET http://localhost:8800/detect/qr?image=http://localhost:8800/detect/qr?image=https://telecomtalk.info/wp-content/uploads/2021/03/qr-code-google-chrome-web-page.jpeg -o image_with_qr.png

curl -X GET http://localhost:8800/detect/qr?image=http://localhost:8800/detect/qr?image=https://cdn.qrstuff.com/resources/images/qr-code-examples/QRStuff_QRCodeExample_2.jpg -o image_with_qr2.png

# http://localhost:8800/detect/qr?image=http://localhost:8800/detect/qr?image=https://cdn.qrstuff.com/resources/images/qr-code-examples/QRStuff_QRCodeExample_9.jpg
# http://localhost:8800/detect/qr?image=http://localhost:8800/detect/qr?image=https://cdn.qrstuff.com/resources/images/qr-code-examples/QRStuff_QRCodeExample_8.jpg


```


