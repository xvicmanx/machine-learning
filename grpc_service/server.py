"""Machine learning Servicer"""

from concurrent import futures
import service_pb2_grpc
import service_pb2

class MachineLearningServicer(service_pb2_grpc.MachineLearningServicer):
    """Provides methods that implement functionality of machine learning server."""

    def __init__(self, salary_model, social_ads_model):
        self.__salary_model = salary_model
        self.__social_ads_model = social_ads_model

    def PredictSalary(self, request, context):
       predictions = self.__salary_model.predict([[request.years]])
       return service_pb2.PredictSalaryResponse(salary=predictions[0])

    def PredictPurchase(self, request, context):
       predictions = self.__social_ads_model.predict([[request.age, request.salary]])
       return service_pb2.PredictPurchaseResponse(purchase=bool(predictions[0]))
