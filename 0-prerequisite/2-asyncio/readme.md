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

# **8. Coroutines Are Similar to Generators**

But with more capabilities:

- Coroutines use `await`
- Generators use `yield`
- Coroutines integrate with event loop
- Coroutines can await I/O and resume when ready
