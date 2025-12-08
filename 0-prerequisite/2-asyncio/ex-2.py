import asyncio
import time


async def fetch_data(param):
    print(f"Fetching data with {param}")
    await asyncio.sleep(param)  # Simulating a non-blocking I/O operation
    print(f"Data fetched with {param}")
    return f"Data for {param}"


async def main():
    task1 = fetch_data(1)  # Create coroutine for first fetch
    task2 = fetch_data(2)  # Create coroutine for second fetch
    result1 = await task1  # Await first fetch
    print("Fetch 1 complete:", result1)
    result2 = await task2  # Await second fetch
    print("Fetch 2 complete:", result2)
    return [result1, result2]

t1 = time.perf_counter()  # Start time measurement
results = asyncio.run(main())  # Run the main coroutine
print("Results:", results)  # Print results
t2 = time.perf_counter()  # End time measurement
print(f"Completed in {t2 - t1} seconds")  # Print elapsed time
