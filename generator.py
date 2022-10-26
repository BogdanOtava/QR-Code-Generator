from PIL import Image
from parser import parse_arguments
import qrcode
import os
import pathlib

# Path to working directory & the directory where the codes will be saved.
ROOT = pathlib.Path(__file__).parent
CODES = ROOT.joinpath("qr_codes")

# Check whether directory exists, if not it will create it.
if not os.path.exists(CODES):
    os.mkdir(CODES)

link = parse_arguments().query
file = parse_arguments().n

# Generate QR Code.
qr = qrcode.QRCode(
    version=parse_arguments().s,
    box_size=parse_arguments().p,
    border=parse_arguments().b
)

qr.add_data(link)

img = qr.make_image(fill_color="black", back_color="white")
img.save(f"{CODES}/{file}.png")

# Open the QR Code image as soon as it is created.
show_img = Image.open(f"{CODES}/{file}.png")
show_img.show()
