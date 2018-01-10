import socket

s = socket.socket()
print("Socket successfully created")

port = 12345

s.bind(('', port))
print("socket binded to " + str(port))

s.listen(5)
print("socket is listening")

while True:
   c, addr = s.accept()
   print(addr)
   print(c)

   c.send(b'Thank you for connecting')
   c.close()
