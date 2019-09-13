# openapi_client.MarketApi

All URIs are relative to *https://api-invest.tinkoff.ru/openapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**market_bonds_get**](MarketApi.md#market_bonds_get) | **GET** /market/bonds | Получение списка облигаций
[**market_currencies_get**](MarketApi.md#market_currencies_get) | **GET** /market/currencies | Получение списка валютных пар
[**market_etfs_get**](MarketApi.md#market_etfs_get) | **GET** /market/etfs | Получение списка ETF
[**market_search_by_figi_get**](MarketApi.md#market_search_by_figi_get) | **GET** /market/search/by-figi | Получение инструмента по FIGI
[**market_search_by_ticker_get**](MarketApi.md#market_search_by_ticker_get) | **GET** /market/search/by-ticker | Получение инструмента по тикеру
[**market_stocks_get**](MarketApi.md#market_stocks_get) | **GET** /market/stocks | Получение списка акций


# **market_bonds_get**
> MarketInstrumentListResponse market_bonds_get()

Получение списка облигаций

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
api_instance = openapi_client.MarketApi(openapi_client.ApiClient(configuration))

try:
    # Получение списка облигаций
    api_response = api_instance.market_bonds_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->market_bonds_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MarketInstrumentListResponse**](MarketInstrumentListResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**500** | Инструмент не найден |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_currencies_get**
> MarketInstrumentListResponse market_currencies_get()

Получение списка валютных пар

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
api_instance = openapi_client.MarketApi(openapi_client.ApiClient(configuration))

try:
    # Получение списка валютных пар
    api_response = api_instance.market_currencies_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->market_currencies_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MarketInstrumentListResponse**](MarketInstrumentListResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**500** | Инструмент не найден |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_etfs_get**
> MarketInstrumentListResponse market_etfs_get()

Получение списка ETF

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
api_instance = openapi_client.MarketApi(openapi_client.ApiClient(configuration))

try:
    # Получение списка ETF
    api_response = api_instance.market_etfs_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->market_etfs_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MarketInstrumentListResponse**](MarketInstrumentListResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**500** | Инструмент не найден |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_search_by_figi_get**
> MarketInstrumentResponse market_search_by_figi_get(figi)

Получение инструмента по FIGI

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
api_instance = openapi_client.MarketApi(openapi_client.ApiClient(configuration))
figi = 'figi_example' # str | FIGI

try:
    # Получение инструмента по FIGI
    api_response = api_instance.market_search_by_figi_get(figi)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->market_search_by_figi_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **figi** | **str**| FIGI | 

### Return type

[**MarketInstrumentResponse**](MarketInstrumentResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**500** | Инструмент не найден |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_search_by_ticker_get**
> MarketInstrumentListResponse market_search_by_ticker_get(ticker)

Получение инструмента по тикеру

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
api_instance = openapi_client.MarketApi(openapi_client.ApiClient(configuration))
ticker = 'ticker_example' # str | Тикер инструмента

try:
    # Получение инструмента по тикеру
    api_response = api_instance.market_search_by_ticker_get(ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->market_search_by_ticker_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Тикер инструмента | 

### Return type

[**MarketInstrumentListResponse**](MarketInstrumentListResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**500** | Инструмент не найден |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_stocks_get**
> MarketInstrumentListResponse market_stocks_get()

Получение списка акций

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
api_instance = openapi_client.MarketApi(openapi_client.ApiClient(configuration))

try:
    # Получение списка акций
    api_response = api_instance.market_stocks_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->market_stocks_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MarketInstrumentListResponse**](MarketInstrumentListResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**500** | Инструмент не найден |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

