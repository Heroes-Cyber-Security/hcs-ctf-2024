# Rusak (Easy/Medium)

## Author
daffainfo

## Deskripsi
Dikasih file dari temen eh malah gabisa dibuka, kira-kira kenapa yak?

## Writeup
Jika dilihat dari header filenya, `broken_flag` adalah file dengan ekstensi PNG dan setiap 2 bytes nya di flip. Hal itu bisa diketahui dari "header" file broken_flag yang terlihat seperti ini

```bash
$ hexdump -C broken_flag 
00000000  50 89 47 4e 0a 0d 0a 1a  00 00 0d 00 48 49 52 44  |P.GN........HIRD|
...
```

Jika kita lihat secara seksama, terdapat kumpulan karakter P, N, dan G pada header file yang jika kita cek pada website [ini](https://en.wikipedia.org/wiki/List_of_file_signatures) maka kemungkinan paling besar ini adalah file png

Kemudian, buat script untuk merecover flagnya dengan melakukkan flipping tiap 2 bytes yang script solvernya akan terlihat seperti ini

```python
def reverse_flip_bytes(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        data = f_in.read()
        
    reversed_data = bytearray()
    for i in range(0, len(data), 2):
        if i + 1 < len(data):
            reversed_data.append(data[i + 1])
        reversed_data.append(data[i])

    with open(output_file, 'wb') as f:
        f.write(reversed_data)

# Example:
input_file = 'broken_flag'
output_file = 'flag.png'
reverse_flip_bytes(input_file, output_file)
```

Jalankan solvernya, dan buka file flag.png untuk melihat flagnya

![flag](flag.png)