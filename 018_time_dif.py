import time

start = time.time()
time.sleep(1)
end = time.time()
print(f'{end-start}')

# perf_counter() is more accurate
start = time.perf_counter()
time.sleep(1)
end = time.perf_counter()
print(f'{end=}')
print(f'{start=}')
print(f'{end-start}')