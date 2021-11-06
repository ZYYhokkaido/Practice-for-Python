import urllib.request

f1=open("urls.txt")

urls=list(f1)

for a in range(len(urls)):
    response=urllib.request.urlopen("%s"%urls[a])
    html=response.read()
    final=html.decode("utf-8")
    f2=open("url_%d.txt"%(a+1),"a")
    f2.writelines(final)
    f2.close()

f1.close()
