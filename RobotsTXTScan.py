#imports
import requests


#setup main function
def main():
    #take in a base url from the user
    url = input("Enter the URL to be tested: ")
    #send a request to the website to see if there is a robots.txt file
    r = requests.get(url + "/robots.txt")
    #check if the status code is 200
    if r.status_code == 200:
        #print the contents of the robots.txt file
        print(r.text)
        ###################COULD PROBABLY BE OPTIMIZED?###############################
        #split the URL contents of r.text into a list
        disallowed = []
        for line in r.text.split("\n"):
            if line.startswith("Disallow:"):
                disallowed.append(line.split("Disallow:")[1].strip())
        print(disallowed)
        ##############################################################################
        #Send requests to the website to see if the contents of the robots.txt file are accessible
    else:
        #print that there is no robots.txt file
        print("There is no robots.txt file")


#call the main function
main()