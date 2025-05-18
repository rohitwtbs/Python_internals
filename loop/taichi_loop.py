import taichi as ti
import time

ti.init(arch=ti.gpu)  # Or ti.gpu for potentially faster execution

n = 1000

# Create a Taichi field to hold a scalar value for each iteration
scalar_field = ti.field(dtype=ti.i32, shape=(n, n, n))

@ti.kernel
def taichi_nested_loops():
    for i, j, k in scalar_field:
        # Perform a simple operation (similar to the Python example)
        scalar_field[i, j, k] = i * j + k

if __name__ == "__main__":
    start_time = time.time()
    taichi_nested_loops()
    end_time = time.time()

    total_iterations = n * n * n
    print(f"Total iterations (via Taichi field): {total_iterations}")
    print(f"Execution time (Taichi): {end_time - start_time:.2f} seconds")

    # You can optionally inspect some values in the scalar_field
    # print(scalar_field[0, 0, 0])
    # print(scalar_field[500, 500, 500])
    # print(scalar_field[999, 999, 999])