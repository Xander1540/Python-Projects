import qrcode as qr
from PIL import Image
q=qr.QRCode(version=1, 
            error_correction=qr.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,)

q.add_data("https://youtu.be/NaQ_4ZvCbOE")
q.make(fit=True)
img= q.make_image(fill_color='darkblue', back_color='steelblue')
img.save("x.png")