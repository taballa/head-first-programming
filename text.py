#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, time
def get_price():
    i = 0
    # URL = "http://www.douban.com" # utf8
    # URL = "http://www.gome.com.cn" # utf8
    URL = "http://www.jd.com" # gbk
    key = u'￥' # end_of_price = 1
    while i < 2:
        print("Today discounted price is: ")
        page = urllib2.urlopen(URL)
        text = page.read().decode('gbk') # to Unicode
        where = text.find(key)    
        start_of_price = where + 1
        end_of_price = start_of_price + 6
        price = text[start_of_price:end_of_price]
        # price_gbk = price.encode('gbk', 'ignore')
        print start_of_price
        print end_of_price
        # print price_gbk
        print price # 跳出循环
        i = i + 1
        time.sleep(1)
    print("bye!")

print("Hello Welcome to Supermarket.")

repeat = 'y'

while repeat == 'y':
    get_price()
    _x = raw_input('Do you repeat? (Y/N)')
    repeat = str(_x)

def send_to_mail():
   msg = "I am a message that will be sent to your email." 
   password_manager = urllib2.HTTPPasswordMgr()
   password_manager.add_password("douban API", "http://www.douban.com/", "tel800810@gmail.com", "qq440106")
   http_handle = urllib2.HTTPBasicAuthHandler(password_manager)
