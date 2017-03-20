#!/usr/bin/env python

import sys,struct

def hton(num):
    return struct.pack('!H',num)

def ntoh(num):
    return struct.unpack('!H',num)


num=raw_input("please input a number:")

num=int(num)


print repr(hton(num))

print struct.pack('i',num)
print repr(ntoh(hton(num)))
print int('0x15',16)