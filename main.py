import sys
from src.chatserver import run_server


def main(argv):
    if len(argv) < 2:
        print("usage: chatserver.py <port>", file=sys.stderr)
        return 1

    port = int(argv[1])
    run_server(port)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
