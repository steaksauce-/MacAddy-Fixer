# MacAddy-Fixer
This is a simple python script that accepts an input file of mac addresses in the form of 00AABBCCDDEE and provides an output with colons (00:AA:BB:CC:DD:EE). Useful in many network administration tasks, such as adding mac-addresses to whitelists after scanning them.

## Usage
`macaddy-fixer.py <macaddress-file> <output-file>`

Sample mac-address file:
```
40AAD752405B
FA0944B25F17
76AD4DEC87C9
7E7FA74ED165
C86D8102AA10
67B06A947A50
```

Sample output file:
```
40:AA:D7:52:40:5B
FA:09:44:B2:5F:17
76:AD:4D:EC:87:C9
7E:7F:A7:4E:D1:65
C8:6D:81:02:AA:10
67:B0:6A:94:7A:50
```

## Usecase and inspiration for the script
While scanning the mac-addresses for a large deployment of Aruba Remote APs, I found the the mac-addresses were missing the colons. Unfortunately, to whitelist the APs in the Aruba controller, I needed to have the mac-address with the colons. I took the script a step further and made the output be the list of commands to whitelist each mac-address in the controller. This can be seen in `aruba-usecase.py`.
