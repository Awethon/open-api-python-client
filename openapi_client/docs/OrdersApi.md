# openapi_client.OrdersApi

All URIs are relative to *https://api-invest.tinkoff.ru/openapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders_cancel_post**](OrdersApi.md#orders_cancel_post) | **POST** /orders/cancel | Отмена заявки
[**orders_get**](OrdersApi.md#orders_get) | **GET** /orders | Получение списка активных заявок
[**orders_limit_order_post**](OrdersApi.md#orders_limit_order_post) | **POST** /orders/limit-order | Создание лимитной заявки


# **orders_cancel_post**
> Empty orders_cancel_post(order_id, empty=empty)

Отмена заявки

### Example

* Bearer Authentication (sso_auth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization: sso_auth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api-invest.tinkoff.ru/openapi
configuration.host = "https://api-invest.tinkoff.ru/openapi"
# Create an instance of the API class
api_instance = openapi_client.OrdersApi(openapi_client.ApiClient(configuration))
order_id = 'order_id_example' # str | ID заявки
empty = openapi_client.Empty() # Empty |  (optional)

try:
    # Отмена заявки
    api_response = api_instance.orders_cancel_post(order_id, empty=empty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_cancel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID заявки | 
 **empty** | [**Empty**](Empty.md)|  | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**500** | Ошибка запроса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_get**
> OrdersResponse orders_get()

Получение списка активных заявок

### Example

* Bearer Authentication (sso_auth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization: sso_auth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api-invest.tinkoff.ru/openapi
configuration.host = "https://api-invest.tinkoff.ru/openapi"
# Create an instance of the API class
api_instance = openapi_client.OrdersApi(openapi_client.ApiClient(configuration))

try:
    # Получение списка активных заявок
    api_response = api_instance.orders_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrdersResponse**](OrdersResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список заявок |  -  |
**500** | Инструмент не найден |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_limit_order_post**
> LimitOrderResponse orders_limit_order_post(figi, limit_order_request)

Создание лимитной заявки

### Example

* Bearer Authentication (sso_auth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization: sso_auth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api-invest.tinkoff.ru/openapi
configuration.host = "https://api-invest.tinkoff.ru/openapi"
# Create an instance of the API class
api_instance = openapi_client.OrdersApi(openapi_client.ApiClient(configuration))
figi = 'figi_example' # str | FIGI инструмента
limit_order_request = openapi_client.LimitOrderRequest() # LimitOrderRequest | 

try:
    # Создание лимитной заявки
    api_response = api_instance.orders_limit_order_post(figi, limit_order_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_limit_order_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **figi** | **str**| FIGI инструмента | 
 **limit_order_request** | [**LimitOrderRequest**](LimitOrderRequest.md)|  | 

### Return type

[**LimitOrderResponse**](LimitOrderResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Созданная заявка |  -  |
**500** | Ошибка запроса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

