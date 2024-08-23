from PIL import Image,ImageDraw,ImageFont
import os
if not os.path.exists('banners/bannersave'):
    os.makedirs('banners/bannersave')
FONT_COLOR = "#000000"
temp = Image.open('banners/ban/ban3.png')
WIDTH, HEIGHT = temp.size
def make_banners3(org,event,venue,date,time):
    image_source = Image.open('banners/ban/ban3.png')
    draw = ImageDraw.Draw(image_source)
    org_width, org_height = draw.textsize(org)
    draw.text((3009,845), org, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",185))
    event_width, event_height = draw.textsize(event)
    draw.text((3385,1373), event, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",440))
    date_width, date_height = draw.textsize(date)
    draw.text((538,1688), date, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",80))
    venue_width, venue_height = draw.textsize(venue)
    draw.text((3638,2344),venue, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",135))
    time_width, time_height = draw.textsize(time)
    draw.text((539,2020),time, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",80))
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
    make_banners3(org,event,venue,date,time)
    print("Banners done.")
