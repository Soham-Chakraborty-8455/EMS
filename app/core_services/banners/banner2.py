from PIL import Image,ImageDraw,ImageFont
import os
if not os.path.exists('banners/bannersave'):
    os.makedirs('banners/bannersave')
FONT_COLOR = "#000000"
temp = Image.open('banners/ban/ban2.png')
WIDTH, HEIGHT = temp.size
def make_banners2(org,event,venue,date,time):
    image_source = Image.open('banners/ban/ban2.png')
    draw = ImageDraw.Draw(image_source)
    org_width, org_height = draw.textsize(org)
    draw.text((1809,845), org, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",200))
    event_width, event_height = draw.textsize(event)
    draw.text((2385,1373), event, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",400))
    date_width, date_height = draw.textsize(date)
    draw.text((2958,2454), date, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",80))
    venue_width, venue_height = draw.textsize(venue)
    draw.text((2608,2244),venue, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",115))
    time_width, time_height = draw.textsize(time)
    draw.text((2968,2574),time, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",80))
    image_source.save('banners/bannersave/banner.png', format='PNG')

if __name__ == "__main__":
    names = ["Soham Chakraborty", "Kaustav Giri", "Pritha Saha","Ujjaini Ray"]
    event = "Metathon"
    date = "28.12.2022"
    venue = "Taal Kutir Convention"
    org = "Student Developers Student Clubs"
    phone = "9800910906"
    email = "prithasaha19@gmail.com"
    time = "09:30 a.m."
    make_banners2(org,event,venue,date,time)
    print("Banners done.")
