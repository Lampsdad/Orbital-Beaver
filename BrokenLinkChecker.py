#take input as a list of links
links = input("Enter the links: ")
#split the links into a list
links = links.split("\n")

#loop through the links and request them
for link in links:
    #request the link
    r = requests.get(link)
    #if the status code is 200, print the link
    if r.status_code == 200:
        print(link)