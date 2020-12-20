
from sklearn.ensemble import RandomForestClassifier
import social_network_ads_base_model as bm

class RandomForestSocialNetworkAdsPredictionModel(bm.SocialNetworkAdsPredictionModel):
    def __init__(self):
        super().__init__()

    def _get_model_instance(self):
        return RandomForestClassifier(
            n_estimators = 5,
            criterion = 'entropy',
            random_state = 0
        )