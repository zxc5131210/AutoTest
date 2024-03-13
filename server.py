import socket
import logging
import time
import threading
from queue import Queue

import ci_script
import config


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

        # Create a queue to store incoming client information
        client_info_queue = Queue()

        # Create a flag to indicate if a delay is in progress
        delay_in_progress = False

        def process_client_info():
            nonlocal delay_in_progress
            while True:
                # Wait for client information
                client_info = client_info_queue.get()

                # If there's no delay in progress, start one with the CI process
                if not delay_in_progress:
                    delay_in_progress = True
                    logging.info(
                        "Received client information. Starting 30-minute delay..."
                    )
                    threading.Timer(
                        config.waiting_minutes * 60, lambda: run_ci_process(client_info)
                    ).start()  # Schedule CI after 30 minutes

                # If a delay is in progress, reset the timer and update CI information
                else:
                    logging.info(
                        "Received new client information during delay. Resetting timer."
                    )
                    delay_in_progress = False  # Cancel previous delay
                    client_info_queue.put(
                        client_info
                    )  # Put new info back in queue for processing

        # Start a separate thread for processing client information
        client_info_thread = threading.Thread(target=process_client_info)
        client_info_thread.daemon = True  # Set as daemon to avoid blocking program exit
        client_info_thread.start()

        while True:
            # Wait for a connection
            logging.info("Waiting for a connection...")
            client_socket, client_address = server_socket.accept()
            try:
                # Get the client data
                data = client_socket.recv(1024)
                if data.decode():
                    # Put received data in the queue for processing
                    client_info_queue.put(data.decode())
            except Exception as e:
                logging.error(f"Error processing client data: {e}")
            finally:
                # Close client socket
                client_socket.close()

    except Exception as e:
        logging.error(f"Error in server: {e}")
    finally:
        server_socket.close()


def run_ci_process(client_info):
    # Access and process the client information (replace with actual logic)
    logging.info(f"Running CI process with client information: {client_info}")
    ci_script.main_script()  # Pass client information to CI script


if __name__ == "__main__":
    start_server()
