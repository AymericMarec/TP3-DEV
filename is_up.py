from sys import argv
import os

test = os.popen("ping "+argv[1]).read()

if(len(test.split('\n')) <= 2):
    print("DOWN !")
else :
    if(test.split('\n')[3] == "D‚lai d'attente de la demande d‚pass‚."):
        print("DOWN !")
    else :
        print("UP !")    