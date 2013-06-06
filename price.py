# coding=utf8
import urllib2, time, codecs

i = 0
key = u'¥</span>'
# URL = "http://www.douban.com"
URL = "http://www.gome.com.cn"
while i < 3:
    time.sleep(1)
    page = urllib2.urlopen(URL)
    text = page.read().decode('utf8') # to Unicode
    where = text.find(key)    
    start_of_price = where + 8
    end_of_price = start_of_price + 300
    price = text[start_of_price:end_of_price]
    price_gbk = price.encode('gbk', 'ignore')
    print start_of_price
    print end_of_price
    print price
    print price_gbk
    i = i + 1

print("bye!")