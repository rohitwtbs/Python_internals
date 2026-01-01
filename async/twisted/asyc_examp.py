import asyncio

async def main():
    print_hello()
    print("after asyn call")
    pass

async def print_hello():
    await asyncio.sleep(1)
    print("Hello, Asyncio!")


asyncio.run(main())


# Qyestions , why this warning
#  RuntimeWarning: coroutine 'print_hello' was never awaited
#   print_hello()
# RuntimeWarning: Enable tracemalloc to get the object allocation traceback
# after asyn call