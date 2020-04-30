#!/usr/bin/python3

from pwn import xor # check the bottom function for usage of this module


hex_string = bytearray.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
hex_string2 = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

known_plain_text = 'crypto{'


def determine_key(cipher_text : bytearray, plain_text : str):

    key = ''
    for i in range(len(plain_text)):
        key += chr(cipher_text[i] ^ ord(plain_text[i]))
    return key


def get_flag(encrypted_msg : bytearray, key):
    
    flag = ''
    key_length = len(key)
    for i in range(len(encrypted_msg)):
        # i%key_length helps avoiding out of range
        flag += chr(encrypted_msg[i] ^ ord(key[i%key_length])) 
    return flag

key = determine_key(hex_string, known_plain_text) + 'y' # based on the pattern we now now the key value.
flag = get_flag(hex_string, key)

print(flag)



# and for my other like me who prefer precise, clearer code, I got you..
# you know what to do


# key = bytes(key, 'utf-8')
# 
# flag = xor(hex_string2, key)
# print(str(flag, 'ascii'))