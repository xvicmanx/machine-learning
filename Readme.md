# Machine learning

Machine Learning is a subfield of Artificial Intelligence which goal is to develop technique to make computers (machines) learn.

The purpose of these repository is to solve some machine learning problems for academic purposes.


## GRPC service

### Compiling
Move to `src/grpc_service` directory and run:
```sh
python -m grpc_tools.protoc -I .  --python_out=. --grpc_python_out=. ./service.proto
```

### Starting server

Run the following command:
```sh
python src/start_grpc_server.py
```

### Run client demo

Run the following command:
```sh
python src/grpc_client.py
```

Also using `grpcurl` tool

```sh

grpcurl  -d '{"years": 2}' -plaintext localhost:50051 machine_learning.MachineLearning/PredictSalary

grpcurl  -d '{"age": 47, "salary": "30000"}' -plaintext localhost:50051 machine_learning.MachineLearning/PredictPurchase

grpcurl  -d '{"annual_income": 20, "spending_score": 90}' -plaintext localhost:50051 machine_learning.MachineLearning/PredictSegment

grpcurl  -d '{}' -plaintext localhost:50051 machine_learning.MachineLearning/GetOptimalCampaignAdOption

grpcurl  -d '{"review": "The food was excellent!"}' -plaintext localhost:50051 machine_learning.MachineLearning/PredictReviewOutcome


grpcurl  -d '{"credit_score":502,"geography":"France","gender":"Female","age":42,"tenure":8,"balance":159660.8,"number_of_products":3,"has_credit_card":true,"is_active_member":false,"estimated_salary":113931.57}' -plaintext localhost:50051 machine_learning.MachineLearning/PredictBankLeaving

```

### Machine Learning Service API
Service that makes predictions using machine learning models.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| PredictSalary | [PredictSalaryRequest](#PredictSalaryRequest) | [PredictSalaryResponse](#PredictSalaryResponse) | Predicts salary based on years of experience. |
| PredictPurchase | [PredictPurchaseRequest](#PredictPurchaseRequest) | [PredictPurchaseResponse](#PredictPurchaseResponse) | Predicts if a customer will purchase based on salary and age. |
| PredictSegment | [PredictSegmentRequest](#PredictSegmentRequest) | [PredictSegmentResponse](#PredictSegmentResponse) | Predicts mall customer segment based on annual income and spending score. |
| GetOptimalCampaignAdOption | [GetOptimalCampaignAdOptionRequest](#GetOptimalCampaignAdOptionRequest) | [GetOptimalCampaignAdOptionResponse](#GetOptimalCampaignAdOptionResponse) | Gets the optimal campaign ad |
| PredictReviewOutcome | [PredictReviewOutcomeRequest](#PredictReviewOutcomeRequest) | [PredictReviewOutcomeResponse](#PredictReviewOutcomeResponse) | Predicts whether a review correspond to a like or dislike |
| PredictBankLeaving | [PredictBankLeavingRequest](#PredictBankLeavingRequest) | [PredictBankLeavingResponse](#PredictBankLeavingResponse) | Predicts whether a customer will leaving a banking institution or not |

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



<a name="PredictReviewOutcomeRequest"></a>

#### Predict Review Outcome Request


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| review | string | required | Review text |


<a name="PredictReviewOutcomeResponse"></a>

#### Predict Review Outcome Response


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| liked | bool | | Whether a review was a like or dislike |


<a name="PredictBankLeavingRequest"></a>

#### Predict Bank Leaving Request


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| credit_score | float | required | Customer's credit score |
| geography | string | required | Customer's country |
| gender | string | required | Customer's gender |
| age | int32 | required | Customer's age |
| tenure | int32 | required | Customer's tenure |
| balance | float | required | Customer's balance |
| number_of_products | int32 | required | Customer's number of products |
| has_credit_card | bool | required | If the customer has credit card |
| is_active_member | bool | required | If the customer is an active member |
| estimated_salary | float | required | Customer's estimated salary |


<a name="PredictBankLeavingResponse"></a>

#### Predict Bank Leaving Response


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| exited | bool | | Whether the user is leaving or not |




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
