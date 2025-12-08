# Creating tasks
import asyncio
import time


async def fetch_data(param):
    print(f"Fetching data for {param}...")
    await asyncio.sleep(2)  # Simulating a non-blocking I/O operation
    print(f"Data fetched for {param}")
    return f"Data for {param}"


async def main():
    # Creating task for first fetch
    task1 = asyncio.create_task(fetch_data("parameter1"))
    # Creating task for second fetch
    task2 = asyncio.create_task(fetch_data("parameter2"))

    result1 = await task1  # Awaiting first task
    print("Fetch 1 complete:", result1)
    result2 = await task2  # Awaiting second task
    print("Fetch 2 complete:", result2)
    return [result1, result2]

t1 = time.perf_counter()  # Start time measurement
results = asyncio.run(main())  # Run the main coroutine
print("Results:", results)  # Print results
t2 = time.perf_counter()  # End time measurement
print(f"Completed in {t2 - t1} seconds")  # Print elapsed time
