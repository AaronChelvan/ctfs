We have an image and the description for this problem: `Can you help us find the flag in this Meta-Material?` implies that we should look at the metadata for the image. `exiftool` is a tool that allows us to do this. Running `exiftool 2018.jpg` gives this output:
```
ExifTool Version Number         : 10.10
File Name                       : 2018.png
Directory                       : .
File Size                       : 13 kB
File Modification Date/Time     : 2018:10:27 19:30:19+11:00
File Access Date/Time           : 2018:10:27 19:31:24+11:00
File Inode Change Date/Time     : 2018:10:27 19:30:46+11:00
File Permissions                : rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1200
Image Height                    : 630
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Artist                          : picoCTF{look_in_image_9f5be995}
Image Size                      : 1200x630
Megapixels                      : 0.756
```
We can see that the `Artist` tag contains the flag.

Flag: `picoCTF{look_in_image_9f5be995}`
