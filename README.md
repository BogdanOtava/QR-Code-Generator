## Description

Basic QR Code Generator which is executed from terminal and that saves the image codes locally. It will also automatically open the .png file after it generated it.

##  Prerequisites

`pip install qrcode[pil]` - this will install [qrcode](https://pypi.org/project/qrcode/) & [pillow](https://pypi.org/project/Pillow/).

## How It Works

Takes two argument: the first one is the query, or the website you need the qr code for and the second is the name of the code image.

`python generator.py "www.google.com" "google"`
