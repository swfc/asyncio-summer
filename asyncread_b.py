import asyncio
import sys
from pathlib import Path

import aiofiles
import aionotify


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
    async with aiofiles.open(fnpath, mode="r", encoding="utf-8") as af:
        print("Reading lines!")
        async for line in af:
            print(line, end="")

        while True:
            event = await watcher.get_event()
            print("Got event! {}".format(event))
            async for line in af:
                print(line, end="")

        watcher.close()


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
