import urllib2

page = urllib2.urlopen("http://www.baidu.com")
text = page.read().decode("utf8")

print(text)