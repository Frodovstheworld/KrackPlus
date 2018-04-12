#!/bin/python

###
#
# Issues: 
#	fails to save more than one ip/mac
#	should use something like findUnique so that only unique IPs/MACs are kept 
#	Save whether mac vulnerable to attack A and/or B in hashmap. 
#
###

import re	# used for regular expressions TODO: Har vi noen RE's?
import time
import subprocess

mac = ''
ip = ''
pairMacIP = {mac: ip}
groupVulnMacIP = {mac: ip}
pairwiseVulnMacIP = {mac: ip}

def scanParser(nmap):
	with open('./scanOutput.txt', 'r') as output:
		mac = ''
		ip = ''
		pairMacIP = {mac:ip}
                groupVulnMacIP = {mac:ip}
                pairwiseVulnMacIP = {mac:ip}
                counter = 0
		# goes through the file line by line
		while True:
		        time.sleep(0.5)
		        for line in output.readlines():
		                if (str("]")) in line:
		                        line = line.split(']')[1]
		                        # Filter out interesting lines and parse them
		                if (str("AP-STA-CONNECTED")) in line:
		                        connectedDevice = line.split("AP-STA-CONNECTED ")[1]
		                        print "Device connected with MAC: " + connectedDevice
				if (str("DHCP reply")) in line:
		                        mac = (line.split('DHCP')[0])
					mac = (str(mac).strip())[:-1]
					ip = line.split('reply')[1]
					ip = (ip.split('to')[0]).strip()
					pairMacIP.update({mac:ip})
				if (str("vulnerable")) in line:
		                        if (str("DOESN'T")) in line:
		                                if (str("group")) in line:
							print (mac+" is not vulnerable to group key reinstallation")
						else:
							print (mac+" is not vulnerable to pairwise")  
					else:
						if str("group") in line:
							print (mac+" is vulnerable to group key reinstallation")
						else:
							print (mac+" is vulnerable to pairwise")
                                                        
def nmapOS(dictionary):
        print "Running NMAP OS Scan against connected devices..."
        with open('nmapOutput.txt', 'w') as nmapOutput:
            for key, value in dictionary.iteritems():
                if key != '' and value != '':
                    print value
                    subprocess.check_output(["nmap -O " + value], stdout=nmapOutput, shell=True)

def printDictionary(dictionary):
    # Prints everything in the dictionary.
    for key, value in dictionary.iteritems():
        if key != '' and value != '':
                print "Key: " + key + " has value: " + value

def writeDictionary(dictionary, file):
    with open(file, 'w') as MacIP:
        # Prints the dictionary to file
        for key, value in dictionary.iteritems():
            if key != '' and value != '':
                MacIP.write(key + '\n')
                MacIP.write(value + '\n')
    MacIP.closed

def writeResults():
    writeDictionary(pairMacIP, './scannedMacIP.txt')
    writeDictionary(pairwiseVulnMacIP, './pairwiseVulnMacIP.txt')
    writeDictionary(groupVulnMacIP, './groupVulnMacIP.txt')


