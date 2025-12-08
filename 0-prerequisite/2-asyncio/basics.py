import time


def sync_function(test_param: str) -> str:
    print("This is synchronous function")
    time.sleep(0.2)
    # here we simulate a blocking operation
    return f"Sync function received: {test_param}"
