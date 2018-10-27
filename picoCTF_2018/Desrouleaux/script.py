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
