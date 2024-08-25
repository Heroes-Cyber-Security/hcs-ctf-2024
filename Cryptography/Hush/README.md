# Hush (easy/medium)

## Author
idzoyy

## Deskripsi
Mari belajar "hash"

Suatu algoritma untuk mengonversi data sesuai format tertentu, yang tidak bisa dikembalikan ke data aslinya.
data yang sama seharusnya memiliki hasil hash yang sama, dan data yang berbeda meskipun 1 byte seharusnya memiliki hasil hash yang berbeda.
fungsi :
1. mengamankan data tersimpan dengan format yang tidak bisa dibaca i.e "password"
2. sebagai signature integritas suatu file/data
3. dll

## Writeup
mencari hash dari acakan data yang akan menjadi flag 

mengetahui acakan data yang benar dengan mengcompare dengan hash yang diberikan

flag: HCS{c5d87a505f8a5590a6ccf659dc8014e}

## Solver script

```
import itertools
flag = ['dc80', '5590', '5f8a', '14e}', 'a6cc', 'c5d8', 'HCS{', 'f659', '7a50']
permutations = itertools.permutations(flag)
for perm in permutations:
     if ''.join(perm).startswith('HCS{'):
         if md5(''.join(perm).encode()).hexdigest() == '83106e2e86716463f5d7e6363473559c':
             print(''.join(perm))
```
