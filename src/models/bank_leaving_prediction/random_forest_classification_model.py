
from sklearn.ensemble import RandomForestClassifier
import bank_leaving_prediction_base_model as bm

class RandomForestBankLeavingPredictionModel(bm.BankLeavingPredictionModel):
    def __init__(self):
        super().__init__()

    def _get_model_instance(self):
        return RandomForestClassifier(
            n_estimators = 10,
            criterion = 'entropy',
            random_state = 0
        )