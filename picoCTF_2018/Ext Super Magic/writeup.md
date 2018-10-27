We are given what seems to be an image file, judging by the file extension. So I checked it using the `file` command:
```console
$ file ext-super-magic.img 
ext-super-magic.img: data
```
For some reason, the file is not being recognised as any particular format.
The name of this challenge _Ext Super Magic_ is a hint that it might have something to do with the magic number of an ext filesystem.
After some research, I found that the bytes at offset 0x438 and 0x439 from the beginning of the file should be `0x53` and `0xFF` respectively.
Opening the file with a hex editor (e.g. `bless`) shows that the magic number is missing, so we add those bytes in.

Now `file` gives this output:
```console
$ file ext-super-magic.img 
ext-super-magic.img: Linux rev 1.0 ext2 filesystem data, UUID=aa043d2f-4828-4073-8dfe-f13acc388fdc (large files)
``` 
Since it is recognised as an ext2 filesystem image, we can mount it. The image contains a list of JPEG files.
One of those images contains the flag:
![flag](images/flag.jpg)

Flag: `picoCTF{a7DB29eCf7dB9960f0A19Fdde9d00Af0}`
