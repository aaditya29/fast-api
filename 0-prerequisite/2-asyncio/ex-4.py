import time
import asyncio
from concurrent.futures import ProcessPoolExecutor  # for CPU bound tasks


def fetch_data(param):
    print(f"Fetching data for {param}...", flush=True)
    time.sleep(param)  # Simulating a blocking I/O operation
    print(f"Data fetched for {param}", flush=True)
    return f"Data for {param}"


async def main():
    # creating threads
    # wrapping sync function to run in separate thread
    task1 = asyncio.create_task(asyncio.to_thread(fetch_data, 1))
    # wrapping sync function to run in separate thread
    task2 = asyncio.create_task(asyncio.to_thread(fetch_data, 2))
    result1 = await task1  # Awaiting first task
    print("Thread 1 completed")
    result2 = await task2  # Awaiting second task
    print("Thread 2 completed")

    # running cpu bound tasks in process pool
    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as executor:  # here we are creating pool of processes
        # running sync function in separate process
        task1 = loop.run_in_executor(executor, fetch_data, 1)
        task2 = loop.run_in_executor(executor, fetch_data, 2)

        result1 = await task1  # Awaiting first process task
        print("Process 1 completed")
        result2 = await task2  # Awaiting second process task
        print("Process 2 completed")

    return [result1, result2]

if __name__ == "__main__":
    t1 = time.perf_counter()  # Start time measurement
    results = asyncio.run(main())  # Run the main coroutine
    print("Results:", results)  # Print results
    t2 = time.perf_counter()  # End time measurement
    print(f"Completed in {t2 - t1} seconds")  # Print elapsed time
