We're given a pcap file, which we can open with Wireshark: `wireshark data.pcap`.
We need to find a password, so we should be looking for POST requests.
Packet 68 is a POST request packet and analysing it reveals this information: `user=admin&password=picoCTF{n0ts3cur3_b186631d}`.

Flag: `picoCTF{n0ts3cur3_b186631d}`
