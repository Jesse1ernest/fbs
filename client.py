import sys
import os
from urllib.request import urlopen

# each node on the network gets one hardcoded account number
accts = {'10.0.0.1':10293,
         '10.0.0.2':1293,
         '10.0.0.3':13333,
         '10.0.0.4':7466,
         '10.0.0.5':4137,
         'localhost':19001}

# server_host = '10.0.0.5:9999'
server_host = 'http://127.0.0.1:9999'

# f = os.popen('ifconfig eth0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
# ip = f.read()[:-1]
# f.close()

ip = '10.0.0.1'

def main(args):
    if len(args) != 3:
        print("Usage: client.py <destination address> <amount>")
        return
    dest = args[1]
    amt = args[2]
    data = bytes("src="+str(accts[ip]) + "&dest="+str(accts[dest]) + "&amt="+amt, "ASCII")
    response = urlopen(server_host, data)
    pass

if __name__ == "__main__":
    main(sys.argv)
