We are provided a JSON file called `incidents.json`, which contains some network data. 
When we connect to the socket using: `nc 2018shell3.picoctf.com 40952`, it asks: `What is the most common source IP address? If there is more than one IP address that is the most common, you may give any of the most common ones.`.
This can be solved programatically by connecting to the socket using Python, loading the JSON file in the Python program, calculating the most common source IP, and sending the answer back through the connection.

Once the answer is provided, a second questions is asked: `How many unique destination IP addresses were targeted by the source IP address XXX.XXX.XXX.XXX?`, where the IP address will be randomly selected.
As a result, the data received from the connection will need to be parsed so that the answer can be dynamically computed.

The final question will be: `What is the number of unique destination ips a file is sent, on average? Needs to be correct to 2 decimal places.`.
Again, this can be solved programatically. Giving the answer will provide the flag.

This is the script I used:
```
from pwn import *
import json

# Return the most common source IP
def most_common_source_ip(data):
	src_count= {}
	for entry in data["tickets"]:
		if entry["src_ip"] not in src_count:
			src_count[entry["src_ip"]] = 1
		else:
			src_count[entry["src_ip"]] += 1
	
	ip = ""
	ip_count = 0
	for entry in src_count:
		if src_count[entry] > ip_count:
			ip_count = src_count[entry]
			ip = entry
	return ip

# Return the number of unique destination IPs targeted by a given source IP
def unique_dest_ips(data, src_ip):
	dest_ips = []
	for entry in data["tickets"]:
		if (entry["src_ip"] == src_ip) and (entry["dst_ip"] not in dest_ips):
			dest_ips.append(entry["dst_ip"])
	return len(dest_ips)

# Return the number of unique destination IPs a file is sent to, on average. (2 decimal places)
def average_num_destinations(data):
	file_destinations = {} # key = file hash, value = list of unique destination IPs
	for entry in data["tickets"]:
		if entry["file_hash"] not in file_destinations:
			file_destinations[entry["file_hash"]] = [entry["dst_ip"]]
		elif entry["dst_ip"] not in file_destinations[entry["file_hash"]]:
			file_destinations[entry["file_hash"]].append(entry["dst_ip"])
	
	num_files = len(file_destinations)
	num_dests = 0
	for entry in file_destinations:
		num_dests += len(file_destinations[entry])
	
	return "{0:.2f}".format(float(num_dests)/float(num_files))

# Load the JSON file as a dictionary
with open("incidents.json") as f:
	data = json.load(f)

r = remote("2018shell3.picoctf.com", 40952)
r.recv()
r.sendline(most_common_source_ip(data))
src_ip = r.recv().split()[-1][:-1]
r.sendline(str(unique_dest_ips(data, src_ip)))
r.recv()
r.sendline(average_num_destinations(data))
print(r.recv())

```

Flag: `picoCTF{J4y_s0n_d3rUUUULo_b6cacd6c}`
