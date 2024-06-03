import qrcode
from PIL import Image

# use 'pip install qrcode' to get dependency 

# qr of below data 
data="https://github.com/RajKumarSaroj01/learning-python"

# The box_size parameter controls how many pixels each “box” of the QR code is.
# The border parameter controls how many boxes thick the border should be (the default is 4, which is the minimum according to the specs).

qr=qrcode.QRCode(version=2,box_size=10,border=5)
qr.add_data(data)
qr.make(fit=True)
image=qr.make_image(fill="black",back_color="white")

image.save("test.png")