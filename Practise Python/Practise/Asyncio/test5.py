"""Timeouts and cancellation"""

import asyncio

async def long_running_task():
    try:
        await asyncio.sleep(10)
        print("Task completed")
    except asyncio.CancelledError:
        print("Task cancelled")

async def main():
    task = asyncio.create_task(long_running_task())

    try:
        await asyncio.create_task(long_running_task())
    except asyncio.TimeoutError:
        print("Timeout reached, canceling task")
        task.cancel()
        await task

if __name__ == "__main__":
    asyncio.run(main())

