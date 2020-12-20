
from sklearn.tree import DecisionTreeClassifier
import restaurant_reviews_prediction_base_model as bm

class DecisionTreeRestaurantReviewsPredictionModel(bm.RestaurantReviewsPredictionModel):
    def __init__(self):
        super().__init__()

    def _get_model_instance(self):
        return DecisionTreeClassifier(
            criterion = 'entropy',
            random_state = 0
        )
