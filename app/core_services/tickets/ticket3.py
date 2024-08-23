from PIL import Image,ImageDraw,ImageFont
import os
if not os.path.exists('tickets/ticketsave'):
    os.makedirs('tickets/ticketsave')
FONT_COLOR = "#000000"
temp = Image.open('tickets/tckts/tic3.png')
WIDTH, HEIGHT = temp.size
def make_tickets3(name,event,date,org,venue,email,phone,time):
    image_source = Image.open('tickets/tckts/tic3.png')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name)
    draw.text((1598,220), name, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",20))
    event_width, event_height = draw.textsize(event)
    draw.text((450,240), event, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",100))
    date_width, date_height = draw.textsize(date)
    draw.text((580,486), date, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",20))
    venue_width, venue_height = draw.textsize(venue)
    draw.text((480,430), venue, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",35))
    org_width, org_height = draw.textsize(org)
    draw.text((355,130), org, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",40))
    email_width, email_height = draw.textsize(email)
    draw.text((1590,341),email, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",20))
    phone_width, phone_height = draw.textsize(phone)
    draw.text((1600,280),phone, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",20))
    time_width, time_height = draw.textsize(time)
    draw.text((585,522),time, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",20))
    image_source.save('tickets/ticketsave/ticket.png', format='PNG')

if __name__ == "__main__":
    names = ["Soham Chakraborty", "Kaustav Giri", "Pritha Saha","Ujjaini Ray"]
    event = "Metathon"
    date = "29.12.2022"
    venue = "Taal Kutir Convention"
    org = "Student Developers Student Clubs"
    phone = "9800910906"
    email = "prithasaha19@gmail.com"
    time = "09:30 a.m."
    for name in names:
        make_tickets3(name,event,date,org,venue,email,phone,time)
    print(len(names),"Tickets done.")