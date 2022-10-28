## Description

Program that generates a **QR Code** based on the arguments specified. It takes one positional argument which is the _query_/_website_ and a few optional arguments that are described below.

## Prerequisites

- [qrcode](https://pypi.org/project/qrcode/) -> library that generates the QR Code.
- [pillow](https://pypi.org/project/Pillow/) -> used in the generation of the code and for saving and opening the image.

Install both of them with **PIP**:
```
pip install qrcode[pil]
```

## How It Works

Example to run the program without any optional arguments:
```
python generator.py "www.google.com"
```

Optional arguments:

- -h -> shows the help message.
- -n -> name of the file; a random name will be generated else.
- -s -> size of the QR Code.
- -b -> border size of the QR Code.
- -p -> number of pixels each QR Code has.
- -x -> changes the 'fill color'
- -z -> changes the 'back color'
