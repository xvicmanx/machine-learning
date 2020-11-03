# Machine learning

Machine Learning is a subfield of Artificial Intelligence which goal is to develop technique to make computers (machines) learn.

The purpose of these repository is to solve some machine learning problems for academic purposes.


## GRPC service

### Machine Learning Service
Service that makes predictions using machine learning models.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| PredictSalary | [PredictSalaryRequest](#PredictSalaryRequest) | [PredictSalaryResponse](#PredictSalaryResponse) | Predicts salary based on years of experience. |
| PredictPurchase | [PredictPurchaseRequest](#PredictPurchaseRequest) | [PredictPurchaseResponse](#PredictPurchaseResponse) | Predicts if a customer will purchase based on salary and age. |


<a name="PredictSalaryRequest"></a>

### PredictSalaryRequest
Predict Salary Request


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| years | int32 | required | The years of experience |


<a name="PredictSalaryResponse"></a>

### PredictSalaryResponse
Predict Salary Response


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| salary | float | | The predicted salary |


<a name="PredictSalaryRequest"></a>

### PredictPurchaseRequest
Predict Purchase Request


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| age | int32 | required | Customer's age |
| salary | float | required | Customer's salary |


<a name="PredictPurchaseResponse"></a>

### PredictPurchaseResponse
Predict Purchase Response


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| purchase | bool | | If the customer will purchase or not |


### Compiling
Move to `grpc_service` directory and run:
```sh
python -m grpc_tools.protoc -I .  --python_out=. --grpc_python_out=. ./service.proto
```

### Starting server

Run the following command:
```sh
python start_server.py
```

### Run client demo

Run the following command:
```sh
python grpc_client.py
```