from collections import deque
import queue
import threading
import time

class OrderQueue:
    def __init__(self):
        self.queue = deque()
        self.lock = threading.Lock()

    def place_order(self, order):
        with self.lock:
            time.sleep(0.5)  # Simulate time taken to place orders
            self.queue.appendleft(order)

    def serve_order(self):
        with self.lock:
            if self.queue:
                time.sleep(2)  # Simulate time taken to serve orders
                current_order = self.queue.pop()  # Simulate time taken to serve orders
                print(f"Serving order: {current_order}")
            else:
                print("No orders to serve.")


q=OrderQueue()
t1=threading.Thread(target=q.place_order, args=("Order 1",))
t2=threading.Thread(target=q.place_order, args=("Order 2",)) 
t3=threading.Thread(target=q.place_order, args=("Order 3",))
t4=threading.Thread(target=q.serve_order, args=())   
t5=threading.Thread(target=q.serve_order, args=())
t6=threading.Thread(target=q.serve_order, args=())

t1.start()
t2.start()
t3.start()
time.sleep(1)  # Ensure orders are placed before serving
t4.start()
t5.start()
t6.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()