import sys
import tracemalloc
import psutil
import os
import time

def swap_case(s):
    return_string = ""
    for i in s:
        if(i.islower()):
            c = i.upper()
        else:
            c = i.lower()
        # print(i.casefold())
        return_string = return_string + c
    return return_string

def swap_case_optimized(s):
    """More memory-efficient version using list comprehension"""
    return ''.join(c.upper() if c.islower() else c.lower() for c in s)

def get_process_memory():
    """Get current process memory usage in MB"""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024

def profile_function(func, test_string, func_name):
    """Profile a function's memory usage"""
    print(f"\n--- Profiling {func_name} ---")
    
    # Start memory tracing
    tracemalloc.start()
    initial_memory = get_process_memory()
    
    # Take initial snapshot
    snapshot_before = tracemalloc.take_snapshot()
    
    # Execute function
    start_time = time.time()
    result = func(test_string)
    end_time = time.time()
    
    # Take final snapshot
    snapshot_after = tracemalloc.take_snapshot()
    final_memory = get_process_memory()
    
    # Analyze memory usage
    top_stats = snapshot_after.compare_to(snapshot_before, 'lineno')
    
    print(f"Execution time: {(end_time - start_time) * 1000:.2f} ms")
    print(f"Memory before: {initial_memory:.2f} MB")
    print(f"Memory after: {final_memory:.2f} MB")
    print(f"Memory difference: {final_memory - initial_memory:.2f} MB")
    
    print("\nTop memory allocations:")
    for i, stat in enumerate(top_stats[:3]):
        print(f"{i+1}. {stat}")
    
    tracemalloc.stop()
    return result

def run_memory_comparison():
    """Compare memory usage between original and optimized versions"""
    test_cases = [
        ("Small string", "Hello World!" * 10),
        ("Medium string", "Hello World!" * 100),
        ("Large string", "Hello World!" * 1000),
        ("Very large string", "Hello World!" * 5000)
    ]
    
    print("=" * 60)
    print("MEMORY PROFILING COMPARISON")
    print("=" * 60)
    
    for test_name, test_string in test_cases:
        print(f"\n{'='*20} {test_name} ({'Length: ' + str(len(test_string))}) {'='*20}")
        
        # Profile original function
        result1 = profile_function(swap_case, test_string, "Original swap_case")
        
        # Small delay to separate measurements
        time.sleep(0.1)
        
        # Profile optimized function
        result2 = profile_function(swap_case_optimized, test_string, "Optimized swap_case")
        
        # Verify results match
        print(f"\nResults match: {result1 == result2}")
        print("-" * 80)

def interactive_mode():
    """Run in interactive mode with memory profiling"""
    print("Enter a string to swap case (with memory profiling):")
    s = input()
    
    print("\nRunning with memory profiling...")
    result = profile_function(swap_case, s, "swap_case")
    print(f"\nResult: {result}")

if __name__ == '__main__':
    try:
        # Check if psutil is available
        import psutil
    except ImportError:
        print("Installing required packages...")
        os.system("pip install psutil")
        import psutil
    
    if len(sys.argv) > 1 and sys.argv[1] == 'profile':
        # Run memory comparison
        run_memory_comparison()
    else:
        # Run interactive mode
        interactive_mode()