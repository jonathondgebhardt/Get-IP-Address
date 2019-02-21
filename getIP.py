#!/usr/bin/env python3

import sys
import socket

if len(sys.argv) >= 2:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    targetIP = sys.argv[1]
    s.connect((targetIP, 80))
    print(s.getsockname()[0])

    s.close()

else:
    print("usage: ./getIP.py [target IP address]")
