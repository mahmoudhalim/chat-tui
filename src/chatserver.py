import socket
import select


listener_socket = socket.socket()
listener_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
read_set = {listener_socket}
connected_peers: dict[socket.socket, tuple] = {}


def run_server(port: int) -> None:
    listener_socket.bind(("", port))
    listener_socket.listen()
    print(f"Listening on PORT {port}")
    while True:
        ready, _, _ = select.select(read_set, {}, {}, None)
        for s in ready:
            if s == listener_socket:
                sock, addr = listener_socket.accept()
                read_set.add(sock)
                connected_peers[sock] = addr
                broadcast(f"{addr} Connected!\n", read_set)
            else:
                try:
                    data = s.recv(4096)
                except ConnectionResetError:
                    close_connection(s)
                    continue
                if len(data) == 0:
                    close_connection(s)
                else:
                    broadcast(
                        f"{s.getpeername()} {len(data)} bytes: {data}\n", read_set
                    )


def broadcast(message: str, sockets: set[socket.socket]) -> None:
    print(message, end="")
    for s in sockets:
        if s == listener_socket:
            continue
        s.sendall(message.encode())


def close_connection(s: socket.socket):
    peer = connected_peers[s]
    read_set.remove(s)
    s.close()
    broadcast(f"{peer} Disconnected\n", read_set)
