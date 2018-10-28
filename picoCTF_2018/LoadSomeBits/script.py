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
