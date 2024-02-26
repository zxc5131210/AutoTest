import socket
import logging
import ci_script


def start_server():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)-2s %(message)s",
        datefmt="%Y%m%d %H:%M:%S",
    )

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # bind ip address and port
        server_address = ("", 12345)
        server_socket.bind(server_address)

        # start listening
        server_socket.listen(1)

        while True:
            # waiting for a connection
            logging.info("Waiting for a connection...")
            client_socket, client_address = server_socket.accept()
            try:
                # get the client data
                data = client_socket.recv(1024)
                if data.decode():
                    start_ci_process()
            except Exception as e:
                logging.error(f"Error processing client data: {e}")
            finally:
                # close client
                client_socket.close()

    except Exception as e:
        logging.error(f"Error in server: {e}")
    finally:
        server_socket.close()


def start_ci_process():
    ci_script.main_script()


if __name__ == "__main__":
    start_server()
