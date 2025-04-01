import os
import qrcode
from PIL import Image

def qrGenerator():
    data = input("Enter anything to generate QR code : ")
    qr = qrcode.QRCode(version=3, box_size=8, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill="Black", back_color="white")

    folder = 'QRcodes'
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = os.path.join(folder,'qr_code.png')
    image.save(file_path)
    print(f'QR code generated in {file_path}')

    Image.open(file_path)


if __name__ == '__main__':
    qrGenerator()