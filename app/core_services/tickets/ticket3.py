from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the save directory exists
if not os.path.exists('./ticketsave'):
    os.makedirs('./ticketsave')

FONT_COLOR = "#000000"
FONT_PATH = "arial.ttf"  # Specify font path if necessary

def make_tickets3(name, event, date, org, venue, email, phone, time):
    try:
        # Load the ticket template
        image_source = Image.open('./tckts/tic3.png')
        draw = ImageDraw.Draw(image_source)

        # Load fonts, or use default if unavailable
        try:
            font20 = ImageFont.truetype(FONT_PATH, 20)
            font35 = ImageFont.truetype(FONT_PATH, 35)
            font40 = ImageFont.truetype(FONT_PATH, 40)
            font100 = ImageFont.truetype(FONT_PATH, 100)
        except IOError:
            print("Font file not found, using default font.")
            font20 = ImageFont.load_default()
            font35 = ImageFont.load_default()
            font40 = ImageFont.load_default()
            font100 = ImageFont.load_default()

        # Draw text on the image
        draw.text((1598, 220), name, fill=FONT_COLOR, font=font20)
        draw.text((450, 240), event, fill=FONT_COLOR, font=font100)
        draw.text((580, 486), date, fill=FONT_COLOR, font=font20)
        draw.text((480, 430), venue, fill=FONT_COLOR, font=font35)
        draw.text((355, 130), org, fill=FONT_COLOR, font=font40)
        draw.text((1590, 341), email, fill=FONT_COLOR, font=font20)
        draw.text((1600, 280), phone, fill=FONT_COLOR, font=font20)
        draw.text((585, 522), time, fill=FONT_COLOR, font=font20)

        # Save each ticket with a unique filename
        ticket_filename = f'./ticketsave/ticket_{name.replace(" ", "_")}.png'
        image_source.save(ticket_filename, format='PNG')
        print(f"Ticket created for {name}: {ticket_filename}")

    except Exception as e:
        print(f"An error occurred while creating the ticket for {name}: {e}")


