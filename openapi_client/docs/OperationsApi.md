# openapi_client.OperationsApi

All URIs are relative to *https://api-invest.tinkoff.ru/openapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operations_get**](OperationsApi.md#operations_get) | **GET** /operations | Получение списка операций


# **operations_get**
> OperationsResponse operations_get(_from, interval, figi=figi)

Получение списка операций

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
api_instance = openapi_client.OperationsApi(openapi_client.ApiClient(configuration))
_from = '2013-10-20' # date | Начало временного промежутка
interval = openapi_client.OperationInterval() # OperationInterval | Длительность временного промежутка
figi = 'figi_example' # str | Figi инструмента для фильтрации (optional)

try:
    # Получение списка операций
    api_response = api_instance.operations_get(_from, interval, figi=figi)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Начало временного промежутка | 
 **interval** | [**OperationInterval**](.md)| Длительность временного промежутка | 
 **figi** | **str**| Figi инструмента для фильтрации | [optional] 

### Return type

[**OperationsResponse**](OperationsResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список операций |  -  |
**500** | Брокерский счет не найден |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

