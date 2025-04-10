import os
import hashlib
import pyperclip
import qrcode # type: ignore
from PIL import Image # type: ignore

def qrGenerator():

    while True:
        data = input("Enter anything to generate QR code : ")
        if (data == ''):
            print('No input. Please enter information to generate a QR code')
        else:
            break
    

    hash_val = hashlib.md5(data.encode()).hexdigest()[:6]

    qr = qrcode.QRCode(version=3, box_size=8, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill="Black", back_color="white")

    folder = 'QRcodes'
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_name = f"qr_code_{hash_val}.png"
    file_path = os.path.join(folder,file_name)
    image.save(file_path)
    print(f'QR code generated in {file_path}')

    pyperclip.copy(file_path)
    print("File path copied to clipboard.")
    
    #Image.open(file_path).show()

    with open(os.path.join(folder, "qr_log.txt"),"a") as log:
        log.write(f"{file_name}: {data}\n")

    
if __name__ == '__main__':
    while True:
        qrGenerator()
        again = input("Generate another QR code? (y/n): ").lower()
        if again != 'y':
            break
