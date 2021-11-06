import urllib.request
import chardet

url = input("请输入URL：")

response = urllib.request.urlopen("http://%s"%url).read()
count = chardet.detect(response)

print("该网页使用的编码是：%s"%count['encoding'])
