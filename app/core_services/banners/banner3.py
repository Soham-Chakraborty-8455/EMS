from PIL import Image, ImageDraw, ImageFont
import os

# Create directory if it doesn't exist
if not os.path.exists('./bannersave'):
    os.makedirs('./bannersave')

FONT_COLOR = "#000000"
FONT_PATH = "arial.ttf"  # Ensure the correct path to your font file

# Load template image
temp = Image.open('./ban/ban3.png')
WIDTH, HEIGHT = temp.size

def make_banners3(org, event, venue, date, time):
    # Open the source image
    image_source = Image.open('./ban/ban3.png')
    draw = ImageDraw.Draw(image_source)

    # Load fonts with error handling
    try:
        org_font = ImageFont.truetype(FONT_PATH, 185)
        event_font = ImageFont.truetype(FONT_PATH, 440)
        date_font = ImageFont.truetype(FONT_PATH, 80)
        venue_font = ImageFont.truetype(FONT_PATH, 135)
        time_font = ImageFont.truetype(FONT_PATH, 80)
    except IOError:
        print("Font file not found. Ensure the font file path is correct.")
        return

    # Draw text on the image
    draw.text((3009, 845), org, fill=FONT_COLOR, font=org_font)
    draw.text((3385, 1373), event, fill=FONT_COLOR, font=event_font)
    draw.text((538, 1688), date, fill=FONT_COLOR, font=date_font)
    draw.text((3638, 2344), venue, fill=FONT_COLOR, font=venue_font)
    draw.text((539, 2020), time, fill=FONT_COLOR, font=time_font)

    # Save the image
    image_source.save('./bannersave/banner.png', format='PNG')

# if __name__ == "__main__":
#     names = ["Soham Chakraborty", "Kaustav Giri", "Pritha Saha", "Ujjaini Ray"]
#     event = "Metathon"
#     date = "28.12.2022"
#     venue = "Taal Kutir Convention"
#     org = "Student Developers Student Clubs"
#     phone = "9800910906"
#     email = "prithasaha19@gmail.com"
#     time = "09:30 a.m."
#     make_banners3(org, event, venue, date, time)
#     print("Banners done.")
