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
    # sync_result = sync_function("Hello Sync")  # calling sync function
    # print(sync_result)  # printing result of sync function
    # calling async function returns a coroutine object
    coroutine_obj = async_function("Hello Async")
    print(coroutine_obj)  # printing coroutine object

    # awaiting the coroutine to get the result
    coroutine_result = await coroutine_obj
    print(coroutine_result)  # printing result of async function

    # creating a task to run the async function concurrently
    task = asyncio.create_task(async_function("Hello from Task"))
    print(f"Task created: {task}")  # printing the task object

    task_result = await task  # awaiting the task to get the result
    print(f"Task result: {task_result}")  # printing the result of the task


if __name__ == "__main__":
    asyncio.run(main())
