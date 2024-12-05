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
    