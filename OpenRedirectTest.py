#import all necessary modules to make http requests
import requests

#ask the user to input the vulnerable url
url = input("Enter the URL to be tested: ")

#ask the user to input the file with the payloads
payloads = "OpenRedirectPayloads.txt"
#ask the user to input the file with the redirections
redirections = "OpenRedirectURIList.txt"

#open the file with the payloads
with open(payloads, "r") as f:
    #read the file with the payloads
    payload = f.read()
    #split the payloads into a list
    payload = payload.split("\n")

#open the file with the redirections
with open(redirections, "r") as f:
    #read the file with the redirections
    redirection = f.read()
    #split the redirections into a list
    redirection = redirection.split("\n")

# Loop through the redirections and try all the payloads
for redir in redirection:
    for pay in payload:
        # Create the payload string
        payload_str = redir + pay
        # Make the request
        full_url = url + payload_str
        print("Testing: " + full_url)
        r = requests.get(full_url)
        print(r.url);
        # Check if the payload was successful
        if r.url != full_url:
            print("HIT: " + full_url)

