
from sklearn.linear_model import LogisticRegression
import social_network_ads_base_model as bm

class LogisticRegressionSocialNetworkAdsPredictionModel(bm.SocialNetworkAdsPredictionModel):
    def __init__(self):
        super().__init__()

    def _get_model_instance(self):
        return LogisticRegression(random_state = 0)