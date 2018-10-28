We are given a file named `husky.png`. 
We can verify that it is actually a PNG file:
```console
$ file husky.png
husky.png: PNG image data, 2140 x 2232, 8-bit/color RGBA, non-interlaced
```
The questions says: `Stego-Saurus hid a message for you in this image, can you retreive it?`, implying that this is a steganography challenge.
A common steganography technique used to hide messages within images is LSB.
`zsteg` is a tool capable of finding messages hidden within images using the LSB technique.
This was my output when running it:
```console
$ zsteg husky.png
b1,r,lsb,xy         .. text: "^5>c[rvyzrf@"
b1,rgb,lsb,xy       .. text: "picoCTF{r34d1ng_b37w33n_7h3_by73s}"
b1,abgr,msb,xy      .. file: PGP\011Secret Sub-key -
b2,g,msb,xy         .. text: "ADTU@PEPA"
b2,rgb,lsb,xy       .. file: PGP\011Secret Sub-key -
b3,abgr,msb,xy      .. text: "t@Wv!Wt\tGtA"
b4,r,msb,xy         .. text: "0Tt7F3Saf"
b4,g,msb,xy         .. text: "2g'uV `3"
b4,b,lsb,xy         .. text: "##3\"TC%\"2f"
b4,b,msb,xy         .. text: " uvb&b@f!"
b4,rgb,lsb,xy       .. text: "1C5\"RdWD"
b4,rgb,msb,xy       .. text: "T E2d##B#VuQ`"
b4,bgr,lsb,xy       .. text: "A%2RTdGG"
b4,bgr,msb,xy       .. text: "EPD%4\"c\"#CUVqa "
b4,rgba,lsb,xy      .. text: "?5/%/d_tO"
b4,abgr,msb,xy      .. text: "EO%O#/c/2/C_e_q"
```
This reveals the flag.

Flag: `picoCTF{r34d1ng_b37w33n_7h3_by73s}`

