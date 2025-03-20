import time
import queue 
import threading

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

def list_primes(high, q = None):
    primes = []

    for i in range(high):
        if is_prime(i):
            primes.append(i)

    if q is not None:
        q.put(primes)

    return primes

if __name__ == '__main__':
    t_start = time.time()

    # primes = list_primes()
    thr_q = queue.Queue()

    thr = threading.Thread(target=list_primes, args=[1000, thr_q], daemon=True)
    thr_q.put(thr)

    thr.start()
    thr.join()

    primes = thr_q.get()

    t_end = time.time()
    
    print(*primes)
    print("Time completed ", t_end - t_start)
