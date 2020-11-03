import grpc
from grpc_service import service_pb2, service_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        client = service_pb2_grpc.MachineLearningStub(channel)
        
        salary_response = client.PredictSalary(service_pb2.PredictSalaryRequest(years = 5))
        purchase_response = client.PredictPurchase(service_pb2.PredictPurchaseRequest(age = 47, salary = 30000))
        
        print('The Salary is = ' + str(salary_response.salary))
        print('Will purchase? = ' + str(purchase_response.purchase))


if __name__ == '__main__':
    run()