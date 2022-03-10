import asyncio
import sys
from pathlib import Path

import aiofiles


async def follow(rawfn):

    cleanfn = Path(rawfn).name
    fnpath = Path().cwd() / cleanfn

    if not fnpath.is_file():
        raise Exception(reason="File {} not found".format(rawfn))

    # Open and read what is in file already
    async with aiofiles.open(fnpath, mode="r", encoding="utf-8") as af:
        print("Reading lines!")
        while True:
            line = await af.readline()
            print(line, end="")


async def main(*args):
    tasks = [follow(name) for name in args]
    await asyncio.gather(*tasks)
    # await follow("one.txt")


if __name__ == "__main__":

    args = sys.argv[1:]
    args = ["one.txt", "two.txt"]

    asyncio.run(main(*args))

    # loop = asyncio.get_event_loop()
    # asyncio.ensure_future(main(*args))
    # loop.run_forever()
