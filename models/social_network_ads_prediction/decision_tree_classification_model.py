
from sklearn.tree import DecisionTreeClassifier
import social_network_ads_base_model as bm

class DecisionTreeSocialNetworkAdsPredictionModel(bm.SocialNetworkAdsPredictionModel):
    def __init__(self):
        super().__init__()

    def _get_model_instance(self):
        return DecisionTreeClassifier(
            criterion = 'entropy',
            random_state = 0
        )