import sys
import qrcode

"""
Sample Usage for Command Line Arguments:

sys.argv[0] = filename
sys.argv[1] = mode (HardCoded: hard, UserInput: ui, CommandInput: ci)  # default: ui

# command input
sys.argv[2] = data
sys.argv[3] = output_filename  # if not given use default (output_qr.png)

"""
"""
Testing qrcode module

CLI Usage: qr "Some text" > test.png      # Not Working


Basic Usage:

import qrcode
img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")


SVG Usage:
import qrcode
import qrcode.image.svg

if method == 'basic':
    # Simple factory, just a set of rects.
    factory = qrcode.image.svg.SvgImage
elif method == 'fragment':
    # Fragment factory (also just a set of rects)
    factory = qrcode.image.svg.SvgFragmentImage
else:
    # Combined path factory, fixes white space that may occur when zooming
    factory = qrcode.image.svg.SvgPathImage

img = qrcode.make('Some data here', image_factory=factory)

"""

# Command Line Arguments
# for i, arg in enumerate(sys.argv):
#     print(f"#{i:^3}: {arg}")


def create_qr(input_url: str, output_path="output_qr.png") -> bool:
    qr_img = qrcode.make(input_url)

    try:
        qr_img.save(output_path)
        return True

    except Exception as e:
        print(e[:10])
        return False


if __name__ == "__main__":
    argument_count = len(sys.argv)

    filename = sys.argv[0]
    url = ""
    output_filename = ""

    # If no mode is given
    if argument_count == 1:
        mode = "ui"
    else:
        mode = sys.argv[1]

    match mode:
        case 'hard':
            # Hard Coded
            url = "www.google.com"
            output_filename = "my_qr.png"  # needs file ext
        case 'ui':
            # User Input
            url = input("URL: ")
            output_filename = input("Output Filename (no ext): ") + ".png"
        case 'ci':
            url = sys.argv[2]
            output_filename = sys.argv[3]  # needs file ext
        case "help":
            help_text = f"""
Usage: 
    {filename} [mode]

MODES:
    hard    Hard Coded Input
    ui      User Input
    ci      Command Input, {filename} ci [input_data] [output_path]
    help    Shows Current Screen

Examples: 
    {filename} hard
    {filename} ui
    {filename} ci "www.google.com" my_google_qr.png
"""
            print(help_text)
            quit()

    # Check to make sure output filename doesnt already exist if it does, do you want to overwrite?

    # Create qrcode
    if create_qr(url, output_filename):
        print(f"\n[ Successfully created QR Code ] -> {output_filename}\n")
    else:
        print(f"\n[ Unable to create QR Code ]\n")
