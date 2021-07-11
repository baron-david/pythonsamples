import urllib.request

#response = urllib.request.urlopen("http://checkip.amazonaws.com")
response = urllib.request.urlopen("https://domains.google.com/checkip")
result = response.readline()

print(result)
print(result.find(b'76.94.30'))

response.close()
