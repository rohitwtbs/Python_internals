import asyncio

async def greet():
    print("Hello, world!")
    await asyncio.sleep(10)
    print("Goodbye, world!")


asyncio.run(greet())
print("This is a test")



# Notes
# this is not beahving like async like how async beahves in javascript