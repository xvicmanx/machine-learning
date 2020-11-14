
from sklearn.svm import SVC
import bank_leaving_prediction_base_model as bm

class SupportVectorMachinesBankLeavingPredictionModel(bm.BankLeavingPredictionModel):
    def __init__(self):
        super().__init__()

    def _get_model_instance(self):
        return SVC(kernel = 'rbf')