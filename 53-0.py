import urllib.request

response = urllib.request.urlopen("https://ilovefishc.com/")
html = response.read(300)
print(html.decode("utf-8"))
    
    
