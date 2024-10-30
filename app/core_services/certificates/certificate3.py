from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the output directory exists
if not os.path.exists('certificates/certificatesave'):
    os.makedirs('certificates/certificatesave')

FONT_COLOR = "#000000"
FONT_PATH = "arial.ttf"  # Replace with the path to your font file

# Load fonts once
try:
    name_font = ImageFont.truetype(FONT_PATH, 75)
    event_font = ImageFont.truetype(FONT_PATH, 30)
    date_font = ImageFont.truetype(FONT_PATH, 30)
    org_font = ImageFont.truetype(FONT_PATH, 30)
    desig_font = ImageFont.truetype(FONT_PATH, 30)
    n1_font = ImageFont.truetype(FONT_PATH, 30)
except IOError:
    print("Error: Font file not found. Ensure the font file path is correct.")
    exit()


def make_certificates3(name, event, date, org, desig, n1, signurl1, logourl1):
    try:
        # Open the certificate template
        image_source = Image.open('../certificates/app/core_services/certificates/cert/cert3.png')
        draw = ImageDraw.Draw(image_source)

        # Draw text on the certificate
        draw.text((813, 720), name, fill=FONT_COLOR, font=name_font)
        draw.text((696, 913), event, fill=FONT_COLOR, font=event_font)
        draw.text((1560, 912), date, fill=FONT_COLOR, font=date_font)
        draw.text((1153, 910), org, fill=FONT_COLOR, font=org_font)
        draw.text((1132, 862), name, fill=FONT_COLOR, font=org_font)
        draw.text((432, 1220), desig, fill=FONT_COLOR, font=desig_font)
        draw.text((433, 1133), n1, fill=FONT_COLOR, font=n1_font)

        # Open and paste images
        insert_image1 = Image.open(signurl1)
        logo1 = Image.open(logourl1)

        # Dynamic resizing and pasting
        def resize_and_paste(image, size, position):
            image.thumbnail(size, Image.LANCZOS)
            image_source.paste(image, position, image if image.mode == 'RGBA' else None)

        resize_and_paste(insert_image1, (450, 75), (400, 1040))
        resize_and_paste(logo1, (200, 100), (1400, 1040))

        # Save the certificate with a unique name
        output_path = f'../certificates/certificatesave/{name.replace(" ", "_")}_certificate.png'
        image_source.save(output_path, format='PNG')
        print(f"Certificate saved for: {name}")

    except IOError as e:
        print(f"Error processing certificate for {name}: {e}")

