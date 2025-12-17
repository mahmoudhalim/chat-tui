import socket
import sys
import time
from chatui import init_windows, read_command, print_message, end_windows


def main(argv: list[str]):
    if len(argv) < 4:
        print("usage: chatclient.py <username> <host> <port>")
        return 1

    [user, url, port] = argv[1:]
    s = socket.socket()
    s.connect((url, int(port)))
    print("Connected to Server")
    s.sendall(f"Hello from {user}".encode())
    time.sleep(3)
    s.sendall(b"")
    # s.shutdown(socket.SHUT_WR)  # Graceful shutdown     instead of close
    s.close()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))


# def draw_ui():
#     pass
#
#
# init_windows()
#
# while True:
#     try:
#         command = read_command("Enter a thing> ")
#     except:
#         break
#
#     print_message(f">>> {command}")
#     continue
# end_windows()
