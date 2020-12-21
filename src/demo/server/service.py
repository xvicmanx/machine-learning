import os, sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)

sys.path.append(current_dir)
sys.path.append(parent_dir)
sys.path.append(os.path.dirname(parent_dir))

from grpc_service import service_pb2 as srv

class Service:
  def __init__(self, client):
    self.__client = client
  
  def predict_salary(self, years):
    return self.__client.PredictSalary(srv.PredictSalaryRequest(years = years))

  def predict_purchase(self, age, salary):
    return self.__client.PredictPurchase(srv.PredictPurchaseRequest(age = age, salary = salary))
