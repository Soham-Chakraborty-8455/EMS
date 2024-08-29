from PIL import Image, ImageDraw, ImageFont
import os

# Create directory if it doesn't exist
if not os.path.exists('certificates/certificatesave'):
    os.makedirs('certificates/certificatesave')

FONT_COLOR = "#000000"
FONT_PATH = "arial.ttf"  # Ensure the correct path to your font file

# Load fonts once with error handling
try:
    name_font = ImageFont.truetype(FONT_PATH, 90)
    gender_font = ImageFont.truetype(FONT_PATH, 35)
    event_font = ImageFont.truetype(FONT_PATH, 45)
    desig_font = ImageFont.truetype(FONT_PATH, 40)
    n1_font = ImageFont.truetype(FONT_PATH, 40)
except IOError:
    print("Font file not found. Ensure the font file path is correct.")
    exit()


def make_certificates1(name, gender, event, desig, n1, url1, log1):
    try:
        image_source = Image.open('certificates/cert/cert1.png')
        draw = ImageDraw.Draw(image_source)

        # Draw text on the image
        draw.text((762, 570), name, fill=FONT_COLOR, font=name_font)
        draw.text((1218, 849), gender, fill=FONT_COLOR, font=ImageFont.truetype("arial.ttf", 25))
        draw.text((974, 785), gender, fill=FONT_COLOR, font=gender_font)
        draw.text((579, 837), event, fill=FONT_COLOR, font=event_font)
        draw.text((520, 1170), desig, fill=FONT_COLOR, font=desig_font)
        draw.text((488, 1099), n1, fill=FONT_COLOR, font=n1_font)

        # Open and resize logos and signatures
        logo1 = Image.open(log1)
        logo1.thumbnail((200, 100), Image.ANTIALIAS)  # Resize with aspect ratio
        image_source.paste(logo1, (1340, 1030), logo1 if logo1.mode == 'RGBA' else None)

        insert_image1 = Image.open(url1)
        insert_image1.thumbnail((450, 75), Image.ANTIALIAS)  # Resize with aspect ratio
        image_source.paste(insert_image1, (453, 994), insert_image1 if insert_image1.mode == 'RGBA' else None)

        # Save the image
        output_path = f'certificates/certificatesave/{name.replace(" ", "_")}_certificate.png'
        image_source.save(output_path, format='PNG')
        print(f"Certificate saved for: {name}")

    except IOError as e:
        print(f"Error processing certificate for {name}: {e}")


# if __name__ == "__main__":
#     names = ["Soham Chakraborty", "Kaustav Giri", "Pritha Saha", "Ujjaini Ray"]
#     event = "Devfest Kolkata 2023"
#     gender = "his/her"
#     desig = "Principal"
#     n1 = "Mitra Basu"
#     url1 = "signs/sig1.png"
#     log1 = "logos/logo1.png"
#
#     for name in names:
#         make_certificates1(name, gender, event, desig, n1, url1, log1)
#
#     print(len(names), "certificates done.")
