import socket

scan = input("Enter the IP Address you want to scan: ")

ports = [7, 9, 13, 21, 23, 25, 26, 37, 53, 79, 81, 88, 106, 110, 111, 113, 119, 135, 139, 143, 144, 179, 199, 389, 427, 443, 445, 465, 513, 515, 543, 544, 548, 554, 587, 631, 646, 873, 990, 993, 995, 1025, 1029, 1110, 1433, 1720, 1723, 1755, 1900, 2000, 2001, 2049, 2121, 2717, 3000, 3128, 3306, 3389, 3986, 4899, 5000, 5009, 5051, 5060, 5101, 5190, 5357, 5432, 5631, 5666, 5800, 5900, 6000, 6001, 6646, 7070, 8000, 8008, 8009, 8080, 8081, 8443, 8888, 9100]

print(f"\nScanning {scan}...\n" + "-"*20)

for port in ports:
    try:
        #you open a new Socket IPv4 TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) #set a timeout to make sure the program don't crash or don't take so long
        result = s.connect_ex((scan, port)) #try to connect to the port (0 means open)

        if result == 0:
            print(f"{port:5} OPEN PORT")
        else:
            print(f"{port:5} CLOSED PORT")
        s.close() #when the Scan finish you need close the Socket
    
    except:
        print("you put a correct IP address?")
        print("you reach that IP address?")
        print("Possible open ports but firewall block")
