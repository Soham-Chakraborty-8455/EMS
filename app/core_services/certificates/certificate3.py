from PIL import Image,ImageDraw,ImageFont
import os
if not os.path.exists('certificates/certificatesave'):
    os.makedirs('certificates/certificatesave')
#FONT_FILE = ImageFont.truetype("arial.ttf", 50)
#FONT_FILE_o = ImageFont.truetype("arial.ttf", 30)
FONT_COLOR = "#000000"
t1 = Image.open('certificates/cert/cert3.png')
WIDTH, HEIGHT = t1.size
def make_certificates3(name,event,date,org,desig,n1,url1,log1):
    image_source = Image.open('certificates/cert/cert3.png')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name)
    draw.text((813,720), name, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",75))
    event_width, event_height = draw.textsize(event)
    draw.text((696,913), event, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",30))
    date_width, date_height = draw.textsize(date)
    draw.text((1560,912), date, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",30))
    org_width, org_height = draw.textsize(org)
    draw.text((1153,910), org, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",30))
    name_width, name_height = draw.textsize(name)
    draw.text((1132,862), name, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",30))

    desig_width, desig_height = draw.textsize(desig)
    draw.text((432,1220), desig, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",30))
    #design_width, design_height = draw.textsize(design)
    #draw.text((1404,1204), design, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",30))
    n1_width, n1_height = draw.textsize(n1)
    draw.text((433,1133), n1, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",30))
    #n2_width, n2_height = draw.textsize(n2)
    #draw.text((1391,1123), n2, fill=FONT_COLOR,font=ImageFont.truetype("arial.ttf",30))
    #image_source.save("./out/" + name +".png")
    #print('Saving Certificate of:', name)

    insert_image1 = Image.open(url1)
    #insert_image2 = Image.open(url2)

    width1, height1 = insert_image1.size
    #width2, height2 = insert_image2.size
    x = width1/height1
    #y = width2/height2
    if x <= 3 :
        insert_image1 = insert_image1.resize((250,75))
        image_source.paste(insert_image1, (400,1040))
    else:
        insert_image1 = insert_image1.resize((450,75))
        image_source.paste(insert_image1, (400,1040))
        
    #if y <= 3 :
        #insert_image2 = insert_image2.resize((250,75))
        #image_source.paste(insert_image2, (1296,1040))
    #else :
        #insert_image2 = insert_image2.resize((450,75))
        #image_source.paste(insert_image2, (1276,1040))

    logo1 = Image.open(log1)
    #logo2 = Image.open(log2)

    width3, height3 = logo1.size
    #width4, height4 = logo2.size
    a = width3/height3
    #b = width4/height4
    if a <= 3:
        logo1 = logo1.resize((100,100))
        image_source.paste(logo1, (1400,1040))
    else :
        logo1 = logo1.resize((200,100))
        image_source.paste(logo1, (1400,1040))

    #if b <= 3 :
        #logo2 = logo2.resize((100,100))
        #image_source.paste(logo2, (1045,63))
    #else :
        #logo2 = logo2.resize((200,100))
        #image_source.paste(logo2, (1045,63))

    image_source.save('certificates/certificatesave/certificate.png', format='PNG')

if __name__ == "__main__":
    names = ["Soham Chakraborty", "Kaustav Giri", "Pritha Saha","Ujjaini Ray"]
    event = "Metathon"
    date = "28.12.2022"
    #venue = "Taal Kutir Convention"
    org = "Presidency"

    desig = "Principal"
    #design = "Student Head"
    n1 = "Mitra Basu"
    #n2 = "P. K. Dan"
    url1 = "signs/sig1.png"
    #url2 = "signs/sig2.png"
    log1 = "logos/logo1.png"
    #log2 = "logos/logo2.png"
    for name in names:
        make_certificates3(name,event,date,org,desig,n1,url1,log1)
    print(len(names), "certificates done.")