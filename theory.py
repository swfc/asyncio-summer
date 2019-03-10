from random import randint
import time
import asyncio


def odds(start, stop):
    for odd in range(start, stop + 1, 2):
        yield odd


async def randn():
    await asyncio.sleep(3)
    return randint(1, 10)


async def square_odds(start, stop):
    for odd in odds(start, stop):
        await asyncio.sleep(2)
        yield odd ** 2


async def main():
    odds1 = [odd for odd in odds(3, 15)]
    odds2 = tuple(odds(21, 29))
    print(odds1, odds2)

    start = time.perf_counter()
    r = await randn()
    elapsed = time.perf_counter() - start
    print(f'{r} took {elapsed:0.2f} seconds.')

    start = time.perf_counter()
    r = await asyncio.gather(*(randn() for _ in range(10)))
    elapsed = time.perf_counter() - start
    print(f'{r} took {elapsed:0.2f} seconds.')

    async for so in square_odds(11, 17):
        print('so:', so)

if __name__ == "__main__":
    asyncio.run(main())
