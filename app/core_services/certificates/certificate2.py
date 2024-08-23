from PIL import Image,ImageDraw,ImageFont
import os
if not os.path.exists('certificates/certificatesave'):
    os.makedirs('certificates/certificatesave')
#FONT_FILE = ImageFont.truetype("arial.ttf", 50)
#FONT_FILE_o = ImageFont.truetype("arial.ttf", 30)
FONT_COLOR = "#000000"
t1 = Image.open('certificates/cert/cert2.png')
WIDTH, HEIGHT = t1.size
def make_certificates2(name,event,date,venue,desig,n1,url1,log1):
    image_source = Image.open('certificates/cert/cert2.png')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name)
    draw.text((740,516), name, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",70))
    event_width, event_height = draw.textsize(event)
    draw.text((415,816), event, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",40))
    date_width, date_height = draw.textsize(date)
    draw.text((1420,810), date, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",40))
    venue_width, venue_height = draw.textsize(venue)
    draw.text((769,812), venue, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",40))

    desig_width, desig_height = draw.textsize(desig)
    draw.text((520,1161), desig, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",30))
    #design_width, design_height = draw.textsize(design)
    #draw.text((1302,1161), design, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",30))
    n1_width, n1_height = draw.textsize(n1)
    draw.text((488,1110), n1, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",30))
    #n2_width, n2_height = draw.textsize(n2)
    #draw.text((1301,1110), n2, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",30))
    #image_source.save("./out/" + name +".png")
    #print('Saving Certificate of:', name)

    insert_image1 = Image.open(url1)
    #insert_image2 = Image.open(url2)

    width1, height1 = insert_image1.size
    #width2, height2 = insert_image2.size
    x = width1/height1
    #y = width2/height2
    if x <= 3:
        insert_image1 = insert_image1.resize((250,75))
        image_source.paste(insert_image1, (453,1020))
    else :
        insert_image1 = insert_image1.resize((450,75))
        image_source.paste(insert_image1, (453,1020))

    #if y <= 3 :
        #insert_image2 = insert_image2.resize((250,75))
        #image_source.paste(insert_image2, (1269,1020))
    #else :
        #insert_image2 = insert_image2.resize((450,75))
        #image_source.paste(insert_image2, (1269,1020))

    logo1 = Image.open(log1)
    #logo2 = Image.open(log2)

    width3, height3 = logo1.size
    #width4, height4 = logo2.size
    a = width3/height3
    #b = width4/height4
    if a <= 3:
        logo1 = logo1.resize((100,100))
        image_source.paste(logo1, (1340,1030))
    else :
        logo1 = logo1.resize((200,100))
        image_source.paste(logo1, (1340,1030))

    #if b <= 3 :
        #logo2 = logo2.resize((100,100))
        #image_source.paste(logo2, (1045,63))
    #else :
        #logo2 = logo2.resize((200,100))
        #image_source.paste(logo2, (1045,63))

    image_source.save('certificates/certificatesave/certificate.png', format='PNG')

if __name__ == "__main__":
    names = ["Soham Chakraborty", "Kaustav Giri", "Pritha Saha","Ujjaini Ray"]
    event = "Devfest 2k23"
    date = "28.12.2022"
    venue = "Taal Kutir Convention"

    desig = "Principal"
    #design = "Student Head"
    n1 = "Mitra Basu"
    #n2 = "P. K. Dan"
    url1 = "signs/sig1.png"
    #url2 = "signs/sig2.png"
    log1 = "logos/logo1.png"
    #log2 = "logos/logo2.png"
    for name in names:
        make_certificates2(name,event,date,venue,desig,n1,url1,log1)
    print(len(names), "certificates done.")