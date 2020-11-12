import grpc
from grpc_service import service_pb2 as srv, service_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        client = service_pb2_grpc.MachineLearningStub(channel)
        
        salary_response = client.PredictSalary(srv.PredictSalaryRequest(years = 5))
        purchase_response = client.PredictPurchase(srv.PredictPurchaseRequest(age = 47, salary = 30000))
        segment_response = client.PredictSegment(srv.PredictSegmentRequest(annual_income = 20, spending_score = 90))
        ad_response = client.GetOptimalCampaignAdOption(srv.GetOptimalCampaignAdOptionRequest())
        
        print('The Salary is = ' + str(salary_response.salary))
        print('Will purchase? = ' + str(purchase_response.purchase))
        print('Segment = ' + str(segment_response.segment))
        print('Ad = ' + str(ad_response.ad))


if __name__ == '__main__':
    run()