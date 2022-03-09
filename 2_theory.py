# Demonstrate coroutines
from random import randint
import time
import asyncio


def sync_my_randn():
    # this is a blocking sleep which means no other tasks can be
    # executed until this sleep has finished.
    time.sleep(3)
    return randint(1, 10)


def sync_main():
    # Basic single call to sync_my_randn will take 3 seconds
    start = time.perf_counter()
    r = sync_my_randn()
    elapsed = time.perf_counter() - start
    print(f"{r} took {elapsed:0.2f} seconds.")

    # List comprehension should take around 9 seconds
    start = time.perf_counter()
    r = [sync_my_randn() for _ in range(3)]
    elapsed = time.perf_counter() - start
    print(f"{r} took {elapsed:0.2f} seconds.")


# This asynchronous function is called a coroutine.
# Requires an "async" before def. Should be called with await.
# Is a consumer.
async def async_my_randn():
    # asyncio.sleep is an async function (coroutine) and needs to be awaited.
    # this await will wait for sleep to be complete but other things can
    # be executed elsewhere until this has finished waiting.
    await asyncio.sleep(3)
    return randint(1, 10)


# This is also a coroutine and needs to be awaited.
async def async_main():
    # Basic single call to async_my_randn will take 3 seconds
    start = time.perf_counter()
    r = await async_my_randn()
    elapsed = time.perf_counter() - start
    print(f"{r} took {elapsed:0.2f} seconds.")

    # List comprehension should also take around 9 seconds
    start = time.perf_counter()
    r = [await async_my_randn() for _ in range(3)]
    elapsed = time.perf_counter() - start
    print(f"{r} took {elapsed:0.2f} seconds.")

    # Use asyncio gather to run multiple async_my_randn asynchronously
    # All 3 calls will only take 3 seconds!!
    start = time.perf_counter()
    r = await asyncio.gather(async_my_randn(), async_my_randn(), async_my_randn())
    elapsed = time.perf_counter() - start
    print(f"{r} took {elapsed:0.2f} seconds. AWESOME!!!!!!!!")

    # Use asyncio gather to run multiple async_my_randn asynchronously
    # All 3 calls will only take 3 seconds!!
    start = time.perf_counter()
    # use * to unpack a list comprehension into separate arguments
    r = await asyncio.gather(*[async_my_randn() for _ in range(10)])
    elapsed = time.perf_counter() - start
    print(f"{r} took {elapsed:0.2f} seconds. AWESOMER!!!!!!!!")

    # Use asyncio gather to run multiple async_my_randn asynchronously
    # All 3 calls will only take 3 seconds!!
    start = time.perf_counter()
    # use * to unpack a generator into separate arguments
    r = await asyncio.gather(*(async_my_randn() for _ in range(10)))
    elapsed = time.perf_counter() - start
    print(f"{r} took {elapsed:0.2f} seconds. AWESOMER!!!!!!!!")


if __name__ == "__main__":
    sync_main()

    # need an event loop to run the async_main() coroutine
    asyncio.run(async_main())
