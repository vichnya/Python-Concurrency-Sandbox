#Программа с двумя потоками сервера и клиента, используя threading.Barrier

import threading
import time

def server(barrier):
    print("Server: Initializing...")
    time.sleep(2) 
    print("Server: Initialization complete.")
    barrier.wait()
    print("Server: Handling requests...")

def client(barrier):
    print("Client: Waiting for server to initialize...")
    barrier.wait()
    print("Client: Sending request to server...")


barrier = threading.Barrier(2)  

server_thread = threading.Thread(target=server, args=(barrier,))
client_thread = threading.Thread(target=client, args=(barrier,))

server_thread.start()
client_thread.start()

server_thread.join()
client_thread.join()
