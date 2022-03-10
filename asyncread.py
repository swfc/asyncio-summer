import asyncio
import contextlib
import sys
import time
from pathlib import Path

import aionotify
from aiofile import AIOFile, LineReader


async def follow(rawfn):

    cleanfn = Path(rawfn).name
    fnpath = Path().cwd() / cleanfn

    if not fnpath.is_file():
        raise Exception(reason="File {} not found".format(rawfn))

    # Setup watcher for file
    watcher = aionotify.Watcher()
    watcher.watch(alias=rawfn, path=str(fnpath), flags=aionotify.Flags.MODIFY)
    await watcher.setup(asyncio.get_event_loop())
    print('Watcher created for "{}"'.format(fnpath))

    # Open and read what is in file already
    async with AIOFile(fnpath, mode="r", encoding="utf-8") as afp:
        print("Sending lines!")
        reader = LineReader(afp)

        async for line in reader:
            print(line, end="")

        while True:
            event = await watcher.get_event()
            print("Got event! {}".format(event))
            async for line in reader:
                print(line, end="")

        watcher.close()


async def main(*args):
    tasks = [follow(name) for name in args]
    result = await asyncio.gather(*tasks)
    # await follow("one.txt")


if __name__ == "__main__":

    args = sys.argv[1:]
    args = ["one.txt", "two.txt"]

    asyncio.run(main(*args))

    # loop = asyncio.get_event_loop()
    # asyncio.ensure_future(main(*args))
    # loop.run_forever()
