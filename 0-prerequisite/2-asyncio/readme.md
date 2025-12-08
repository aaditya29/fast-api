# Everything about AsyncIO

## 1. What AsyncIO Is

- AsyncIO = Python’s built-in library for concurrent I/O-bound tasks using `async` / `await`.
- Runs on a single thread and single process.
- Uses cooperative multitasking where tasks voluntarily use await.
- Async: While one task waits, another task runs.

## 2. Event Loop

The event loop:

- Runs all async tasks
- Knows when a task is suspended (because it hit await)
- Switches to another ready task

We start the loop with:

```python
asyncio.run(main())
```

## 3. Awaitables

Only awaitable objects can be used with await. <br>
There 3 types of awaitables:

- Coroutines
- Tasks
- Futures (low-level and rarely used directly)

## 4. Co-Routines

### 4.1 What is Co-Routine:

A coroutine is a special type of function that can pause its execution and resume later which allows other tasks to run in the meantime.
In Python coroutines are created using:

```python
async def function_name():
    ...
```

### 4.2 Coroutine vs Normal Function

#### Normal function:

- Runs from start to finish.
- Cannot be paused.
- Blocks the thread.

```python
def f():
    time.sleep(1)
    return 10
```

#### Coroutine:

- Can **pause** using `await`
- Gives control back to the event loop
- Does NOT block the thread

```python
async def f():
    await asyncio.sleep(1)
    return 10
```

When we call it:

```python
x = f()
```

We **do NOT run it** but we get a **coroutine object**.

To actually run it:

```python
await x
```

---

### 4.3 Coroutine Function vs Coroutine Object

This part is often most confusing.

#### Coroutine Function

Created with:

```python
async def fetch():
    ...
```

This is only a **definition** like a template.

#### Coroutine Object

Created when we _call_ the coroutine function:

```python
coro = fetch()
```

This coroutine object is:

- **awaitable**
- **scheduled and executed only when awaited or turned into a task**

So coroutines = _functions whose execution can be suspended and resumed by the event loop._

### 4.4 Why Coroutines Are Useful

Because they allow:

- Concurrency without threads
- Speeding up I/O-bound operations
  (API calls, DB queries, file access, network waits, sleep)
- Efficient use of single-thread event loop

### 4.5 Coroutines Run Only Inside an Event Loop\*\*

We can’t run coroutines in normal Python.

Invalid:

```python
fetch()
```

Valid:

```python
asyncio.run(fetch())
```

### 4.6 Coroutines Can Pause Themselves

Example:

```python
async def example():
    print("Before")
    await asyncio.sleep(2)   # coroutine suspends here
    print("After")
```

During the `await` the event loop:

- pauses this coroutine
- runs any other scheduled tasks
- returns when the sleep is done

This is **cooperative multitasking**.

### 4.7. Coroutines vs Tasks

Coroutines **do not** run concurrently by themselves.

To run them concurrently we wrap them in a task:

```python
task = asyncio.create_task(fetch())
```

Tasks = scheduled coroutines.

## 5. Tasks

A Task is a scheduled coroutine. If a coroutine is a “plan” then a `task` is the execution of that plan on the event loop.

### 5.1 Why Tasks Exist

Coroutines do not run concurrently on their own.<br>
If we do:

```python
await fetch(1)
await fetch(2)
```

They run sequentially.<br>
To run them concurrently we must wrap the coroutine in a Task:

```python
task1 = asyncio.create_task(fetch(1))
task2 = asyncio.create_task(fetch(2))
```

This schedules both coroutines to run on the event loop immediately enabling concurrency.

### 5.2 How to Create a Task

The function:

```python
asyncio.create_task(coro)
```

- wraps a coroutine in a Task.
- schedules it on the event loop.
- returns a Task object.

##### Example:

```python
async def fetch(n):
    await asyncio.sleep(n)
    return n

task = asyncio.create_task(fetch(1))
```

This does not wait for completion but starts running in the background.

### 5.3 How to Wait for a Task

We must `await` the task to get its result:

```python
result = await task
```

If we don’t `await` it:

- Task still run
- But our function may exit before task finishes
- Unfinished tasks get cancelled silently

### 5.4 Task Lifecycle

A Task has states:

- **PENDING:** created but not finished.
- **RUNNING:** executing coroutine.
- **SUSPENDED:** coroutine hit `await`.
- **DONE:** finished or failed.

We can inspect tasks:

```python
task.done()
task.cancelled()
```

> Important: Awaiting a Task DOES NOT mean it runs next.

Example:

```python
await task2
```

Does **not** mean “start running task2 now”.

It means:

- Pause this coroutine until task2 is done
- Event loop decides which task runs next
- Often, _task1 may finish before task2_ even if we awaited task2 first

This is the key insight:

> The event loop controls task scheduling not the programmer.

## 6. Blocking the Event Loop

If we call synchronous blocking functions inside async code we freeze the event loop.

Consider below example:

### 6.1 Version A which uses `time.sleep(param)`

```python
import asyncio
import time


async def fetch_data(param):
    print(f"Do something with {param}...")
    time.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"


async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1 = await task1
    print("Task 1 fully completed")
    result2 = await task2
    print("Task 2 fully completed")
    return [result1, result2]


t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2 - t1:.2f} seconds")
```

Here

- `time.sleep()` does NOT yield control
- the event loop cannot run any other task
- The entire event loop thread freezes for the duration of the sleep
- Task 2 cannot run until Task 1 finishes even though both were scheduled concurrently

Which results in no concurrency and behaves like synchronous code even though we used `create_task`.

### 6.2 Version B which uses `await asyncio.sleep(param)`

```python
import asyncio
import time


async def fetch_data(param):
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"


async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result2 = await task2
    print("Task 2 fully completed")
    result1 = await task1
    print("Task 1 fully completed")
    return [result1, result2]


t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2 - t1:.2f} seconds")
```

Here

- await yields control to event loop
- The coroutine is suspended
- Event loop can run other tasks while this one is waiting
- Real concurrency happens

Result:

- Task 1 sleeps 1s
- Task 2 sleeps 2s
- Both started together
