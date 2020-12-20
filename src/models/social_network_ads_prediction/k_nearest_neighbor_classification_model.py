
from sklearn.neighbors import KNeighborsClassifier
import social_network_ads_base_model as bm

class KNearestNeighborSocialNetworkAdsPredictionModel(bm.SocialNetworkAdsPredictionModel):
    def __init__(self):
        super().__init__()

    def _get_model_instance(self):
        return KNeighborsClassifier(
            n_neighbors = 5,
            metric = 'minkowski',
            p = 2,
        )
        