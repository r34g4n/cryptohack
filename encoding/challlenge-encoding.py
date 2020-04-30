#!/usr/bin/python3


import sys
import json
import base64
import Crypto
from codecs import encode as rot13
from pwn import *


class DecodeClass(object):

    def __init__(self, data):
        self.key = ''
        self.value = ''
        loaded_json = json.loads(data)
        print(f"Raw received: {loaded_json}")
        self.key = loaded_json['type']
        self.value = loaded_json['encoded']

        print("Received--> %s : %s" %(self.key, self.value))

    def calling(self):
        if self.key == 'base64':
            return base64.b64decode(self.value).decode('ISO-8859-1')
        elif self.key == 'hex':
            return bytes.fromhex(self.value).decode('ISO-8859-1')
        elif self.key == 'rot13':
            return rot13(self.value, 'rot13')
        elif self.key == 'bigint':
            len_decode = len(self.value)
            x =  int(self.value, 16).to_bytes(len_decode, 'big')
            return str(x, 'UTF-8').lstrip('\x00')
        elif self.key == 'utf-8':
            return ''.join(chr(o) for o in self.value)
        else:
            print('Excuse me good Sir! I dont know what to do with the below..')
            print('%s : %s' % (self.key, self.value))
            print('Exiting...')
            sys.exit()

p = connect('socket.cryptohack.org', 13377)

for i in range(100):
    retrieve = p.recv_raw(1024)
    decoder = DecodeClass(retrieve)
    decode = decoder.calling()
    print("Decoded--> %s: %s" % (i, decode))
    decode = {
        'decoded': decode
    }
    response = json.dumps(decode)
    print(f"raw sent: {response}")
    p.send(response)
    del decoder
    

print('\n\nthe flag is:'+p.recv(1024).decode('ISO-8859-1'))