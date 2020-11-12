# Machine learning

Machine Learning is a subfield of Artificial Intelligence which goal is to develop technique to make computers (machines) learn.

The purpose of these repository is to solve some machine learning problems for academic purposes.


## GRPC service

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

Also using `grpcurl` tool

```sh

grpcurl  -d '{"years": 2}' -plaintext localhost:50051 machine_learning.MachineLearning/PredictSalary

grpcurl  -d '{"age": 47, "salary": "30000"}' -plaintext localhost:50051 machine_learning.MachineLearning/PredictPurchase

grpcurl  -d '{"annual_income": 20, "spending_score": 90}' -plaintext localhost:50051 machine_learning.MachineLearning/PredictSegment

grpcurl  -d '{}' -plaintext localhost:50051 machine_learning.MachineLearning/GetOptimalCampaignAdOption

```

### Machine Learning Service API
Service that makes predictions using machine learning models.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| PredictSalary | [PredictSalaryRequest](#PredictSalaryRequest) | [PredictSalaryResponse](#PredictSalaryResponse) | Predicts salary based on years of experience. |
| PredictPurchase | [PredictPurchaseRequest](#PredictPurchaseRequest) | [PredictPurchaseResponse](#PredictPurchaseResponse) | Predicts if a customer will purchase based on salary and age. |
| PredictSegment | [PredictSegmentRequest](#PredictSegmentRequest) | [PredictSegmentResponse](#PredictSegmentResponse) | Predicts mall customer segment based on annual income and spending score. |
| GetOptimalCampaignAdOption | [GetOptimalCampaignAdOptionRequest](#GetOptimalCampaignAdOptionRequest) | [GetOptimalCampaignAdOptionResponse](#GetOptimalCampaignAdOptionResponse) | Gets the optimal campaign ad |


<a name="PredictSalaryRequest"></a>

#### Predict Salary Request


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| years | int32 | required | The years of experience |


<a name="PredictSalaryResponse"></a>

#### Predict Salary Response


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| salary | float | | The predicted salary |


<a name="PredictSalaryRequest"></a>

#### Predict Purchase Request


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| age | int32 | required | Customer's age |
| salary | float | required | Customer's salary |


<a name="PredictPurchaseResponse"></a>

#### Predict Purchase Response


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| purchase | bool | | If the customer will purchase or not |


<a name="PredictSegmentRequest"></a>

#### Predict Segment Request


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| annual_income | float | required | Customer's annual income |
| spending_score | float | required | Customer's spending score |


<a name="PredictPurchaseResponse"></a>

#### Predict Segment Response


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| segment | [CustomerSegment](#CustomerSegment) | | Customer's segment |


<a name="GetOptimalCampaignAdOptionRequest"></a>

#### Get Optimal Campaign Ad Option Request

Empty

<a name="GetOptimalCampaignAdOptionResponse"></a>

#### Get Optimal Campaign Ad Option Response


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ad | int32 | | Optimal campaign ad |


<a name="CustomerSegment"></a>

#### Customer Segment


| Key | Value |
| ----- | ---- |
| UNKNOWN_SEGMENT | 0 |
| MEDIUM_INCOME_MEDIUM_SPENDING_SCORE_SEGMENT | 1 |
| LOW_INCOME_HIGH_SPENDING_SCORE_SEGMENT | 2 |
| HIGH_INCOME_HIGH_SPENDING_SCORE_SEGMENT | 3 |
| LOW_INCOME_LOW_SPENDING_SCORE_SEGMENT | 4 |
| HIGH_INCOME_LOW_SPENDING_SCORE_SEGMENT | 5 |
