#!/usr/bin/python3
def exa(n):
    for i in range(1, n+1):
        print(i ,"= 0x"+hex(i)[2:])
exa(98)