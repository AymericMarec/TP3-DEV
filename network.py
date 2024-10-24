import socket
from sys import argv
import re
import os
import psutil
import time
import datetime



def lookup(hostname):
    if(re.search("[a-z]+\.+[a-z]",hostname)):
        return socket.gethostbyname(hostname)
    else :
        print("bad hostname")
        return None
def ping(ip):
    test = os.popen("ping "+ip).read()
    if(len(test.split('\n')) <= 2):
        return "DOWN !"
    else :
        if(test.split('\n')[3] == "D‚lai d'attente de la demande d‚pass‚."):
            return "DOWN !"
        else :
            return "UP !"  

def ip():
    infos = str(psutil.net_if_addrs()['Wi-Fi'][1])
    ip = infos.split('\'')[1]
    return ip

def AddLog(response,command,args):
    LogSentence = ""
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    LogSentence += str(date)
    if not response == None :
        LogSentence += " [INFO] Command "+ command +" called successfully " +"\n"
    else :
        LogSentence += " [ERROR] Command " + command + " called with bad arguments : " + str(args) +"\n"
    
    LOG_FILE = os.path.join(os.getenv('localappdata'), "Temp", "network_tp3","network.log")
    log = open(LOG_FILE, "a")
    log.write(LogSentence)
    log.close()

Arg1 = None
Arg2 = None
if len(argv) > 1:
    Arg1 = argv[1]
if len(argv) > 2:
    Arg2 = argv[2]


response = ""

match(Arg1):
    case "lookup":
        response = lookup(argv[2])
    case "ping":
        response = ping(argv[2])
    case "ip":
        response = ip()
    case _ :
        response = Arg1 +" is not an available command. Déso."


pathFolder = os.path.join(os.getenv('localappdata'), "Temp", "network_tp3")

if not os.path.exists(pathFolder):
    os.makedirs(pathFolder)
    print("dossier crééée : "+pathFolder)

AddLog(response,Arg1,Arg2)

print(response)