#!/usr/bin/python3


from pwn import xor # ensure to pip install pwn

# rule1 KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# rule2 KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# rule3 KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# rule4 FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5f24

KEY1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')

# consider rule2, using xor self-invese and identity properties i.e KEY2 ^ KEY1 ^ KEY1 -> KEY2

KEY2 = xor(bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'), KEY1)

# consider rule3, using xor self-invese and identity properties ie. KEY2 ^ KEY3 ^ KEY2 -> KEY3

KEY3 = xor(bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'), KEY2) 

# consider rule4 FLAG ^ KEY1 ^ KEY3 ^ KEY2 ^ KEY1 ^ KEY3 ^ KEY2

k1_x_k2 = xor(KEY1, KEY2)
k1_x_k2_x_k3 = xor(k1_x_k2, KEY3)

FLAG = xor(bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5f24'), k1_x_k2_x_k3)

print(FLAG)
