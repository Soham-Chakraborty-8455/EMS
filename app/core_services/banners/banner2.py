from PIL import Image, ImageDraw, ImageFont
import os

# Create directory if it doesn't exist
if not os.path.exists('../banners/bannersave'):
    os.makedirs('../banners/bannersave')

FONT_COLOR = "#000000"
FONT_PATH = "arial.ttf"

# Load template image
temp = Image.open('../banners/ban/ban2.png')
WIDTH, HEIGHT = temp.size


def make_banners2(org, event, venue, date, time):
    # Open the source image
    image_source = Image.open('../banners/ban/ban2.png')
    draw = ImageDraw.Draw(image_source)

    # Load fonts with error handling
    try:
        org_font = ImageFont.truetype(FONT_PATH, 200)
        event_font = ImageFont.truetype(FONT_PATH, 400)
        date_font = ImageFont.truetype(FONT_PATH, 80)
        venue_font = ImageFont.truetype(FONT_PATH, 115)
        time_font = ImageFont.truetype(FONT_PATH, 80)
    except IOError:
        print("Font file not found. Ensure the font file path is correct.")
        return

    # Draw text on image
    draw.text((1809, 845), org, fill=FONT_COLOR, font=org_font)
    draw.text((2385, 1373), event, fill=FONT_COLOR, font=event_font)
    draw.text((2958, 2454), date, fill=FONT_COLOR, font=date_font)
    draw.text((2608, 2244), venue, fill=FONT_COLOR, font=venue_font)
    draw.text((2968, 2574), time, fill=FONT_COLOR, font=time_font)

    # Save the image
    image_source.save('../banners/bannersave/banner.png', format='PNG')


