import cv2 # from opencv-python pip package  # vision and machine learning library 
from pyzbar import pyzbar

def detect_qr_code(image_path):
    image = cv2.imread(image_path)
    
    print('----------------------------------')
    print(f'INFO: Checking QR code in {image_path}')

    try:
      # Convert the image to grayscale
      gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      
      # Detect QR codes in the image
      qr_codes = pyzbar.decode(gray_image)
      
      for qr_code in qr_codes:
          # Extract the bounding box location of the QR code
          (x, y, w, h) = qr_code.rect
          
          # Draw the bounding box on the image
          cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
          
          # Print the QR code data
          qr_code_data = qr_code.data.decode("utf-8")
          print(f"INFO: Detected QR code. Data: {qr_code_data}")
          
          # Display the output image with QR code bounding box
          cv2.imshow("Image", image)

          cv2.waitKey(0)

          cv2.destroyAllWindows()
    
    except Exception:
      print(f"WARN: Image does not have QR code. {image_path}")

# Examples -------------------------
detect_qr_code('test_images/sample_qr_1.png')
detect_qr_code('test_images/sample_qr_2.png')
detect_qr_code('test_images/sample_qr_more.png')

detect_qr_code('test_images/cetaris_ppo_test_qr.png')
detect_qr_code('test_images/sample_qr_product.png')

detect_qr_code('test_images/sample_no_qr_1.png')
