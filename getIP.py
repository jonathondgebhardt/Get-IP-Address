#!/usr/bin/env python3

import sys
import socket

# If an argument IP isn't provided, use Google's DNS.
targetIP = "8.8.8.8"

if len(sys.argv) >= 2:
    targetIP = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect((targetIP, 80))
print(s.getsockname()[0])

s.close()
