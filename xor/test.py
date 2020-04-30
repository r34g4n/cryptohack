raw = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipher_bytes = bytearray.fromhex(raw)

def repeating_key_xor(message, key):
    output = b''
    index = 0
    for byte in message:
        # XOR current byte with offset of key
        output += bytes([byte ^ key[index]])

        # Reset index
        if (index + 1) == len(key):
            index = 0
        else:
            index += 1
    return output

def match_xor(cipher_text, plain_text):
    key = b''        
    index = 0
    for byte in cipher_text:
        key += bytes([byte ^ plain_text[index]])    
        if (index + 1) == len(plain_text):
            break
        else:
            index += 1
    return key

# Retrieve partial key
print(match_xor(cipher_bytes, b"crypto{").decode("utf-8"))
# Key is myXORkey
print(repeating_key_xor(cipher_bytes, b"myXORkey").decode("utf-8"))