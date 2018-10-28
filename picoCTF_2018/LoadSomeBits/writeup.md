We have an image file, and the hints for this challenge are:
* `Look through the Least Significant Bits for the image`
* `If you interpret a binary sequence (seq) as ascii and then try interpreting the same binary sequence from an offset of 1 (seq[1:]) as ascii do you get something similar or completely different?`

We can write a script that will extract all of the LSBs from the image, create an ASCII string from those bits, and repeat this process at varying offsets until we get the flag.
This is the Python script I used:
```python
# Read in the image file data
with open ("pico2018-special-logo.bmp") as f:
	data = f.read()

offset_size = 0
while True:
	# Offset the data
	offset_data = data[offset_size:]
	
	# Create a string of the least significant bits
	bit_string = ""
	for i in offset_data:
		bit_string += str(ord(i) & 0x1)
	
	# Convert the bit string to a byte string
	byte_string = ""
	for i in range(0, len(bit_string), 8):
		byte_string += chr(int(bit_string[i:i+8], 2))
	
	# If the byte string contains the flag, print the string, and break out of the loop
	if "picoCTF" in byte_string:
		print(byte_string)
		break
	else: # Otherwise, increase the offset size and try again
		offset_size += 1
```

The output of this script contains the flag.

Flag: `picoCTF{st0r3d_iN_tH3_l345t_s1gn1f1c4nT_b1t5_770554193}`
