
from sklearn.linear_model import LinearRegression
import salary_prediction_base_model as base_model

class LinearRegressionSalaryPredictionModel(base_model.BaseSalaryPredictionModel):
    def __init__(self):
        super().__init__()

    def _get_model_instance(self):
        return LinearRegression()