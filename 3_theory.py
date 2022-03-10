# Demonstrate asynchronous generator
from random import randint
import time
import asyncio


def skip1(start, stop):
    # generator function
    # yield returns value then pauses execution
    # can be resumed any time later
    for i in range(start, stop + 1, 2):
        yield i


# this is an asynchronous generator
# use when whatever it is generating may
# take a long time like disk io etc
async def slow_square(start, stop):
    for i in skip1(start, stop):
        # this simulates disk io or operating system doing a task
        await asyncio.sleep(2)
        yield i * i


async def fast_cube(start, stop):
    for i in skip1(start, stop):
        # this simulates disk io or operating system doing a task
        await asyncio.sleep(1)
        yield i * i * i


async def main():
    # to use asynchronous generator we use async for loops
    async for sq in slow_square(11, 17):
        print("sq:", sq)

    async for cu in fast_cube(11, 17):
        print("cu:", cu)


if __name__ == "__main__":
    asyncio.run(main())
