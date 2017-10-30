import urllib2
import re

url = input("Enter the Uniform Resource Locator ( URL: )" )
#connect to a URL
website = urllib2.urlopen(url)

#read html code
html = website.read()

#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

#Links will be printed
print links
