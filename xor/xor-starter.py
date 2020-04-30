string = 'label'
xor_int = 13

value = ''.join(chr(ord(s) ^ xor_int) for s in string)

print("flag: crypto{%s}" % value)

