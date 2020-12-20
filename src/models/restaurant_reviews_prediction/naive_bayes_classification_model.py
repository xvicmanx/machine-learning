
from sklearn.naive_bayes import GaussianNB
import restaurant_reviews_prediction_base_model as bm

class NaiveBayesRestaurantReviewsPredictionModel(bm.RestaurantReviewsPredictionModel):
    def __init__(self):
        super().__init__()

    def _get_model_instance(self):
        return GaussianNB()
