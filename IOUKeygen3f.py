#!/usr/bin/python3
print ("*******
********'')
print ("Cisco IOU License Generator Kal 2011, python port of 2006 C version")
import os
import socket
import hashlib
import struct
# get the host id and host name to calculate the hostkey
hostid=os.popen("hostid").read().strip()
hostname = socket.gethostname()
ioukey int (host id, 16)
for x in hostname:
ioukey = ioukey + ord (x)
print("hostid=" + hostid +", hostname="+ hostname + ", ioukey=" + hex(ioukey) [2:]) # create the license using md5sum
iouPad1 = b'\x4E\x58\x21\X81\x56\x7E\x0D\XF3\X21\x43\x9B\x7E\XAC\X1D\XE6\xBA' iouPad2 b'x80' + 39*b '\0'
md5input=iouPad1 + iouPad2 + struct.pack('!i', ioukey) + iouPad1 iouLicense=hashlib.md5(md5input).hexdigest() [:16]
print ("\nAdd the following text to iourc:")
||
print("[license] \n" + hostname + = " + iouLicense + ";\n") with open("iourc.txt", "wt") as out_file:
out_file.write("[license] \n" + hostname + " = " + iouLicense + ";\n") \nAlready copy to the file iourc.txt\n")
print("^
print ("You can disable the phone home feature with something like:") print(" echo '127.0.0.127 xml.cisco.com' >> /etc/hosts\n")
