from PIL import Image, ImageDraw, ImageFont
import os

# Create output directory if it doesn't exist
if not os.path.exists('../certificates/certificatesave'):
    os.makedirs('../certificates/certificatesave')

FONT_COLOR = "#000000"
FONT_PATH = "arial.ttf"  # Ensure the correct path to your font file

# Load fonts once with error handling
try:
    name_font = ImageFont.truetype(FONT_PATH, 70)
    event_font = ImageFont.truetype(FONT_PATH, 40)
    date_font = ImageFont.truetype(FONT_PATH, 40)
    venue_font = ImageFont.truetype(FONT_PATH, 40)
    desig_font = ImageFont.truetype(FONT_PATH, 30)
    n1_font = ImageFont.truetype(FONT_PATH, 30)
except IOError:
    print("Font file not found. Ensure the font file path is correct.")
    exit()


def make_certificates2(name, event, date, venue, desig, n1, signurl1, logourl1):
    try:
        # Open certificate template
        image_source = Image.open('../certificates/cert/cert2.png')
        draw = ImageDraw.Draw(image_source)

        # Draw text on the image
        draw.text((740, 516), name, fill=FONT_COLOR, font=name_font)
        draw.text((415, 816), event, fill=FONT_COLOR, font=event_font)
        draw.text((1420, 810), date, fill=FONT_COLOR, font=date_font)
        draw.text((769, 812), venue, fill=FONT_COLOR, font=venue_font)
        draw.text((520, 1161), desig, fill=FONT_COLOR, font=desig_font)
        draw.text((488, 1110), n1, fill=FONT_COLOR, font=n1_font)

        # Open and resize logos and signatures
        insert_image1 = Image.open(signurl1)
        insert_image1.thumbnail((450, 75), Image.LANCZOS)  # Resize with aspect ratio
        image_source.paste(insert_image1, (453, 1020), insert_image1 if insert_image1.mode == 'RGBA' else None)

        logo1 = Image.open(logourl1)
        logo1.thumbnail((200, 100), Image.LANCZOS)  # Resize with aspect ratio
        image_source.paste(logo1, (1340, 1030), logo1 if logo1.mode == 'RGBA' else None)

        # Save the image with a unique name
        output_path = f'../certificates/certificatesave/{name.replace(" ", "_")}_certificate.png'
        image_source.save(output_path, format='PNG')
        print(f"Certificate saved for: {name}")

    except IOError as e:
        print(f"Error processing certificate for {name}: {e}")



