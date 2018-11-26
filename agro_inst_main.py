# -*- coding: utf-8 -*-
import feedparser
import time
import Instagram_post

#CHANNEL_NAME = id_name.CHANNEL_NAME
list_of_articles = []
text = ''
i=0
counter_of_articles=0
if_need_to_post = False
if_list_refreshed = False
image_error = False
#rss_link = id_name.rss_link
category_interpretator=[["#тракторы","#комбайны","#техникафермера","#автотехника","#спецтехника","#прицепоборудывание",
                         "#акциидилеров","#законодательство","#кредитованиелизинг","#химиядляпочвы",
                         "#химиядлярастений","#рынокзапчастей","#агрорынок","#испытаниетехники","#новыетехнологии",
                         "#агробизнесlife","#мототехника"],
                        ["tractors","combains","technika-fermera","auto-technika","special-technik","pricepnoe-oborudovanie",
                         "akcii-dillerov","zakonodatelstvo","creditovanie-lizing","chimiya-dla-pochvy",
                         "chimia-dla-rasteniy","rynok-zapchastey","agrorynok","ispytanye-techniki","novye-technologi","agrobiznes-life","mototehnika"],
                        ["тракторы", "комбайны", "техника фермера", "автотехника", "спецтехника",
                         "прицепоборудывание",
                         "акции дилеров", "законодательство", "кредитование лизинг", "химия для почвы",
                         "химия для растений", "рынок запчастей", "агрорынок", "испытание техники", "новые технологии",
                         "агробизнес life", "мототехника"]
                        ]






def parse_agropravda(list):
    try:
        feed = feedparser.parse('http://agropravda.com/feed')
        for entry in feed.entries:
            time.sleep(5)
            article_title = search_for_quots(entry.title)
            list.append(article_title)

    except Exception as msg:
        print(msg)
        print(time.strftime("%H:%M", time.localtime()) + "  Error parse")

def search_for_quots(title_text):
    while (title_text.find('&quot;')!=-1):
        title_text_copy=title_text
        title_text=title_text_copy[:title_text.find('&quot;')]+'"'+title_text[title_text.find('&quot;')+6:]
    return title_text


if __name__ == '__main__':
    #parse_agropravda(list_of_articles)



    print(time.strftime("%H:%M", time.localtime()) + "  Begin")
    #print(list_of_articles)


    while True:

            # if (time.strftime("%H:%M", time.localtime()) == '03'):
            #     if_list_refreshed = False
            # if (time.strftime("%H", time.localtime())=='01'):
            #     if (if_list_refreshed==False):
            #         list_of_articles.clear()
            #         parse_autocon(list_of_articles)
            #         if_list_refreshed = True

            try:
                #print("try")
                #print("start parse")
                feed = feedparser.parse('http://agropravda.com/feed')
                #time.sleep(20)

                for entry in feed.entries:

                    #time.sleep(10)
                    article_title = search_for_quots(entry.title)
                    if list_of_articles.count(article_title) == 0:
                        #amount_of_img = len(entry.enclosures)
                        print(time.strftime("%H:%M", time.localtime()) + "  New article:"+article_title)
                        if_need_to_post = True
                        if if_need_to_post == True:
                            article_link = entry.link
                            article_link = article_link[7:]
                            print(time.strftime("%H:%M", time.localtime()) + "  Added link")
                            article_category = entry.category
                            print(time.strftime("%H:%M", time.localtime()) + "  Added category")
                            if_need_to_post = False
                            print(time.strftime("%H:%M", time.localtime()) + "  if_need_to_post = false")
                            category = article_category
                            print(time.strftime("%H:%M", time.localtime()) + "  Added category")
                            h1=category_interpretator[0][category_interpretator[1].index(category)]
                            high_text=category_interpretator[2][category_interpretator[1].index(category)]
                            print(time.strftime("%H:%M", time.localtime()) + "  Created h1")



                            # while (amount_of_img > img_counter):
                            #         try:
                            #             article_img_link = entry.enclosures[img_counter]
                            #             #print(time.strftime("%H:%M", time.localtime()) + "  Added img")
                            #             bot.send_photo(CHANNEL_NAME, article_img_link.url,
                            #                    caption='*' + article_title + '*' + '\n' + h1 + '\n\n' + article_link,
                            #                    parse_mode='Markdown', reply_markup=keyboard)
                            #             list_of_articles.append(article_title)
                            #             break
                            #         except Exception:
                            #             img_counter += 1
                            #             print('Cannot send image with text')
                            #
                            # if (amount_of_img == img_counter):
                            #text = entry.description
                            i=0
                            article_posted=False
                            while (article_posted!=True):
                                try:
                                    first_image_end=500
                                    text = entry.description
                                    if (text.find(".jpg")!=-1):
                                        first_image_end=text.find(".jpg")
                                        print("1:"+str(first_image_end))
                                        article_img_link = text[10:first_image_end + 4]
                                    if (text.find(".JPG")!=-1)&(text.find(".JPG")<first_image_end):
                                        first_image_end=text.find(".JPG")
                                        print("2:" + str(first_image_end))
                                        article_img_link = text[10:first_image_end + 4]
                                    if (text.find(".png")!=-1)&(text.find(".png")<first_image_end):
                                        first_image_end=text.find(".png")
                                        print("3:" + str(first_image_end))
                                        article_img_link = text[10:first_image_end + 4]
                                    if (text.find(".PNG")!=-1)&(text.find(".PNG")<first_image_end):
                                        first_image_end=text.find(".PNG")
                                        print("4:" + str(first_image_end))
                                        article_img_link = text[10:first_image_end + 4]
                                    if (text.find(".JPEG")!=-1)&(text.find(".JPEG")<first_image_end):
                                        first_image_end=text.find(".JPEG")
                                        print("5:" + str(first_image_end))
                                        article_img_link = text[10:first_image_end + 5]
                                    if (text.find(".jpeg")!=-1)&(text.find(".jpeg")<first_image_end):
                                        first_image_end=text.find(".jpeg")
                                        print("6:" + str(first_image_end))
                                        article_img_link = text[10:first_image_end + 5]
                                    #article_img_link = text[10:first_image_end + 4]
                                    print(time.strftime("%H:%M", time.localtime()) + " (" + article_img_link + ")")

                                    # if (text.find(".JPG")==-1):
                                    #     article_img_link=text[10:text.find(".jpg")+4]
                                    #     print(time.strftime("%H:%M", time.localtime()) + "1: (" + article_img_link+")")
                                    # else:
                                    #     if (text.find(".jpg") == -1):
                                    #         article_img_link = text[10:text.find(".JPG") + 4]
                                    #         print(time.strftime("%H:%M", time.localtime()) + "2: (" + article_img_link+")")
                                    #     else:
                                    #         if (text.find(".JPG")<text.find(".jpg")):
                                    #             article_img_link = text[10:text.find(".JPG") + 4]
                                    #             print(time.strftime("%H:%M", time.localtime()) + "3: (" + article_img_link+")")
                                    #         else:
                                    #             article_img_link = text[10:text.find(".jpg") + 4]
                                    #             print(time.strftime("%H:%M", time.localtime()) + "4: (" + article_img_link+")")


                                    print("Okey")
                                    if (i<5):
                                            print("Okey0")
                                            print(time.strftime("%H:%M", time.localtime()) + " i="+str(i))
                                            if_made_post = Instagram_post.begin_of_driver(article_img_link,
                                                                                          article_title.upper(), text,
                                                                                          h1, counter_of_articles,
                                                                                          high_text,entry.link)
                                            # bot.send_photo(CHANNEL_NAME, article_img_link,
                                            #                 caption='*' + article_title + '*' + '\n' + h1 + '\n\n' + article_link,
                                            #                 parse_mode='Markdown', reply_markup=keyboard)
                                            print("Posted foto")
                                    else:
                                            print("Okey1")
                                            print(time.strftime("%H:%M", time.localtime()) + " i="+str(i))
                                            # bot.send_message(CHANNEL_NAME,
                                            #                      '*' + article_title + '*' + '\n' + h1 + '\n\n' + article_link,
                                            #                      parse_mode='Markdown', reply_markup=keyboard)
                                            print("Posted text")

                                    article_posted = True
                                    counter_of_articles += 1
                                    if (counter_of_articles == 25): counter_of_articles = 0
                                    list_of_articles.append(article_title)

                                    if (i <=6):
                                        i = -1
                                        article_posted=True
                                except Exception as msg:
                                    print(msg)
                                    print(time.strftime("%H:%M", time.localtime()) + " i=" + str(i))
                                    if (article_posted==True):list_of_articles.append(article_title)
                                    i+=1
                                    if(i==6):
                                        i=-1
                                        article_posted = True
                                    print("Cannot send img")
                                    time.sleep(20)








                time.sleep(900)

            except Exception as msg:
                 print(msg)
                 print(time.strftime("%H:%M", time.localtime()) + "  Error loop")
                 time.sleep(900)
