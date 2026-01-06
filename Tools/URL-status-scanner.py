import requests

url = input("Enter the URL you want to scan: ") #here you put the URL you want to scan

try:
    response = requests.get(url)
    if response.status_code == 200: # This is the answer from the server
        print("Server Status OK")
    elif response.status_code == 404:
        print("Page not found")
    elif response.status_code == 504:
        print("Gateway timeout")
    elif response.status_code == 403:
        print("Forbidden")
    else:
        print("Possibly another response from the server") # If the server don't found your request, or maybe another what you don't have, this is the response
except:
    print("The URL you entered may be incorrect") # exceptions from the code, you need check this possibles errors
    print("possible firewall block")
    print("url not found")
