# Python - Async Programming

## Introduction

Asynchronous programming in Python allows the execution of tasks concurrently without blocking the main thread. It is particularly useful for operations that involve I/O, such as file operations, database interactions, or making HTTP requests.

This guide explores **asyncio**, the main module for asynchronous programming in Python, and provides a comprehensive overview of coroutines and asynchronous tasks.

---

## Key Concepts

### Coroutines
- Coroutines are the building blocks of asynchronous programming.
- Declared using the `async def` keyword.
- Can pause and resume execution using `await`.

## Example:  
      async def say_hello():print("Hello, Async!")  

## Available Functions and Features

### 1. `asyncio.run`  
The main entry point for running asynchronous code.  

    async def example():  
      print("Asyncio Run Example")  

asyncio.run(example())  

### 2. `asyncio.sleep`  
  Suspends execution for a given amount of time.  

    await asyncio.sleep(2)  # Pause for 2 seconds  

### 3. `asyncio.create_task`  
Schedules a coroutine to run as a concurrent task.  

    task = asyncio.create_task(coroutine())  

### 4. `asyncio.gather`  
Executes multiple coroutines concurrently.  


    async def main():  
    await asyncio.gather(task1(), task2())  

### 5. asyncio.wait  
Waits for a set of tasks to complete.  

    done, pending = await asyncio.wait([task1, task2])  

### 6. asyncio.run_in_executor  
Executes blocking code in a separate thread or process.  

    def blocking_operation():
        print("Blocking operation")

    async def main():  
        loop = asyncio.get_event_loop()  
        await loop.run_in_executor(None, blocking_operation)  

### 7. asyncio.Queue  
Asynchronous FIFO queue for inter-task communication.  

    queue = asyncio.Queue()

    async def producer():
        await queue.put("Produced item")

    async def consumer():
        item = await queue.get()
        print(item)  

### 8. asyncio.TimeoutError  
Handles execution timeouts.  

    async def main():
        try:
            await asyncio.wait_for(asyncio.sleep(5), timeout=3)
        except asyncio.TimeoutError:
            print("Operation timed out")

    asyncio.run(main())

### 9. asyncio.Semaphore  
Limits the number of concurrent tasks.  

    semaphore = asyncio.Semaphore(2)

    async def limited_task():
        async with semaphore:
            await asyncio.sleep(1)  

### 10. asyncio.Event  
Synchronizes tasks.  

    event = asyncio.Event()

    async def waiter():
        await event.wait()

    async def setter():
        event.set()  

### 11. asyncio.Condition  
Manages shared resources with conditions.  

    condition = asyncio.Condition()

    async def writer():
        async with condition:
            print("Resource updated")
            condition.notify_all()
