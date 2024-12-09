# 🚀 Python - Asynchronous Execution 🌟

## Introduction 🧠

Asynchronous execution in Python allows you to write **concurrent** code without the need for threads or multiple processes. It's particularly useful for I/O-bound tasks, such as web requests or database queries. Using coroutines and the `async/await` syntax, your code can perform multiple tasks simultaneously in an efficient manner. ⚡

---

## Basic Concepts 📚  

### 1️⃣ Coroutine
A coroutine is a special type of function that can **pause** its execution to allow other tasks to run. It can later resume where it left off. 🛑➡️▶️

Defined with `async`:

async def my_coroutine():
    await asyncio.sleep(1)
    print("Coroutine executed!")  


### 2️⃣ Event Loop
The event loop is the core of any asyncio application. It:

Schedules tasks. 📅
Manages I/O operations. 💾
Executes callbacks. 🔄  


### 3️⃣ async and await
async: Used to define a coroutine.
await: Used inside a coroutine to call another coroutine and wait for its result. It allows control to be handed back to the event loop. ⏳
Example:

    async def say_hello():
        await asyncio.sleep(1)
        print("Hello! 👋")  

Basic Example
A simple asynchronous program with coroutines:  

      import asyncio

    async def say_hello():
        await asyncio.sleep(1)
        print("Hello! 👋")

    async def say_world():
        await asyncio.sleep(1)
        print("World! 🌍")

    async def main():
        await say_hello()
        await say_world()

    asyncio.run(main())  


Result:
Total time: 2 seconds. ⏱️
Sequential execution.  

Concurrent Execution ⚡
To execute multiple coroutines simultaneously, use asyncio.gather:  

    async def main():  
    await asyncio.gather(say_hello(), say_world())  

    Result:  
    Total time: ~1 second. 🚀  
    Coroutines run in parallel. 🎭  


Real-World Example 🌐  
Suppose you want to fetch multiple web pages at the same time. Here’s an example using aiohttp:  

        import aiohttp
        import asyncio

    async def fetch_url(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()

    async def main():
        urls = ["https://example.com", "https://example.org", "https://example.net"]
        tasks = [fetch_url(url) for url in urls]
        pages = await asyncio.gather(*tasks)
        for url, page in zip(urls, pages):
            print(f"Content from {url}: {len(page)} bytes 📝")

    asyncio.run(main())  

Benefits:  
Concurrent data retrieval. 🌐
Significant time savings for I/O tasks.  

Coroutines vs Multi-threading 🧵  
Coroutines 👍  
- Lightweight: Minimal memory usage. 💾  
- Predictable: No preemption or race conditions. 🛡️  
- Ideal for I/O-bound tasks. 🌍  
- Threads 👎  
- True parallelism for CPU-bound tasks. ⚙️  
- Higher memory overhead: Each thread consumes more resources. 💥  
- Issues like deadlocks and race conditions. 🧨  

Additional Resources 📖  
- Official asyncio documentation  
- aiohttp tutorial  