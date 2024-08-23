from PIL import Image,ImageDraw,ImageFont
import os
if not os.path.exists('certificates/certificatesave'):
    os.makedirs('certificates/certificatesave')
#FONT_FILE = ImageFont.truetype("arial.ttf", 50)
#FONT_FILE_o = ImageFont.truetype("arial.ttf", 30)
FONT_COLOR = "#000000"
t1 = Image.open('certificates/cert/cert1.png')
WIDTH, HEIGHT = t1.size
#def make_certificates(name,event,date,venue):
def make_certificates1(name,gender,event,desig,n1,url1,log1):
    image_source = Image.open('certificates/cert/cert1.png')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name)
    draw.text((762,570), name,fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",90))
    gender_width, gender_height = draw.textsize(gender)
    draw.text((1218,849), gender, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",25))
    gender_width, gender_height = draw.textsize(gender)
    draw.text((974,785), gender, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",35))
    event_width, event_height = draw.textsize(event)
    draw.text((579,837), event, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",45))
    desig_width, desig_height = draw.textsize(desig)
    draw.text((520,1170), desig, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",40))
    #design_width, design_height = draw.textsize(design)
    #draw.text((1302,1170), design, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",40))
    n1_width, n1_height = draw.textsize(n1)
    draw.text((488,1099), n1, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",40))
    #n2_width, n2_height = draw.textsize(n2)
    #draw.text((1301,1099), n2, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",40))
    #event_width, event_height = draw.textsize(event)
    #draw.text((568,938), event, fill=FONT_COLOR)
    #date_width, date_height = draw.textsize(date)
    #draw.text((948,930), date, fill=FONT_COLOR)
    #venue_width, venue_height = draw.textsize(venue)
    #draw.text((1238,930), venue, fill=FONT_COLOR)
    #image_source.save("./out/" + name +".png")
    #print('Saving Certificate of:', name)

    insert_image1 = Image.open(url1)
    #insert_image2 = Image.open(url2)
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




    width1, height1 = insert_image1.size
    #width2, height2 = insert_image2.size
    x = width1/height1
    #y = width2/height2
    if x <= 3:
        insert_image1 = insert_image1.resize((250,75))
        image_source.paste(insert_image1, (453,994))
    else :
        insert_image1 = insert_image1.resize((450,75))
        image_source.paste(insert_image1, (453,994))

    #if y <= 3 :
        #insert_image2 = insert_image2.resize((250,75))
        #image_source.paste(insert_image2, (1269,994))
    #else :
        #insert_image2 = insert_image2.resize((450,75))
        #image_source.paste(insert_image2, (1269,994))

    image_source.save('certificates/certificatesave/certificate.png', format='PNG')


if __name__ == "__main__":
    names = ["Soham Chakraborty", "Kaustav Giri", "Pritha Saha","Ujjaini Ray"]
    event = "Devfest Kolkata 2023"
    #date = "28.12.2022"
    #venue = "Taal Kutir Convention"
    gender = "his/her"
    desig = "Principal"
    #design = "Student Head"
    n1 = "Mitra Basu"
    #n2 = "P. K. Dan"
    url1 = "signs/sig1.png"
    #url2 = "signs/sig2.png"
    log1 = "logos/logo1.png"
    #log2 = "logos/logo2.png"
    for name in names:
        #make_certificates(name,event,date,venue)
        make_certificates1(name,gender,event,desig,n1,url1,log1)
    print(len(names), "certificates done.")