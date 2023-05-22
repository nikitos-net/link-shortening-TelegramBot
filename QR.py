import qrcode

def generate_qr_code(url):
    img = qrcode.make(url)
    img.save("qr.png")

