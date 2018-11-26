from selenium import webdriver
import pickle
import time



def Get_cookies(driver,filename):

    cookies = pickle.load(open(filename, "rb"))
    print(len(cookies))
    print(cookies)

    for cookie in cookies:  # session cookies
        # Setting domain to None automatically instructs most webdrivers to use the domain of the current window
        # handle
        cookie_dict = {'domain': cookie.get('domain'), 'name': cookie.get('name'), 'value': cookie.get('value'), 'secure': cookie.get('secure')}
        if cookie.get('expires')!=None:
            cookie_dict['expiry'] = cookie.get('expires')
        if cookie.get('path')!=None:
            cookie_dict['path'] = cookie.get('path')
        if cookie.get('httpOnly')!=None:
            cookie_dict['httpOnly'] = cookie.get('httpOnly')
        print(cookie_dict)

        driver.add_cookie(cookie_dict)

    return driver


