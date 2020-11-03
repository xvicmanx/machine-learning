
from sklearn.tree import DecisionTreeRegressor
import salary_prediction_base_model as base_model

class DecisionTreeRegressionSalaryPredictionModel(base_model.BaseSalaryPredictionModel):
    def __init__(self):
        super().__init__()

    def _get_model_instance(self):
        return DecisionTreeRegressor(random_state = 0)
