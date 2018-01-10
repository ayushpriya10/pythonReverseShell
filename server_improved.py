import socket

serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 6969

serversocket.bind((host, port))

serversocket.listen(1)

clientsocket, addr = serversocket.accept()
print(addr)
print("Connection Succesful.\n")

clientsocket.send(b"Connection Succesful.")

while True:

	cwd = "NOT A DIRECTORY"
	while cwd == "NOT A DIRECTORY":
		cwd = clientsocket.recv(1024).decode("utf-8")

	command = input(cwd + "~$")
	cwd = "NOT A DIRECTORY"

	if command == "quit()":
		clientsocket.send(b"quit()")
		clientsocket.close()
		break
	elif command == "":
		clientsocket.send(b"RESPOND NULL")
	else:
		clientsocket.send(command.encode("utf-8"))
