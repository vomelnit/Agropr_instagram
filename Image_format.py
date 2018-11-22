from PIL import Image,ImageFont,ImageDraw

def Image_change(image_name,name_of_article,high_text):
    image1 = Image.open(image_name)
    (width, heigh) = image1.size
    # (width,heigh)=image1.size
    # print(width)
    # print(heigh)
    # y=heigh*0.6
    # y1=heigh*0.65
    # x1=width*0.05
    #image1.show()
    #image1.thumbnail((300,300))
    text=name_of_article
    while text.find('«')!=-1:
        text_quot1=text.find('«')
        text_quot2=text.find('»')
        text=text[:text_quot1]+'"'+text[text_quot1+1:]
        text = text[:text_quot2] + '"' + text[text_quot2+1:]

        # text[text_copy1.find('«')]='"'
        # text[text_copy1.find('»')] = '"'
        # text = text_copy1[:text.find('«')]+'"'+text[text.find('«')+1:]
        # text = text_copy2[:text.find('»')] + '"' + text[text.find('»') + 1:]
        # second_quot=text.find('»')
        # text[second_quot] = '"'
    text_len=len(text)
    words=text.split(' ')
    print(len(words))
    new_text=''
    font_size = round(width / 20)
    separator=25
    if text_len >= 50:
        font_size = round(font_size * 0.8)
        separator=30
    counter_of_symbols=0
    for i in range(len(words)):
        counter_of_symbols+=len(words[i])
        if counter_of_symbols>=separator:
            new_text+='\n'
            counter_of_symbols=len(words[i])
        new_text+=words[i]+' '


    (width,heigh)=image1.size
    print(heigh)
    differ=width-heigh
    categ_beginy=heigh+differ*0.05
    categ_beginx=width*0.1
    text_beginx = width * 0.03
    text_beginy=heigh+differ*0.2
    # if width>heigh:
    img=Image.new(mode='RGB',size=(width,width),color='#003333')
    im=image1.point(lambda p: p * 1.15)
    img.paste(im,(0,0))
    #img.show()
    font_size=round(width/19)
    if text_len>=50:
        font_size=round(font_size*0.8)
    else:
        y=heigh*0.4
        y1=heigh*0.5
    x1=width*0.1
    #img = image1.point(lambda p: p * 0.6)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("12241.ttf", font_size)
    fontt = ImageFont.truetype("12241.ttf", round(font_size/1.5))
    draw.text((text_beginx, categ_beginy),high_text.upper(),'#FFD700',font=fontt)
    draw.text((text_beginx, text_beginy),new_text,(255,255,255),font=font)
    # draw.text((105, 210),"уже 20 лет. Какими они были",(255,255,255),font=font)
    img.save(image_name)
    #img=image1.filter(ImageFilter.SMOOTH_MORE)
    #img.show()