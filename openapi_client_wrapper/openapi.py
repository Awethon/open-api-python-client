from openapi_client import MarketApi
from openapi_client import SandboxApi
from openapi_client import OrdersApi
from openapi_client import PortfolioApi
from openapi_client import OperationsApi
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration


class SandboxOpenApi(object):
    def __init__(self, api_client):
        self.sandbox = SandboxApi(api_client=api_client)
        self.orders = OrdersApi(api_client=api_client)
        self.portfolio = PortfolioApi(api_client=api_client)
        self.market = MarketApi(api_client=api_client)
        self.operations = OperationsApi(api_client=api_client)


class OpenApi(object):
    def __init__(self, api_client):
        self.orders = OrdersApi(api_client=api_client)
        self.portfolio = PortfolioApi(api_client=api_client)
        self.market = MarketApi(api_client=api_client)
        self.operations = OperationsApi(api_client=api_client)


def sandbox_api_client(sso_token):
    sandbox_host = 'https://api-invest.tinkoff.ru/openapi/sandbox/'
    conf = Configuration(host=sandbox_host)

    conf.access_token = sso_token
    return SandboxOpenApi(ApiClient(configuration=conf))


def api_client(sso_token):
    host = 'https://api-invest.tinkoff.ru/openapi/'
    conf = Configuration(host=host)
    conf.access_token = sso_token
    return OpenApi(ApiClient(configuration=conf))

