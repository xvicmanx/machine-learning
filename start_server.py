"""Start Machine Learning server"""

import grpc
from concurrent import futures
from grpc_service.service_pb2_grpc import add_MachineLearningServicer_to_server
from grpc_service.server import MachineLearningServicer

from models.salary_prediction.linear_regression_model import LinearRegressionSalaryPredictionModel


def serve():
    predict_salary_model = LinearRegressionSalaryPredictionModel()
    predict_salary_model.load()
  
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servicer = MachineLearningServicer(predict_salary_model)
    add_MachineLearningServicer_to_server(servicer, server)
  
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()