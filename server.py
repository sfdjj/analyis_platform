from tornado.httpclient import AsyncHTTPClient
from tornado.simple_httpclient import SimpleAsyncHTTPClient


def main():
    AsyncHTTPClient.configure(SimpleAsyncHTTPClient, max_clients=10000, defaults=dict(request_timeout=400))
    # from ser


if __name__ == '__main__':
    main()
