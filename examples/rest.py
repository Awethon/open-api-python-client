from openapi_client_wrapper import openapi

token = 'YOUR TOKEN'
client = openapi.sandbox_api_client(token)
client.sandbox.sandbox_register_post()
client.sandbox.sandbox_currencies_balance_post(sandbox_set_currency_balance_request={"currency": "USD", "balance": 1000})
