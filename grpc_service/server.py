"""Machine learning Servicer"""

from concurrent import futures
from service_pb2_grpc import MachineLearningServicer as BaseServicer
import service_pb2 as srv

class MachineLearningServicer(BaseServicer):
    """Provides methods that implement functionality of machine learning server."""

    def __init__(
        self,
        salary_model,
        social_ads_model,
        mall_customers_segmentation_model,
        campaign_ad_optimization_model,
    ):
        self.__salary_model = salary_model
        self.__social_ads_model = social_ads_model
        self.__mall_customers_segmentation_model = mall_customers_segmentation_model
        self.__campaign_ad_optimization_model = campaign_ad_optimization_model

    def PredictSalary(self, request, context):
       predictions = self.__salary_model.predict([[request.years]])
       return srv.PredictSalaryResponse(salary = predictions[0])

    def PredictPurchase(self, request, context):
       predictions = self.__social_ads_model.predict([[request.age, request.salary]])
       return srv.PredictPurchaseResponse(purchase = bool(predictions[0]))

    def PredictSegment(self, request, context):
       predictions = self.__mall_customers_segmentation_model.predict([[request.annual_income, request.spending_score]])
       return srv.PredictSegmentResponse(segment = predictions[0] + 1)

    def GetOptimalCampaignAdOption(self, request, context):
       option = self.__campaign_ad_optimization_model.optimal_option()
       return srv.GetOptimalCampaignAdOptionResponse(ad = option + 1)

