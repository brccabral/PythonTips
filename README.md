# Python Tips

Codes from 001 to 008 are from this Raymond Hettinger lecture. It is Python 2 based, but many tips can be applied to Python 3  

## Transforming Code into Beautiful, Idiomatic Python
https://www.youtube.com/watch?v=OSGv2VnC0go  


# from mCoding https://www.youtube.com/watch?v=qUeud6DvOWI
import socket
# don't use try to close conenctions
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
    s.sendall(b'Helllo, world')
finally:
    s.close()
# use with
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b'Helllo, world')

# from mCoding https://www.youtube.com/watch?v=qUeud6DvOWI
import socket
# don't use try to close conenctions
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
    s.sendall(b'Helllo, world')
finally:
    s.close()
# use with
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b'Helllo, world')
