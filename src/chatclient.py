import socket
import sys
import threading
from chatui import init_windows, read_command, print_message, end_windows


s = socket.socket()


def receive_message():
    init_windows()
    while True:
        message = s.recv(512).decode()
        print_message(message.rstrip("\n"))


def main(argv: list[str]):
    if len(argv) < 4:
        print("usage: chatclient.py <username> <host> <port>")
        return 1

    [user, url, port] = argv[1:]
    s.connect((url, int(port)))
    print("Connected to Server")

    # recieving thread
    t = threading.Thread(target=receive_message, daemon=True)
    t.start()

    # main thread loop
    while True:
        message = read_command()
        s.sendall(message.encode())


if __name__ == "__main__":
    sys.exit(main(sys.argv))
