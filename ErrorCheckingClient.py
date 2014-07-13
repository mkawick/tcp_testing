# Echo client program
import socket
import sys

#HOST = '70.186.140.93'
HOST = 'mber.pub.playdekgames.com'    # The remote host
PORT = 9601 
s = None
print( ' Connection test utility' )
print( '@ 2014 Mickey Kawick' )
print( 'address {0}:{1}'.format( HOST, PORT ) );
print( '................................' )
print( 'Connecting...' )
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print( 'could not open socket' )
    sys.exit(1)
else:
	print( 'connection was fine' )
s.close()

print( '................................' )
print( 'execution complete...' )