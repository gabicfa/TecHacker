#!/usr/bin/python

import argparse
import socket as sk
from socket import *

def wellKnown(sock, targetPort, scanType):
    try:
        if(targetPort<=1023):
            service = sk.getservbyport(targetPort, scanType)
            print("Servece Running: " + str(service))
    except:
        print("No service running")

def tcpScan(targetIp,targetPort):
    sock = socket(AF_INET,SOCK_STREAM)
    try: 
        sock.connect((targetIp,int(targetPort)))
        print ("[+] TCP Port: " +str(targetPort) + " Open")
        
    except: 
        print ("[+] TCP Port: " +str(targetPort) + " CLOSED")
    
    finally:
        wellKnown(sock, targetPort, "tcp")
        sock.close()

def udpScan(targetIp,targetPort):
    consock = socket(AF_INET,SOCK_DGRAM)
    
    try:
        consock.connect((targetIp,targetPort))
        print ("[+] UDP Port Open: " + str(targetPort))
        
    except:
        print ("[+] UDP port closed: " + str(targetPort))
    
    finally:
        wellKnown(consock, targetPort, "udp")
        consock.close()
    
def checkType(ip,port,typeScan,rangeport):
    print ("Port Scan Initiated on: " + ip + "\n") 
    if not(rangeport):
        for ports in port:
            if (typeScan == "isTcp"):
                tcpScan(ip,int(ports))
            elif(typeScan == "isUdp"):
                udpScan(ip,int(ports))
    else:
        for ports in range (int(port[0]), int(port[1])+1):
            if (typeScan == "isTcp"):
                tcpScan(ip,int(ports))
            elif(typeScan == "isUdp"):
                udpScan(ip,int(ports))
       
if __name__ ==  "__main__":
    
    print ("Welcome To Port Scanner!\n")
    try:
        parser = argparse.ArgumentParser("TCP Scanner")
        parser.add_argument("-a","--address",type=str,help="Enter the ip address to scan")
        parser.add_argument("-p","--ports",type=str,help="Enter The port to scan")
        parser.add_argument("-rp","--rangeports",type=str,help="Enter a range of port to scan")
        parser.add_argument("-u","--udp",action="store_true")
        parser.add_argument("-t","--tcp",action="store_true")
        args = parser.parse_args()
        remoteserver = args.address
        ipaddress = gethostbyname(remoteserver)
        try:
            port = args.ports.split(',')
            rangeport = False
        except:
            port = args.rangeports.split('-')
            rangeport = True

        isUdp = args.udp
        isTcp = args.tcp

        if(isUdp):
            checkType(ipaddress,port,"isUdp", rangeport)
        if(isTcp):
            checkType(ipaddress,port,"isTcp", rangeport)
        
    except:
        print ("[+] No Arugments Supplied\nExamples:\npython portscanner.py -u -a 192.168.43.224 -rp 22-80\npython portscanner.py -t -a 192.168.43.224 -p 22, 30,80 ")