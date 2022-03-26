import aiohttp
import asyncio


async def main() -> None:
    async with aiohttp.ClientSession('http://localhost:8080') as session:
        await session.post(f'/sessions')

        while True:
            response = await session.post(f'/status', data={'payload': {'status': 'OK'}})
            if response.status == 200:
                print('sent status to server')
            else:
                print(f'Got {response.status} status')
            # print("Response body: ", await response.text())
            await asyncio.sleep(1)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
