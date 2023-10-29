cal = 0
c1 = 460


encrypt_dict = {}
for i in range(32):
    cal += 1
    encrypt_dict[cal] = chr(c1+cal)
print(encrypt_dict)