#!/usr/bin/python3


import base64

x = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

x = bytes.fromhex(x)
print(base64.b64encode(x))