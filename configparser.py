import configparser

myconfig = configparser.ConfigParser()
myconfig.read('config.ini')

myDomain = myconfig['domains']['ddns']
print(myDomain)
