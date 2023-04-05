#generate a sitemap of a given website
#import the required modules
import requests
import sys

#ask the user to input the url
url = input("Enter the URL to be tested: ")

#Request the url and parse the html
r = requests.get(url)
html = r.text
#split the html into a list
html = html.split("\n")
#find all links in the html
links = []
for line in html:
    if "href=" in line:
        links.append(line)
