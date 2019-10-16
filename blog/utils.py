import pyqrcode
from pyqrcode import QRCode
import os
import png
from pyzbar.pyzbar import decode
from PIL import Image
from django.conf import settings

def generate_qr(code_obj):
  # Generate QR code
  code = pyqrcode.create(code_obj.content)

  # Create and save the png file naming "myqr.png"
  code.png("code-" + str(code_obj.pk) + ".png", scale = 8)

  # move the generated file to the images folder
  os.system("mv " + "code-{}.png".format(code_obj.pk) + " mysite/static/images/")

def decode_now(pk):
  img_path = settings.PROJECT_DIR + '/static/images/code-{}.png'.format(pk)
  return decode(Image.open(img_path))
