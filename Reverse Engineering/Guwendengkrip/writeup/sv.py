from pwn import xor
open('decrypt.jpg','wb').write(xor(open('output.guwendeng','rb').read(),120))
