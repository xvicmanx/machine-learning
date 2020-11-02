"""Machine learning Servicer"""

from concurrent import futures
import service_pb2_grpc
import service_pb2

class MachineLearningServicer(service_pb2_grpc.MachineLearningServicer):
    """Provides methods that implement functionality of machine learning server."""

    def __init__(self, salary_model):
        self.__salary_model = salary_model

    def PredictSalary(self, request, context):
       salary_predictions = self.__salary_model.predict([[request.years]])
       return service_pb2.PredictSalaryResponse(salary=salary_predictions[0])
