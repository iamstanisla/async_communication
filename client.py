import aiohttp
import asyncio
from aiohttp import web

import argparse
PROTOCOL = 'http'
HOST = 'localhost'
PORT = '8080'

URL_PREFIX = f'{PROTOCOL}://{HOST}:{PORT}'


runners = []


async def start_client(app, port, address='localhost'):
    runner = web.AppRunner(app)
    runners.append(runner)
    await runner.setup()
    site = web.TCPSite(runner, address, port)
    await site.start()


async def main() -> None:
    session_initialized = False
    get_count = 1
    async with aiohttp.ClientSession() as session:
        while True:
            if not session_initialized:
                response = await session.post(f'{URL_PREFIX}/sessions')
                if response.status == 200:
                    session_initialized = True

            if session_initialized:
                response = await session.get(f'{URL_PREFIX}/data')
                print("Response body: ", await response.text())
                print("Get count: ", get_count)
                get_count += 1
                await asyncio.sleep(1)

            if get_count >= 100:
                break
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('count', type=int, help='client amount', default=1)
    client_amount = parser.parse_args().count
    if client_amount < 1:
        raise Exception('Client count must more then 1, got ', client_amount)
    loop = asyncio.get_event_loop()

    for number in range(1, client_amount + 1):
        loop.create_task(start_client(web.Application(), port=(8080 + number)))


    try:
        loop.run_forever()
    except:
        pass
    finally:
        for runner in runners:
            loop.run_until_complete(runner.cleanup())
