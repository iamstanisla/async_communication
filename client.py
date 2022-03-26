import aiohttp
import asyncio


async def main() -> None:
    async with aiohttp.ClientSession(base_url='http://localhost:8080') as session:
        await session.post(f'/sessions')

        while True:
            await session.post(f'/data', data={'payload': {'status': 'OK'}})
            print('sent status to server')
            # print("Response body: ", await response.text())
            await asyncio.sleep(1)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
