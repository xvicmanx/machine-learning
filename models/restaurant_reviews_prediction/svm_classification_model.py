
from sklearn.svm import SVC
import restaurant_reviews_prediction_base_model as bm

class SupportVectorMachinesSocialNetworkAdsPredictionModel(bm.RestaurantReviewsPredictionModel):
    def __init__(self):
        super().__init__()

    def _get_model_instance(self):
        return SVC(kernel='rbf')