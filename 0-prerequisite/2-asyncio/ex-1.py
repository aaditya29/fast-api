# Doing synchronoous programming without asyncio
import time


def fetch_data(param):
    print(f"Fetching data for {param}...")
    time.sleep(2)  # Simulating a blocking I/O operation
    print(f"Data fetched for {param}")
    return f"Data for {param}"


def main():
    result = fetch_data("parameter1")  # Start time measurement
    print("Fetch 1 complete:", result)  # Start time measurement
    result2 = fetch_data("parameter2")  # Start time measurement
    print("Fetch 2 complete:", result2)  # Start time measurement
    return [result, result2]


t1 = time.perf_counter()  # Start time measurement

results = main()  # Start time measurement
print("Results:", results)  # Start time measurement

t2 = time.perf_counter()  # Start time measurement
print(f"Completed in {t2 - t1} seconds")  # Start time measurement
