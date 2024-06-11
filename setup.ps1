python -m venv .venv
.venv/Scripts/activate.ps1

# pip install --index-url=https://pypi.org/simple opencv-python # cv2
# pip install --index-url=https://pypi.org/simple pyzbar
python -m pip install -r ./requirements.txt

# required by the pyzbar package for QR code and barcode detection (open source barcode reader)
# run this in admin mode
choco install zbar

