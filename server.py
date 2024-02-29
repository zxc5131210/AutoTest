import socket
import logging
import ci_script
import threading
from datetime import datetime, timedelta

import config

# Flag to indicate whether the CI process is running
ci_process_running = False


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

        latest_client_time = None

        while True:
            # waiting for a connection
            logging.info("Waiting for a connection...")

            # Check if CI process is running, if not, accept new clients
            if not ci_process_running:
                client_socket, client_address = server_socket.accept()
                try:
                    # get the client data
                    data = client_socket.recv(1024)
                    if data.decode():
                        latest_client_time = datetime.now()
                        logging.info(
                            f"Received data from client at {latest_client_time}"
                        )
                except Exception as e:
                    logging.error(f"Error processing client data: {e}")
                finally:
                    # close client
                    client_socket.close()

                # Check if the latest client and if it's time to run CI script
                if latest_client_time:
                    delay_time = (
                        latest_client_time
                        + timedelta(minutes=config.waiting_minutes)
                        - datetime.now()
                    )
                    if delay_time.total_seconds() > 0:
                        logging.info(
                            f"Scheduling CI script to run in {delay_time.total_seconds()} seconds"
                        )
                        schedule_ci_script(delay_time.total_seconds())

    except Exception as e:
        logging.error(f"Error in server: {e}")
    finally:
        server_socket.close()


def delayed_ci_script():
    global ci_process_running
    logging.info("Executing CI script...")
    ci_process_running = True
    start_ci_process()
    ci_process_running = False


def schedule_ci_script(delay_seconds):
    threading.Timer(delay_seconds, delayed_ci_script).start()


def start_ci_process():
    ci_script.main_script()


if __name__ == "__main__":
    start_server()
