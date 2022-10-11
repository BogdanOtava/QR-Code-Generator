from PIL import Image
import qrcode
import os
import pathlib
import argparse

ROOT = pathlib.Path(__file__).parent
CODES = ROOT.joinpath("qr_codes")

if not os.path.exists(CODES):
    os.mkdir(CODES)

parser = argparse.ArgumentParser(description="Generates QR Code for the given query.")
parser.add_argument("query", metavar="query", type=str, help="Enter the query you need to generate a QR Code for.")
parser.add_argument("name", metavar="name", type=str, help="Enter a name for the QR Code image.")
args = parser.parse_args()
link = args.query
file = args.name

img = qrcode.make(link)
img.save(f"{CODES}/{file}.png")

show_img = Image.open(f"{CODES}/{file}.png")
show_img.show()
