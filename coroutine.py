import asyncio
import time
from random import randint


def sync_randn():
    time.sleep(3)
    return randint(1, 10)


def main():
    start = time.perf_counter()
    r = sync_randn()
    elapsed = time.perf_counter() - start
    print(f"sync {r} took {elapsed:0.2f} seconds.")


# this is a coroutine
async def async_randn():
    await asyncio.sleep(3)
    return randint(1, 10)


async def async_main():
    start = time.perf_counter()
    r = await async_randn()
    elapsed = time.perf_counter() - start
    print(f"async {r} took {elapsed:0.2f} seconds.")

    start = time.perf_counter()
    r = await asyncio.gather(async_randn(), async_randn(), async_randn())
    elapsed = time.perf_counter() - start
    print(f"async {r} took {elapsed:0.2f} seconds.")

    start = time.perf_counter()
    # use generator comprehension and unpack with *
    r = await asyncio.gather(*(async_randn() for _ in range(10)))
    elapsed = time.perf_counter() - start
    print(f"async {r} took {elapsed:0.2f} seconds.")


if __name__ == "__main__":

    main()

    # create event loop
    asyncio.run(async_main())
