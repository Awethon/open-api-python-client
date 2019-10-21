from openapi_client import openapi
from datetime import datetime, timedelta
from pytz import timezone

token = 'YOUR TOKEN'
client = openapi.sandbox_api_client(token)
client.sandbox.sandbox_clear_post()
client.sandbox.sandbox_register_post()
client.sandbox.sandbox_currencies_balance_post(sandbox_set_currency_balance_request={"currency": "USD", "balance": 1000})


def print_24hr_operations():
    now = datetime.now(tz=timezone('Europe/Moscow'))
    yesterday = now - timedelta(days=1)
    ops = client.operations.operations_get(_from=yesterday.isoformat(), to=now.isoformat())
    print("operations")
    print(ops)
    print()


def print_orders():
    orders = client.orders.orders_get()
    print("active orders")
    print(orders)
    print()


def make_order():
    order_response = client.orders.orders_limit_order_post(figi='BBG009S39JX6',
                                                           limit_order_request={"lots": 1,
                                                                                "operation": "Buy",
                                                                                "price": 0.01})
    print("make order")
    print(order_response)
    print()
    return order_response

# won't work in sandbox - orders are being instantly executed
def cancel_order(order_id):
    cancellation_result = client.orders.orders_cancel_post(order_id=order_id)
    print("cancel order")
    print(cancellation_result)
    print()


print_24hr_operations()
print_orders()
order_response = make_order()
print_orders()
# cancel_order(order_response.payload.order_id)
# print_orders()
