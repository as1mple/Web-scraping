import asyncio
import time

from agoda_head import run

if __name__ == '__main__':

    start = time.time()
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run())
    loop.run_until_complete(future)
    print('Work time took : ', time.time() - start)
