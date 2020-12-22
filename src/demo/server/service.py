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

  def predict_customer_segment(self, annual_income, spending_score):
    return self.__client.PredictSegment(srv.PredictSegmentRequest(annual_income = annual_income, spending_score = spending_score))

  def get_optimal_campaign_ad(self):
    return self.__client.GetOptimalCampaignAdOption(srv.GetOptimalCampaignAdOptionRequest())

  def predict_review_outcome(self, review):
    return self.__client.PredictReviewOutcome(srv.PredictReviewOutcomeRequest(review = review))
  
  def predict_bank_leaving(
    self,
    credit_score = 502,
    geography = 'France',
    gender = 'Female',
    age = 25,
    tenure = 1,
    balance = 100.00,
    number_of_products = 1,
    has_credit_card = True,
    is_active_member = False,
    estimated_salary = 100.00,
  ):
    return self.__client.PredictBankLeaving(srv.PredictBankLeavingRequest(
      credit_score = credit_score,
      geography = geography,
      gender = gender,
      age = age,
      tenure = tenure,
      balance = balance,
      number_of_products = number_of_products,
      has_credit_card = has_credit_card,
      is_active_member = is_active_member,
      estimated_salary = estimated_salary,
    ))
    
  def predict_cat_or_dog(self, base64_img):
    return self.__client.PredictCatOrDog(srv.PredictCatOrDogRequest(img = base64_img))
