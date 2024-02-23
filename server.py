import socket
import ci_script


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # blind ip address and port
    server_address = ("", 12345)
    server_socket.bind(server_address)

    # start listen
    server_socket.listen(1)

    while True:
        # waiting for client
        print("Waiting for a connection...")
        client_socket, client_address = server_socket.accept()
        # get the client data
        data = client_socket.recv(1024)
        if data.decode():
            start_ci_process()
            # close client
            client_socket.close()
            break


def start_ci_process():
    ci_script.main_script()


if __name__ == "__main__":
    start_server()
