
from sklearn.ensemble import RandomForestRegressor
import salary_prediction_base_model as base_model

class RandomForestRegressionSalaryPredictionModel(base_model.BaseSalaryPredictionModel):
    def __init__(self):
        super().__init__()

    def _get_model_instance(self):
        return RandomForestRegressor(n_estimators = 10, random_state = 0)
