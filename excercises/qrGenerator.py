import qrcode
from PIL import Image

def qrGenerator():
    data = input("Enter anything to generate QR code : ")
    qr = qrcode.QRCode(version=3, box_size=8, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill="Black", back_color="white")

    image.save("qr_code.png")
    Image.open("qr_code.png")


if __name__ == '__main__':
    qrGenerator()