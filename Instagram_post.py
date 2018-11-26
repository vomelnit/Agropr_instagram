# -*- coding: utf-8 -*-
from selenium import webdriver
# import selenium.webdriver.common.action_chains
# from selenium import common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import urllib.request
import Image_format
import Conf_features
import  hashtag_creator
# probably_posted=False
# counter_of_posts=0
import Cookies

mobile_emulation = { "deviceName": "iPhone 6" }
#img_link=''
name_of_article=''
text_of_article=''
hashtag_category=''
article_link=''
article_number=0
successful_post=False
attempt=0
username=Conf_features.username
psw=Conf_features.password




def define_variables(name,text,hashtag,number,link):
            global name_of_article
            global text_of_article
            global hashtag_category
            global article_number
            global successful_post
            global article_link

            name_of_article = name
            text_of_article = text
            hashtag_category = hashtag
            article_number = number
            article_link = link


def put_img_to_folder(image_link,number,name,high_text):
        print(image_link)
        urllib.request.urlretrieve(image_link,'agropravda_images/'+'img_of_article'+str(number)+'.jpg')
        Image_format.Image_change('agropravda_images/'+'img_of_article'+str(number)+'.jpg',name,high_text)



def enter_to_instagram(driver):
        global probably_posted
        #global counter_of_posts
        global successful_post

        try:
                print("parse"+article_link)
                driver.get(article_link)
                time.sleep(2)
                WebDriverWait(driver, 15).until(EC.visibility_of_all_elements_located)
                description = driver.find_element_by_xpath("// body / div[1] / div[2] / div[7] / div[1] / div / div[1] / div[3]").text
                print(description)
                d=driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[7]/div[1]/div/div[1]/div[4]/div[1]/p")
                txt=''
                for c in range(len(d)):
                        txt+=d[c].text
                print(txt)
                print("getted")
                #print(str(d))
                #print(len(d))
                time_of_reading=len(d)//1000+1
                # for m in re.finditer("\n",d):
                #         if m.start()>=1000:
                #                 d=d[:m.start()]
                #                 print(len(d))
                #                 break
                #         print(len(d))



        except Exception as msg:
                print(msg)

        try:
                # cookies = Cookies.pickle.load(open(Conf_features.Cookies_file_name, "rb"))
                # print(len(cookies))
                # print(cookies)
                # driver.get("https://www.google.com/")
                # for cookie in cookies:  # session cookies
                #         # Setting domain to None automatically instructs most webdrivers to use the domain of the current window
                #         # handle
                #         cookie_dict = {'domain': cookie.get('domain'), 'name': cookie.get('name'),
                #                        'value': cookie.get('value'), 'secure': cookie.get('secure')}
                #         if cookie.get('expires') != None:
                #                 cookie_dict['expiry'] = cookie.get('expires')
                #         if cookie.get('path') != None:
                #                 cookie_dict['path'] = cookie.get('path')
                #         if cookie.get('httpOnly') != None:
                #                 cookie_dict['httpOnly'] = cookie.get('httpOnly')
                #         print(cookie_dict)
                #
                #         driver.add_cookie(cookie_dict)
                driver = Cookies.Get_cookies(driver,Conf_features.Cookies_file_name)

        except Exception as msg:
                print(msg)
                driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
                # driver.implicitly_wait(10)
                #time.sleep(1)
                #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[text()='Log in']")))
                #try:
                # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//main/article/div/div/div/button")))
                # button_login = driver.find_element_by_xpath("//*[text()='Log in']")
                # button_login.click()
                    #WebDriverWait(driver, 10).until(EC.)

                    #user_mail = driver.find_element_by_xpath("//*[@class='login-button__user']")
                    #assert user_mail.text == "au"
                # except selenium.common.exceptions.NoSuchElementException:
                #     link_entry = driver.find_element_by_link_text("/accounts/login/?source=auth_switcher")
                #     link_entry.click()
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Phone number, username, or email']")))
                login_field = driver.find_element_by_name("username")
                login_field.send_keys(username)
                WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[text()='Password']")))
                password_field = driver.find_element_by_name("password")
                password_field.send_keys(psw)
                # button_entry = driver.find_element_by_xpath("//*[text()='Войти']")
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Log in']")))
                time.sleep(1)
                entry_form = driver.find_element_by_xpath("//form[@method='post']")
                entry_form.submit()
                #button_entry = driver.find_element_by_xpath("//*[text()='Log in']")
                #button_entry.click()
                print("Log in")

                #time.sleep(600)
                #Cookies.pickle.dump(driver.get_cookies(), open(Conf_features.Cookies_file_name, "wb"))

                #driver.implicitly_wait(10)
                #WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located)
                try:
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Not Now']")))
                        #driver.implicitly_wait(10)
                        button_not_now = driver.find_element_by_xpath("//*[text()='Not Now']")
                        button_not_now.click()
                        print("Not now")
                except Exception as msg:
                        print(msg)

        # time.sleep(5)
        # driver.get("https://www.instagram.com/")

        time.sleep(5)
        driver.get("https://www.instagram.com/" + username)
        #driver = Cookies.Get_cookies(driver, Conf_features.Cookies_file_name)
        # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Profile']")))
        # driver.get("https://www.instagram.com/"+username)
        #time.sleep(1)
        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located)
        # amount_of_posts = int(driver.find_element_by_xpath("//ul/li/span/span").text)
        # print(amount_of_posts)

        post = []
        for j in range(9):
                xpath_str="// section / main / div / div[3] / article / div[1] / div / div[{0}] / div[{1}] / a / div / div[1] / img".format(str((j)//3+1),str((j)%3+1))
                post.append(driver.find_element_by_xpath(xpath_str).get_attribute("alt"))#[:driver.find_element_by_xpath(xpath_str).get_attribute("alt").find("\n")])
                print(post[j])
                if post[j].find(description)!=-1: successful_post=True
        print(len(post))
        # if (probably_posted==True)&(counter_of_posts<amount_of_posts):
        #         successful_post=True
        #         counter_of_posts = amount_of_posts

        if successful_post == False:

                print(driver.current_url)
                #driver.get("https://www.instagram.com/")
                time.sleep(2)
                print(driver.current_url)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='New Post']")))
                button_new_post = driver.find_element_by_xpath("//span[@aria-label='New Post']")
                print(button_new_post.get_attribute("aria-label"))
                print(driver.current_url)
                button_new_post.click()
                time.sleep(2)
                # button_new_post = driver.find_element_by_xpath("//span[@aria-label='New Post']")
                # button_new_post.click()
                print(driver.current_url)
                print("Menuitem_add_post")
                #driver.refresh()
                send_img=driver.find_element_by_xpath("//input[@accept='image/jpeg']")
                print(driver.current_url)
                #send_form=driver.find_elements_by_xpath("//form[@enctype='multipart/form-data']")
                #print(send_img)
                #time.sleep(2)
                #print(send_form)
                #send_img.click()
                Imagepath = os.path.abspath('agropravda_images/'+'img_of_article'+str(article_number)+'.jpg')
                print(driver.current_url)
                send_img.send_keys(Imagepath)
                time.sleep(1)
                print(driver.current_url)

                print("Sent keys of img")


                # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Expand']")))
                # spire_button = driver.find_element_by_xpath("//*[text()='Expand']")
                # spire_button.click()
                # print("Expand")
                #
                # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Rotate']")))
                # rotate_button=driver.find_element_by_xpath("//*[text()='Rotate']")
                # rotate_button.click()
                # time.sleep(0.5)
                # rotate_button.click()
                # time.sleep(0.5)
                # rotate_button.click()
                # time.sleep(0.5)
                # rotate_button.click()
                # print("Rotated")

                #time.sleep(2)
                #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Filter']")))
                #print("wait")
                #spire_button = driver.find_element_by_xpath("//*[text()='Filter']")
                # spire_button =driver.find_element_by_xpath("//button[@tabindex='0']")
                # print("find button")
                # spire_button.click()
                # print("Click")
                # print("Filter button")
                # #time.sleep()
                # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Lark']")))
                # spire_button = driver.find_element_by_xpath("//*[text()='Lark']")
                # # action = selenium.webdriver.common.action_chains.ActionChains(driver)
                # # action.drag_and_drop_by_offset(spire_button, -25, 0).perform()
                # #
                # # time.sleep(1)
                # # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Ludwig']")))
                # # spire_button = driver.find_element_by_xpath("//*[text()='Ludwig']")
                # spire_button.click()
                # print("Pressed on (Lark)")
                # time.sleep(3)

                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Next']")))
                button_next = driver.find_element_by_xpath("//*[text()='Next']")
                button_next.click()
                print("Next")

                time.sleep(2)
                #driver.implicitly_wait(10)
                WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located)
                #time.sleep(5)
                text_field = driver.find_element_by_xpath("//textarea[@aria-label='Write a caption…']")
                #text_field = driver.find_element_by_name("Введите подпись...")
                text_field.clear()
                text_field.send_keys(description+' . .\n_________________________________\n\nПодробнее по ссылке в профиле\nВремя прочтения: ~'+str(time_of_reading)+' мин'+'\n'+hashtag_category+' #агроправда #agropravda'+' '+hashtag_creator.Create_hashtags(name_of_article))
                print("Added text")
                # send_img[1].send_keys(Imagepath)
                time.sleep(1)
                button_share = driver.find_element_by_xpath("//*[text()='Share']")
                button_share.click()
                print("Share")
                #probably_posted = True

                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Profile']")))
                driver.get("https://www.instagram.com/"+username)
                time.sleep(2)

                for j in range(9):
                        xpath_str = "// section / main / div / div[3] / article / div[1] / div / div[{0}] / div[{1}] / a / div / div[1] / img".format(
                                str((j) // 3 + 1), str((j) % 3 + 1))
                        post.append(driver.find_element_by_xpath(xpath_str).get_attribute("alt")) #[
                                   # :driver.find_element_by_xpath(xpath_str).get_attribute("alt").find("\n")])
                        print(post[j+9])
                        if post[j+9].find(description) != -1: successful_post = True

                if (post[9].find(description)==-1)|(len(post[9])==0):
                        for l in range(8):
                                if post[l+10]==post[l]: successful_post=True
                                else:
                                        successful_post=False
                                        break
                # new_amount_of_posts=int(driver.find_element_by_xpath("//ul/li/span/span").text)
                # print(new_amount_of_posts)
                #
                # if (new_amount_of_posts>amount_of_posts): successful_post=True
                #
                # if (new_amount_of_posts>amount_of_posts):
                #         successful_post=True
                #         counter_of_posts=new_amount_of_posts

# class LoginMailBox(unittest.TestCase):


def setUp():


        chrome_options = webdriver.ChromeOptions()
        # Add the mobile emulation to the chrome options variable
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome_options.add_experimental_option("prefs", {"intl.accept_languages": "en-US"})
        #chrome_options.add_argument('headless')
        #self.driver\
        driv = webdriver.Chrome(executable_path='./chromedriver',chrome_options=chrome_options)
        return driv




def test_user_login_in_mail_box(dr):
        driver = dr
        global successful_post
        global attempt
        #WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located)
        print(time.strftime("%H:%M:%S", time.gmtime(time.time())))
        try:
                enter_to_instagram(driver)
                Cookies.pickle.dump(driver.get_cookies(), open(Conf_features.Cookies_file_name, "wb"))
        except Exception as msg:
            print(msg)
            print("Error_of instagram")
            attempt+=1
        print(time.strftime("%H:%M:%S", time.gmtime(time.time())))
        #driver.close()

        driver.quit()

def tear_down(self):
        self.driver.quit()

def begin_of_driver(image_link, name, text, hashtag, number,high_text,link):
        print("begin of driver")
        global successful_post
        global attempt
        put_img_to_folder(image_link, number,name,high_text)
        define_variables(name, text, hashtag, number,link)
        attempt=1
        while(successful_post!=True):
            test_user_login_in_mail_box(setUp())
            print("Attempt #"+str(attempt))
            print(str(successful_post))
            #attempt+=1
            if (attempt>=15): break

        if_post=successful_post
        successful_post=False
        return if_post
