from PIL import Image,ImageDraw,ImageFont
import os
if not os.path.exists('tickets/ticketsave'):
    os.makedirs('tickets/ticketsave')
FONT_COLOR = "#000000"
temp = Image.open('./app/core_services/tickets/tckts/tic2.png')
WIDTH, HEIGHT = temp.size
def make_tickets2(name,event,date,org,venue,email,phone,time):
    image_source = Image.open('./app/core_services/tickets/tckts/tic2.png')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name)
    draw.text((1407,290), name, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",25))
    event_width, event_height = draw.textsize(event)
    draw.text((306,216), event, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",120))
    date_width, date_height = draw.textsize(date)
    draw.text((468,489), date, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",25))
    venue_width, venue_height = draw.textsize(venue)
    draw.text((348,409), venue, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",40))
    org_width, org_height = draw.textsize(org)
    draw.text((101,90), org, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",50))
    email_width, email_height = draw.textsize(email)
    draw.text((1369,434),email, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",25))
    phone_width, phone_height = draw.textsize(phone)
    draw.text((1412,367),phone, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",25))
    time_width, time_height = draw.textsize(time)
    draw.text((472,531),time, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",25))
    image_source.save('tickets/ticketsave/ticket.png', format='PNG')

if __name__ == "__main__":
    names = ["Soham Chakraborty", "Kaustav Giri", "Pritha Saha","Ujjaini Ray"]
    event = "Metathon"
    date = "28.12.2022"
    venue = "Taal Kutir Convention"
    org = "Student Developers Student Clubs, Kolkata"
    phone = "9800910906"
    email = "prithasaha19@gmail.com"
    time = "09:30 a.m."
    for name in names:
        make_tickets2(name,event,date,org,venue,email,phone,time)
    print(len(names), "Tickets done.")