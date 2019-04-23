#!/usr/bin/python3
  
# Converts scanned mac-addresses into formatted mac-addresses.
import argparse

parser = argparse.ArgumentParser(description="Converts a list of mac-addresses to mac-addresses with a different delimeter (or no delimeter). Default behavior is to convert alpha-numeric mac-addresses to colon delimeted macaddresses.")
parser.add_argument("input", help="A line delimeted file containing mac-addresses to be fixed")
parser.add_argument("output", help="The name of the file to place fixed mac-addresses.")
parser.add_argument("--intype", help="The input macadress type. Supported types are alpha-numeric (012ABC3456FF), cisco (012A.BC34.56FF), colon-delimeted (01:2A:BC:34:56:FF), or hyphen-delimeted (01-2A-BC-34-56-FF). This defaults to alpha-numeric.", choices=["alpha-numberic", "cisco", "colon-delimeted", "hyphen-delimeted"], default="alpha-numeric")
parser.add_argument("--outtype", help="The output macadress type. Supported types are alpha-numeric (012ABC3456FF), cisco (012A.BC34.56FF), colon-delimeted (01:2A:BC:34:56:FF), or hyphen-delimeted (01-2A-BC-34-56-FF). This defaults to colon-delimeted.", choices=["alpha-numberic", "cisco", "colon-delimeted", "hyphen-delimeted"], default="colon-delimeted")
args = parser.parse_args()

def convertMacAddressToAlphaNumeric(address):

    if args.intype == "colon-delimeted":
        alphaNumericAddress = address.replace(':','')
        return alphaNumericAddress
    elif args.intype == "cisco":
        alphaNumericAddress = address.replace('.','')
        return alphaNumericAddress
    elif args.intype == "hyphen-delimeted":
        alphaNumericAddress = address.replace('-', '')
        return alphaNumericAddress
    else:
        return address

def convertMacAddressToColonDelimeted(address):
    colonDelimetedAddress = convertMacAddressToAlphaNumeric(address)
    colonDelimetedAddress = ':'.join([ i+j for i,j in zip(colonDelimetedAddress[::2],colonDelimetedAddress[1::2])])
    return colonDelimetedAddress

def convertMacAddressToCisco(address):
    ciscoAddress = convertMacAddressToAlphaNumeric(address)
    ciscoAddress = '.'.join([ i+j+k+l for i,j,k,l in zip(ciscoAddress[::4],ciscoAddress[1::4],ciscoAddress[2::4],ciscoAddress[3::4])])
    return ciscoAddress

def convertMacAddressToHyphenDelimeted(address):
    hyphenDelimetedAddress = convertMacAddressToAlphaNumeric(address)
    hyphenDelimetedAddress = '-'.join([ i+j for i,j in zip(hyphenDelimetedAddress[::2],hyphenDelimetedAddress[1::2])])
    return hyphenDelimetedAddress




macaddyFile = open(args.input, 'r')
macaddyOutput = open(args.output, 'w')


if args.intype == "alpha-numeric":
    if args.outtype == "colon-delimeted":
        for address in macaddyFile:
            convertedAddress = convertMacAddressToColonDelimeted(address)
            macaddyOutput.write(convertedAddress + "\n")
    elif args.outtype == "hyphen-delimeted":
        for address in macaddyFile:
            convertedAddress = convertMacAddressToHyphenDelimeted(address)
            macaddyOutput.write(convertedAddress + "\n")
    elif args.outtype == "cisco":
        for address in macaddyFile:
            convertedAddress = convertMacAddressToCisco(address)
            macaddyOutput.write(convertedAddress + "\n")
    else:
        print("Cannot convert mac-address to same type!")
        exit(1)
elif args.intype == "colon-delimeted":
    if args.outtype == "alpha-numeric":
        for address in macaddyFile:
            convertedAddress = convertMacAddressToAlphaNumeric(address)
            macaddyOutput.write(convertedAddress + "\n")
    elif args.outtype == "hyphen-delimeted":
        for address in macaddyFile:
            convertedAddress = convertMacAddressToHyphenDelimeted(address)
            macaddyOutput.write(convertedAddress + "\n")
    elif args.outtype == "cisco":
        for address in macaddyFile:
            convertedAddress = convertMacAddressToCisco(address)
            macaddyOutput.write(convertedAddress + "\n")
    else:
        print("Cannot convert mac-address to same type!")
        exit(1)
elif args.intype == "hyphen-delimeted":
    if args.outtype == "alpha-numeric":
        for address in macaddyFile:
            convertedAddress = convertMacAddressToAlphaNumeric(address)
            macaddyOutput.write(convertedAddress + "\n")
    elif args.outtype == "colon-delimeted":
        for address in macaddyFile:
            convertedAddress = convertMacAddressToColonDelimeted(address)
            macaddyOutput.write(convertedAddress + "\n")
    elif args.outtype == "cisco":
        for address in macaddyFile:
            convertedAddress = convertMacAddressToCisco(address)
            macaddyOutput.write(convertedAddress + "\n")
    else:
        print("Cannot convert mac-address to same type!")
        exit(1)
elif args.intype == "cisco":
    if args.outtype == "alpha-numeric":
        for address in macaddyFile:
            convertedAddress = convertMacAddressToAlphaNumeric(address)
            macaddyOutput.write(convertedAddress + "\n")
    elif args.outtype == "hyphen-delimeted":
        for address in macaddyFile:
            convertedAddress = convertMacAddressToHyphenDelimeted(address)
            macaddyOutput.write(convertedAddress + "\n")
    elif args.outtype == "colon-delimeted":
        for address in macaddyFile:
            convertedAddress = convertMacAddressToColonDelimeted(address)
            macaddyOutput.write(convertedAddress + "\n")
    else:
        print("Cannot convert mac-address to same type!")
        exit(1)
            
                                

macaddyFile.close()
macaddyOutput.close()
