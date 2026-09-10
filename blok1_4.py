#Вычисление факториала числа с использованием потоков
import threading
import math

def calculate_factorial(n):
    result = math.factorial(n)
    print(f"Factorial of {n}: {result}")

numbers = [5, 10, 15]

threads = []

for num in numbers:
    thread = threading.Thread(target=calculate_factorial, args=(num,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()