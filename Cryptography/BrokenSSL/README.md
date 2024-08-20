# BrokenSSL (Medium)

## Author
idzoyy

## Deskripsi
aku mengenkripsi file menggunakan openssl dengan RSA 2048 bit. Tetapi pas mau decrypt, private key nya kenapa seperti kesensor gitu ya?

## Writeup
analisa structure pem private key yang utuh (generate 2048 bit), compare dengan yang broken

private key yang broken sebenarnya berisi n, d, dan e

decrypt dengan algoritma RSA biasa
