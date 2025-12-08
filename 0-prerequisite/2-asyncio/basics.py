import time
import asyncio


def sync_function(test_param: str) -> str:
    print("This is synchronous function")
    time.sleep(2)
    # here we simulate a blocking operation
    return f"Sync function received: {test_param}"


# we define an asynchronous function using the 'async def' syntax
# this function can use 'await' to pause its execution until the awaited task is complete
async def async_function(test_param: str) -> str:  # coroutine function
    print("This is asynchronous function")
    await asyncio.sleep(2)  # here we simulate a non-blocking operation
    # here we simulate a non-blocking operation
    return f"Async function received: {test_param}"


# we define another asynchronous function to demonstrate calling the synchronous function
async def main():
    sync_result = sync_function("Hello Sync")  # calling sync function
    print(sync_result)  # printing result of sync function

if __name__ == "__main__":
    asyncio.run(main())
