#!/bin/python3

# Running the application
# python3 portscanner.py <ip>

#
import sys
from datetime import datetime as dt
import socket as ss

if len(sys.argv) == 2:
    target = ss.gethostbyname(sys.argv[1]) #Translating hostname t IPv4
else:
    print('Invalid args')

print("-" * 50)
print("Scanning target {}".format(target))
print("Time started {}".format(dt.now()))

# 1, 65535

try:
    for port in range(50, 85):
        print("Scanning " + target + ":" + str(port))
        s = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
        ss.setdefaulttimeout(1)
        res = s.connect_ex((target, port)) #ex returns an error indicator if a port is open it returns a 0 else returns an error = 1
        if res == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nInterruption, exiting")
    sys.exit()

except ss.gaierror:
    print("Hostname {} could not be resolved".format(target))
    sys.exit()

except ss.error:
    print("Couldn't connect")
    sys.exit()
