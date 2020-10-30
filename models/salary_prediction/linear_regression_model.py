
from sklearn.linear_model import LinearRegression
from .base_model import BaseSalaryPredictionModel

class LinearRegressionSalaryPredictionModel(BaseSalaryPredictionModel):
    def __init__(self):
        super().__init__('linear_regression_salary_prediction_model_serialized.sav') 

    def _get_model_instance(self):
        return LinearRegression()