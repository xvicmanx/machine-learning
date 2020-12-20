
from sklearn.svm import SVC
import social_network_ads_base_model as bm

class SupportVectorMachinesSocialNetworkAdsPredictionModel(bm.SocialNetworkAdsPredictionModel):
    def __init__(self):
        super().__init__()

    def _get_model_instance(self):
        return SVC(kernel='rbf')