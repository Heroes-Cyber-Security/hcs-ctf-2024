import random

def encrypt(x, y):
    a = x & y
    b = x & ~y
    return (a << 8) | b

flag = open("flag.txt", "rb").read()
key = [random.randint(0, 255) for _ in range(len(flag))]
ciphertext = [encrypt(flag[i], key[i]) for i in range(len(flag))]

with open("output.txt", "w") as f:
    f.write(f"{ciphertext=}\n")