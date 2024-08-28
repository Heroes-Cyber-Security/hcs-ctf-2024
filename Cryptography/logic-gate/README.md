# Logic Gate (easy)

## Author
ryuk

## Deskripsi
Decrypt ciphertext untuk mendapatkan flag

## Writeup

```python
ciphertext=[16392, 16897, 20993, 10323, 27136, 8532, 370, 5216, 17945, 4200, 9546, 4194, 20240, 18465, 29696, 27665]
flag = b""
for i in ciphertext:
    b = i & 0xff
    a = i >> 8
    flag += bytes([a ^ b])
print(flag)
```

## Flag
HCS{just_xor_it}
