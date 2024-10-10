import socket
from sys import argv
import re

if(re.search("[a-z]+\.+[a-z]",argv[1])):
    print(socket.gethostbyname(argv[1]))
else :
    print("bad hostname")