#Программа симуляции банка с использованием потоков и Lock
import threading
import time

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Deposited {amount} dollars. Balance: {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount} dollars. Balance: {self.balance}")
            else:
                print(f"Insufficient funds. Balance: {self.balance}")

def bank_simulation(account):
    for _ in range(5):
        account.deposit(100)
        time.sleep(0.1)

    for _ in range(5):
        account.withdraw(50)
        time.sleep(0.1)


account = BankAccount()

threads = []
for _ in range(2):
    thread = threading.Thread(target=bank_simulation, args=(account,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()