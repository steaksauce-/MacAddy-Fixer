#!/usr/bin/python3
  
# Converts scanned mac-addresses into formatted mac-addresses.
import sys

macaddyFile = open(sys.argv[1], 'r')
macaddyOutput = open(sys.argv[2], 'w')

for address in macaddyFile:
    convertedAddress = ':'.join([ i+j for i,j in zip(address[::2],address[1::2])])
    macaddyOutput.write(convertedAddress + "\n")

macaddyFile.close()
macaddyOutput.close()
