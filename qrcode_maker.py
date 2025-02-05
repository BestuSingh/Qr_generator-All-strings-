import qrcode
from PIL import Image


qr=qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=12, border=5)
qr.add_data("https://www.youtube.com/watch?v=4fWVbtVGjSI")
qr.make(fit=True)
img=qr.make_image(fill_color="Red", back_color="White")
img.save("Youtube_official.png")
