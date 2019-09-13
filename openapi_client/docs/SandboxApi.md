# openapi_client.SandboxApi

All URIs are relative to *https://api-invest.tinkoff.ru/openapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sandbox_clear_post**](SandboxApi.md#sandbox_clear_post) | **POST** /sandbox/clear | Удаление всех позиций
[**sandbox_currencies_balance_post**](SandboxApi.md#sandbox_currencies_balance_post) | **POST** /sandbox/currencies/balance | Выставление баланса по валютным позициям
[**sandbox_positions_balance_post**](SandboxApi.md#sandbox_positions_balance_post) | **POST** /sandbox/positions/balance | Выставление баланса по инструментным позициям
[**sandbox_register_post**](SandboxApi.md#sandbox_register_post) | **POST** /sandbox/register | Регистрация клиента в sandbox


# **sandbox_clear_post**
> Empty sandbox_clear_post()

Удаление всех позиций

Удаление всех позиций клиента

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
api_instance = openapi_client.SandboxApi(openapi_client.ApiClient(configuration))

try:
    # Удаление всех позиций
    api_response = api_instance.sandbox_clear_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SandboxApi->sandbox_clear_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**500** | Ошибка запроса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_currencies_balance_post**
> Empty sandbox_currencies_balance_post(sandbox_set_currency_balance_request)

Выставление баланса по валютным позициям

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
api_instance = openapi_client.SandboxApi(openapi_client.ApiClient(configuration))
sandbox_set_currency_balance_request = openapi_client.SandboxSetCurrencyBalanceRequest() # SandboxSetCurrencyBalanceRequest | Запрос на выставление баланса по валютным позициям

try:
    # Выставление баланса по валютным позициям
    api_response = api_instance.sandbox_currencies_balance_post(sandbox_set_currency_balance_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SandboxApi->sandbox_currencies_balance_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_set_currency_balance_request** | [**SandboxSetCurrencyBalanceRequest**](SandboxSetCurrencyBalanceRequest.md)| Запрос на выставление баланса по валютным позициям | 

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

# **sandbox_positions_balance_post**
> Empty sandbox_positions_balance_post(sandbox_set_position_balance_request)

Выставление баланса по инструментным позициям

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
api_instance = openapi_client.SandboxApi(openapi_client.ApiClient(configuration))
sandbox_set_position_balance_request = openapi_client.SandboxSetPositionBalanceRequest() # SandboxSetPositionBalanceRequest | Запрос на выставление баланса по инструментным позициям

try:
    # Выставление баланса по инструментным позициям
    api_response = api_instance.sandbox_positions_balance_post(sandbox_set_position_balance_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SandboxApi->sandbox_positions_balance_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_set_position_balance_request** | [**SandboxSetPositionBalanceRequest**](SandboxSetPositionBalanceRequest.md)| Запрос на выставление баланса по инструментным позициям | 

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

# **sandbox_register_post**
> Empty sandbox_register_post()

Регистрация клиента в sandbox

Создание валютные позиций для клиента

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
api_instance = openapi_client.SandboxApi(openapi_client.ApiClient(configuration))

try:
    # Регистрация клиента в sandbox
    api_response = api_instance.sandbox_register_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SandboxApi->sandbox_register_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**500** | Ошибка запроса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

