import grpc
from grpc_service import service_pb2, service_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        client = service_pb2_grpc.MachineLearningStub(channel)
        request = service_pb2.PredictSalaryRequest(years=5)
        response = client.PredictSalary(request)
        
        print('The Salary is = ' + str(response.salary))


if __name__ == '__main__':
    run()