#!/usr/bin/python3
  
# Converts scanned mac-addresses into commands to whitelist the AP in ARUBA
import sys

macaddyFile = open(sys.argv[1], 'r')
macaddyOutput = open(sys.argv[2], 'w')

for address in macaddyFile:
    convertedAddress = ':'.join([ i+j for i,j in zip(address[::2],address[1::2])])
    # Command syntax:
    # whitelist-db rap add mac-address 90:4C:81:CA:B8:A8 ap-group default ap-name 90:4C:81:CA:B8:A8
    macaddyOutput.write("whitelist-db rap add mac-address " + convertedAddress + " ap-group default ap-name " + convertedAddress + "\n")

macaddyFile.close()
macaddyOutput.close()
