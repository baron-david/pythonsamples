import urllib.request

response = urllib.request.urlopen("http://checkip.amazonaws.com")
print(response.readline())
print(response.close())
