# gifff

## Author

rootkids

## Deskripsi

giffff? color? color in giff?? whatever, I can't see it clearly, please help me!

## Writeup

Untuk challenge kali ini jadi diberikan sebuah file gif, dimana isinya adalah sebuah gif yang berisi warna - warna random didalamnya.

Nah untuk menyelesaikan disini kita harus barasumsi bahwa sebuah warna itu bisa di representasikan dalam bentuk hex, dan kita bisa mengambil warna tersebut dari setiap frame yang ada di gif tersebut.

Dan representasi warna yang ada dalam gif tersebut sebenarnya adalah susunan hex value dari flag yang dicari.

Untuk cara menyelesaikannya berikut beberapa langkahnya:

1. Membaca file gif
2. Mengambil setiap frame dari gif tersebut
3. Mengambil sample pixel, dan mengambil warna RGB dari pixel tersebut
4. Mengubah warna RGB tersebut menjadi hex
5. Menggabungkan semua hex yang didapat dari setiap frame
6. Melakukan decode hex tersebut

Untuk automasi proses tersebut sudah ada di file [solver.py](./src/solver.py)

## Flag

HCS{3xtr4ct_fr4m3_bY_fR4m3_th3n_extr4ct_th3_c0l04_a5_h3x_I5_4_g00d_w4y}
