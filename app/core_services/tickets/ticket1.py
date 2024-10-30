from PIL import Image, ImageDraw, ImageFont
import os

if not os.path.exists('../tickets/ticketsave'):
    os.makedirs('../tickets/ticketsave')

FONT_COLOR = "#000000"
FONT_PATH = "arial.ttf"  # Ensure this font is in the current directory or specify the full path

def make_tickets1(name, event, date, org, venue, email, phone, time):
    try:
        image_source = Image.open('../tickets/tckts/tic1.png')
        draw = ImageDraw.Draw(image_source)
        
        # Load the font if available, otherwise default
        try:
            font20 = ImageFont.truetype(FONT_PATH, 20)
            font40 = ImageFont.truetype(FONT_PATH, 40)
            font50 = ImageFont.truetype(FONT_PATH, 50)
            font110 = ImageFont.truetype(FONT_PATH, 110)
        except IOError:
            print("Font file not found, using default font.")
            font20 = ImageFont.load_default()
            font40 = ImageFont.load_default()
            font50 = ImageFont.load_default()
            font110 = ImageFont.load_default()
        
        # Add text to the ticket image at specified coordinates
        draw.text((73, 317), name, fill=FONT_COLOR, font=font20)
        draw.text((1028, 223), event, fill=FONT_COLOR, font=font110)
        draw.text((1172, 465), date, fill=FONT_COLOR, font=font20)
        draw.text((1049, 386), venue, fill=FONT_COLOR, font=font40)
        draw.text((695, 73), org, fill=FONT_COLOR, font=font50)
        draw.text((72, 544), email, fill=FONT_COLOR, font=font20)
        draw.text((74, 427), phone, fill=FONT_COLOR, font=font20)
        draw.text((1173, 494), time, fill=FONT_COLOR, font=font20)
        
        # Save each ticket with a unique filename
        ticket_filename = f'../tickets/ticketsave/ticket_{name.replace(" ", "_")}.png'
        image_source.save(ticket_filename, format='PNG')
        print(f"Ticket created for {name}: {ticket_filename}")
        
    except Exception as e:
        print(f"An error occurred while creating the ticket for {name}: {e}")

