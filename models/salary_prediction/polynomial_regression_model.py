
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import salary_prediction_base_model as base_model

class PolynomialRegressionSalaryPredictionModel(base_model.BaseSalaryPredictionModel):
    def __init__(self):
        super().__init__()
        self.__poly = None

    def _get_model_instance(self):
        return LinearRegression()

    def _transform_input_features(self, inputs):
        if self.__poly is None:
            self.__poly = PolynomialFeatures(degree = 2)
            return self.__poly.fit_transform(inputs)

        return self.__poly.transform(inputs)