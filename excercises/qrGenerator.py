import os
import hashlib
import pyperclip
import qrcode # type: ignore
from PIL import Image # type: ignore

def clipboard(x):
    pyperclip.copy(x)
    print("File path copied to clipboard.")

def encode(x):
    hash_val = hashlib.md5(x.encode()).hexdigest()[:6]
    return hash_val

def imageCreation(x):
    qr = qrcode.QRCode(version=3, box_size=8, border=4)
    qr.add_data(x)
    qr.make(fit=True)
    image = qr.make_image(fill="Black", back_color="white")
    return image

def qrGenerator():

    while True:
        data = input("Enter anything to generate QR code : ")
        if (data == ''):
            print('No input. Please enter information to generate a QR code')
        else:
            break

    image = imageCreation(data)

    folder = 'QRcodes'
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_name = f"qr_code_{encode(data)}.png"
    file_path = os.path.join(folder,file_name)
    image.save(file_path)
    print(f'QR code generated in {file_path}')

    clipboard(file_path)
    
    #Image.open(file_path).show()

    with open(os.path.join(folder, "qr_log.txt"),"a") as log:
        log.write(f"{file_name}: {data}\n")

    
if __name__ == '__main__':
    while True:
        qrGenerator()
        again = input("Generate another QR code? (y/n): ").lower()
        if again != 'y':
            break
