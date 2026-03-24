import queue
import threading
import time

q = queue.Queue()
NUM_ITEMS = 20

def producer():
    for i in range(1, NUM_ITEMS + 1):
        q.put(i)
        print(f"[Producent] Dodałem: {i}")
        time.sleep(0.1)
    q.put(None)
    q.put(None)
    print("[Producent] Skończyłem pracę.")

def consumer(name, condition):
    while True:
        item = q.get()
        if item is None:
            print(f"[{name}] Otrzymałem sygnał końca.")
            break
        if condition(item):
            print(f"[{name}] Przetwarzam: {item}")
            time.sleep(0.30)
        else:
            q.put(item)
        q.task_done()

if __name__ == "__main__":
    t_producer = threading.Thread(target=producer)
    t_consumer1 = threading.Thread(
        target=consumer,
        args=("Konsument Parzysty", lambda x: x % 2 == 0)
    )
    t_consumer2 = threading.Thread(
        target=consumer,
        args=("Konsument Nieparzysty", lambda x: x % 2 != 0)
    )

    t_producer.start()
    t_consumer1.start()
    t_consumer2.start()

    t_producer.join()
    t_consumer1.join()
    t_consumer2.join()

    print("\nWszystkie wątki zakończyły pracę!")