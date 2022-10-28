from PIL import Image
from parser import parse_arguments
from config import CODES
import qrcode
import os

# Check whether directory exists, if not, create it
if not os.path.exists(CODES):
    os.mkdir(CODES)

# Get query & filename
link = parse_arguments().query
file = parse_arguments().n

# Configure QR Code.
qr = qrcode.QRCode(
    version=parse_arguments().s,
    box_size=parse_arguments().p,
    border=parse_arguments().b
)

# Adds data to the QR Code
qr.add_data(link)

# Create image
img = qr.make_image(
    fill_color=parse_arguments().x, 
    back_color=parse_arguments().z
    )

# Save image
img.save(f"{CODES}/{file}.png")

# Open image after it's created
show_img = Image.open(f"{CODES}/{file}.png")
show_img.show()
