# Pipeline

# Etapa 1 (stage1) multiplica por 2, luego pasa al queue.
# Etapa 2 (stage2) añade 10 a cada valor.

import time
import queue
import threading

def stage1(input_data, q):
    for item in input_data:
        result = item * 2
        q.put(result)
        time.sleep(0.1)
    q.put(None)  # sentinel

def stage2(q):
    while True:
        val = q.get()
        if val is None:  # sentinel indica fin
            break
        processed = val + 10
        print(f"Resultado pipeline: {processed}")

if __name__ == '__main__':
    q = queue.Queue()
    data = [1, 2, 3, 4, 5]

    t1 = threading.Thread(target=stage1, args=(data, q))
    t2 = threading.Thread(target=stage2, args=(q,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Fin del pipeline en Python")
