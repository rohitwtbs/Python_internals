import time

outer = 10_000
inner = 100_000  # 10,000 x 100,000 = 1,000,000,000

print(f"Running nested loops: {outer} x {inner} = {outer * inner:,} iterations")

start_time = time.time()

counter = 0
for i in range(outer):
    for j in range(inner):
        counter += 1  # minimal work to prevent optimization

end_time = time.time()

print(f"Done. Final counter: {counter}")
print(f"Time taken: {end_time - start_time:.2f} seconds")
