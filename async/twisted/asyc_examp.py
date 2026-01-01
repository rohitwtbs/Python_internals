import asyncio

async def main():
    await print_hello()
    pass

async def print_hello():
    await asyncio.sleep(1)
    print("Hello, Asyncio!")


asyncio.run(main())