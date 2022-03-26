from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response

from error_message import ErrorMessage
from error_picker import ErrorPicker
from response_body import ResponseBody

connection_pool = list()

response_body = ResponseBody()


async def status(request):
    if request.host not in connection_pool:
        picker = ErrorPicker()
        picker.add(ErrorMessage("You didn't init session"))
        print(f'HOST:\'{request.host}\' DIDN"T FIND')
        return web.Response(
            text=response_body.response_error(picker.get_errors()),
            status=400
        )

    return web.Response(
            text=response_body.response_ok(None),
            status=200
        )


async def session_init(request: Request) -> Response:
    connection_pool.append(request.host)
    print(f'CONNECTION POOL: -> {connection_pool}\n'
          f'CONNECTION COUNT: -> {len(connection_pool)}')

    return web.Response(
            text=response_body.response_ok(None),
            status=200
        )


app = web.Application()
app.add_routes([web.post('/status', status),
                web.post('/sessions', session_init)
                ])

if __name__ == '__main__':
    web.run_app(app)
