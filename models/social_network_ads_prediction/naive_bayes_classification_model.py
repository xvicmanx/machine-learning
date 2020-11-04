
from sklearn.naive_bayes import GaussianNB
import social_network_ads_base_model as bm

class NaiveBayesSocialNetworkAdsPredictionModel(bm.SocialNetworkAdsPredictionModel):
    def __init__(self):
        super().__init__()

    def _get_model_instance(self):
        return GaussianNB()
