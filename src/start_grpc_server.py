"""Start Machine Learning server"""

import grpc
from grpc_reflection.v1alpha import reflection
from concurrent import futures
from grpc_service.service_pb2_grpc import add_MachineLearningServicer_to_server
from grpc_service.service_pb2 import DESCRIPTOR
from grpc_service.server import MachineLearningServicer

from models.salary_prediction.linear_regression_model import LinearRegressionSalaryPredictionModel
from models.social_network_ads_prediction.svm_classification_model import SupportVectorMachinesSocialNetworkAdsPredictionModel
from models.mall_customers_segmentation.k_means_clustering_model import KMeansClusteringModel
from models.optimal_campaign_ad_search.thompson_sampling_model import ThompsonSamplingOptAdSearchModel
from models.restaurant_reviews_prediction.svm_classification_model import SupportVectorMachinesRestaurantReviewsPredictionModel
from models.bank_leaving_prediction.neural_network_classification_model import NeuralNetworkBankLeavingPredictionModel
from models.cat_or_dog_prediction.neural_network_classification_model import NeuralNetworkCatOrDogPredictionModel

def serve():
    print('START')

    predict_salary_model = LinearRegressionSalaryPredictionModel()
    predict_salary_model.load()

    social_ads_model = SupportVectorMachinesSocialNetworkAdsPredictionModel()
    social_ads_model.load()

    mall_customers_segmentation_model = KMeansClusteringModel()
    mall_customers_segmentation_model.load()

    campaign_ad_optimization_model = ThompsonSamplingOptAdSearchModel()
    campaign_ad_optimization_model.load()

    restaurant_review_prediction_model = SupportVectorMachinesRestaurantReviewsPredictionModel()
    restaurant_review_prediction_model.load()

    bank_leaving_model = NeuralNetworkBankLeavingPredictionModel()
    bank_leaving_model.load()

    cat_or_dog_model = NeuralNetworkCatOrDogPredictionModel()
    cat_or_dog_model.load()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servicer = MachineLearningServicer(
        predict_salary_model,
        social_ads_model,
        mall_customers_segmentation_model,
        campaign_ad_optimization_model,
        restaurant_review_prediction_model,
        bank_leaving_model,
        cat_or_dog_model,
    )
    add_MachineLearningServicer_to_server(servicer, server)

    # Enabling service reflection 
    SERVICE_NAMES = (
        DESCRIPTOR.services_by_name['MachineLearning'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
  
    server.add_insecure_port('[::]:50051')
    server.start()

    print('END')

    server.wait_for_termination()


if __name__ == '__main__':
    print('Start server')
    serve()