# Operation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**trades** | [**list[OperationTrade]**](OperationTrade.md) |  | [optional] 
**commission** | [**MoneyAmount**](MoneyAmount.md) |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | 
**payment** | **float** |  | 
**price** | **float** |  | [optional] 
**quantity** | **int** |  | [optional] 
**figi** | **str** |  | [optional] 
**instrument_type** | [**InstrumentType**](InstrumentType.md) |  | [optional] 
**is_margin_call** | **bool** |  | 
**date** | **datetime** | ISO8601 | 
**operation_type** | [**OperationTypeWithCommission**](OperationTypeWithCommission.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


