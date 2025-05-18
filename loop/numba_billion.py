from numba import njit
import time

@njit
def run_loops(outer, inner):
    counter = 0
    for i in range(outer):
        for j in range(inner):
            counter += 1
    return counter

outer = 10_000
inner = 100_000

start = time.time()
result = run_loops(outer, inner)
end = time.time()

print(f"Done. Final counter: {result}")
print(f"Time taken: {end - start:.2f} seconds")
