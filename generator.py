from PIL import Image
import qrcode
import os
import pathlib
import argparse

# Create path to working directory & the directory where the codes will be saved.
ROOT = pathlib.Path(__file__).parent
CODES = ROOT.joinpath("qr_codes")

# Check whether directory exists, if not it will create it.
if not os.path.exists(CODES):
    os.mkdir(CODES)

# Create parser so the program can be executed from the terminal.
parser = argparse.ArgumentParser(description="Generates QR Code for the given query.")
parser.add_argument("query", metavar="query", type=str, help="Enter the query you need to generate a QR Code for.")
parser.add_argument("name", metavar="name", type=str, help="Enter a name for the QR Code image.")
args = parser.parse_args()
link = args.query
file = args.name

# Generate QR Code.
img = qrcode.make(link)
img.save(f"{CODES}/{file}.png")

# Open the QR Code image as soon as it is created.
show_img = Image.open(f"{CODES}/{file}.png")
show_img.show()
