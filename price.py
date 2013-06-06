import urllib2, time, codecs

i = 0
URL = "http://www.douban.com"
while i < 3:
    time.sleep(1)
    page = urllib2.urlopen(URL)
    text = page.read().decode('utf8') # to Unicode
    text_gbk = text.encode('gbk', 'ignore')
    print text_gbk
    i = i + 1

print("bye!")