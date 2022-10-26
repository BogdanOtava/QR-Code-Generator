from name_randomizer import get_name
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generates QR Code for the given query.", add_help=False)
    parser._action_groups.pop()

    required = parser.add_argument_group("Required arguments")
    optional = parser.add_argument_group("Optional Arguments")

    # Required argument for the query/website to generate QR Code for
    required.add_argument(
        "query", 
        type=str,
        help="enter the query you want to generate a QR Code for"
        )

    # Optional argument for showing the help tab
    optional.add_argument(
        "-h", action="help", 
        default=argparse.SUPPRESS, 
        help="show this help message"
        )

    # Optional argument for giving a clear file name for the QR Code
    optional.add_argument(
        "-n", 
        metavar="file name", 
        type=str, 
        default=get_name(), 
        help="enter a name for the QR Code image"
        )

    # Optional argument for changing the QR Code size
    optional.add_argument(
        "-s", 
        metavar="code size", 
        type=int, 
        default=10, 
        help="size of the QR Code (number between 1 and 40)"
        )

    # Optional argument for changing the border size
    optional.add_argument(
        "-b", 
        metavar="border size", 
        type=int, 
        default=1, 
        help="size of the border of the QR Code (number between 0 and 10)"
        )

    # Optional argument for changing the number of pixels each 'box' of the QR Code has
    optional.add_argument(
        "-p",
        metavar="pixels",
        type=int,
        default=10,
        help="number of pixels each 'box' of the QR Code has"
    )

    return parser.parse_args()
