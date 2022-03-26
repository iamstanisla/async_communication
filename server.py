from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response

from error_message import ErrorMessage
from error_picker import ErrorPicker
from response_body import ResponseBody

connection_pool = list()

ok_status_got_count = 0


async def status(request):
    if request.url not in connection_pool:
        picker = ErrorPicker()
        picker.add(ErrorMessage("You didn't init session"))
        return web.Response(
            text=ResponseBody.response_error(picker.get_errors()),
            status=400
        )

    return web.Response(
            text=ResponseBody.response_ok(None),
            status=200
        )


async def session_init(request: Request) -> Response:
    connection_pool.append(request.host)
    print(f'CONNECTION POOL: -> {connection_pool}\nCONNECTION COUNT: -> {len(connection_pool)}')

    return web.Response(
            text=ResponseBody.response_ok(None),
            status=200
        )


app = web.Application()
app.add_routes([web.post('/status', status),
                web.post('/sessions', session_init)
                ])

if __name__ == '__main__':
    web.run_app(app)
