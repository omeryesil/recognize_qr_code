python3 -m venv .venv
source .venv/bin/activate

# pip install --index-url=https://pypi.org/simple opencv-python # cv2
# pip install --index-url=https://pypi.org/simple pyzbar
# pip install --index-url=https://pypi.org/simple Flask pyzbar opencv-python

python3 -m pip install -i https://pypi.org/simple -r ./requirements.txt


# required by the pyzbar package for QR code and barcode detection
# for MacOS
brew install zbar  # required for 

