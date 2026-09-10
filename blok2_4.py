#Программа для записи и чтения данных из файла с использованием объектов типа Future

import concurrent.futures

def write_to_file(filename, data, future):
    with open(filename, 'w') as file:
        file.write(data)
    future.set_result(f"Data written to {filename}")

def read_from_file(filename, future):
    with open(filename, 'r') as file:
        data = file.read()
    future.set_result(data)


filename = "example.txt"
data_to_write = "Hello, this is some data for the file."

with concurrent.futures.ThreadPoolExecutor() as executor:
    write_future = concurrent.futures.Future()
    read_future = concurrent.futures.Future()

    write_thread = executor.submit(write_to_file, filename, data_to_write, write_future)
    read_thread = executor.submit(read_from_file, filename, read_future)

    # Wait for write and read to complete
    concurrent.futures.wait([write_future, read_future], return_when=concurrent.futures.ALL_COMPLETED)

    print(write_future.result())
    print(read_future.result())