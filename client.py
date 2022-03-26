import aiohttp
import asyncio


async def main() -> None:
    async with aiohttp.ClientSession('http://localhost:8080') as session:
        response = await session.post('/sessions')

        if response.status != 200:
            raise Exception('CANNOT INITIALIZE SESSION')

        while True:
            response = await session.post('/status',
                                          data={'payload': {'status': 'OK'}})
            if response.status == 200:
                print('SENT STATUS TO SERVER')
            else:
                print(f'GOT ERROR MSG -> {await response.text()}')
            await asyncio.sleep(1)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
