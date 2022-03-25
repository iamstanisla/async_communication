from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from json import dumps

active_url_pool = list()


async def data(request):
    if request.url not in active_url_pool:
        web.Response(text='You dodn"t have initialized session')
    return web.Response(text='Good morning!')


async def session_init(request: Request) -> Response:
    print('HOST ', request.host)
    if request.host not in active_url_pool:
        active_url_pool.append(request.host)
    return web.Response(text='OK')


async def session_list(request: Request) -> Response:
    return web.Response(text=dumps(active_url_pool))


app = web.Application()
app.add_routes([web.get('/data', data),
                web.post('/sessions', session_init),
                web.get('/sessions', session_list)
                ])

if __name__ == '__main__':
    web.run_app(app)
