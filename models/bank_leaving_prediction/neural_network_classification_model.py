
from sklearn.neural_network import MLPClassifier
import bank_leaving_prediction_base_model as bm

class NeuralNetworkBankLeavingPredictionModel(bm.BankLeavingPredictionModel):
    def __init__(self):
        super().__init__()

    def _get_model_instance(self):
        return MLPClassifier(
            solver = 'adam',
            hidden_layer_sizes = (6, 6),
            random_state = 0,
            learning_rate = 'adaptive',
        )