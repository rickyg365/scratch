import os
import asyncio


async def precursor():
    return 1


async def func1():
    print("Running function 1...")
    await asyncio.sleep(1)
    print("Function 1: DONE")


async def func2():
    print("Running function 2...")
    await asyncio.sleep(2)
    print("Function 2: DONE")


async def func3():
    print("Running function 3...")
    await asyncio.sleep(3)
    print("Function 3: DONE")


async def func4():
    print("Running function 4...")
    await asyncio.sleep(4)
    print("Function 4: DONE")


async def func5():
    print("Running function 5...")
    await asyncio.sleep(5)
    print("Function 5: DONE")


async def main():

    task1 = asyncio.create_task(func1())

    task2 = asyncio.create_task(func2())

    task3 = asyncio.create_task(func3())

    task4 = asyncio.create_task(func4())

    task5 = asyncio.create_task(func5())

    pre = asyncio.create_task(precursor())
    await pre

    print("-"*20)

    await task5

    # await func1()
    # await func2()
    # await func3()
    # await func4()
    # await func5()


if __name__ == "__main__":
    asyncio.run(main())
