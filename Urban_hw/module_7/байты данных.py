a = 'hello' # ascii
chars = []
# буквы в число
for i in a:
    chars.append(ord(i))
print(chars) # [104, 101, 108, 108, 111]

# Числа в буквы
s = ''
for i in chars:
    s += chr(i)
print(s) # hello

print(hex(ord('h'))) # 0x68    строка в hex

bb = b'\x68'
print(type(bb))  # bytes тип
print(bb.decode())  # декодировать байты в строку