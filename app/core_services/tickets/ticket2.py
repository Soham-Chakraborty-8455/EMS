from PIL import Image, ImageDraw, ImageFont
import os

# Create the output directory if it doesn't exist
if not os.path.exists('../tickets/ticketsave'):
    os.makedirs('../tickets/ticketsave')

FONT_COLOR = "#000000"
FONT_PATH = "arial.ttf"  # Ensure this font is available in the current directory

def make_tickets2(name, event, date, org, venue, email, phone, time):
    try:
        image_source = Image.open('../tickets/tckts/tic2.png')
        draw = ImageDraw.Draw(image_source)

        # Load fonts with error handling
        try:
            font25 = ImageFont.truetype(FONT_PATH, 25)
            font40 = ImageFont.truetype(FONT_PATH, 40)
            font50 = ImageFont.truetype(FONT_PATH, 50)
            font120 = ImageFont.truetype(FONT_PATH, 120)
        except IOError:
            print("Font file not found, using default font.")
            font25 = ImageFont.load_default()
            font40 = ImageFont.load_default()
            font50 = ImageFont.load_default()
            font120 = ImageFont.load_default()
        
        # Draw text at specified positions
        draw.text((1407, 290), name, fill=FONT_COLOR, font=font25)
        draw.text((306, 216), event, fill=FONT_COLOR, font=font120)
        draw.text((468, 489), date, fill=FONT_COLOR, font=font25)
        draw.text((348, 409), venue, fill=FONT_COLOR, font=font40)
        draw.text((101, 90), org, fill=FONT_COLOR, font=font50)
        draw.text((1369, 434), email, fill=FONT_COLOR, font=font25)
        draw.text((1412, 367), phone, fill=FONT_COLOR, font=font25)
        draw.text((472, 531), time, fill=FONT_COLOR, font=font25)

        # Save each ticket with a unique filename
        ticket_filename = f'../tickets/ticketsave/ticket_{name.replace(" ", "_")}.png'
        image_source.save(ticket_filename, format='PNG')
        print(f"Ticket created for {name}: {ticket_filename}")

    except Exception as e:
        print(f"An error occurred while creating the ticket for {name}: {e}")

if __name__ == "__main__":
    names = ["Soham Chakraborty", "Kaustav Giri", "Pritha Saha", "Ujjaini Ray"]
    event = "Metathon"
    date = "28.12.2022"
    venue = "Taal Kutir Convention"
    org = "Student Developers Student Clubs, Kolkata"
    phone = "9800910906"
    email = "prithasaha19@gmail.com"
    time = "09:30 a.m."

    for name in names:
        make_tickets2(name, event, date, org, venue, email, phone, time)
    print(len(names), "Tickets done.")
