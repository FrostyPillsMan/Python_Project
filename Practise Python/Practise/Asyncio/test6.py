"""Exception Handling"""

import asyncio

async def fail_after_sleep():
    await asyncio.sleep(1)
    raise ValueError("Oops! Something went wrong.")

async def main():
    try:
        await fail_after_sleep()
    except ValueError as e:
        print(f"Caught exception: {e}")


if __name__ == "__main__":
    asyncio.run(main())

