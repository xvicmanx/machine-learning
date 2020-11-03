
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
import salary_prediction_base_model as base_model

class SupportVectorRegressionSalaryPredictionModel(base_model.BaseSalaryPredictionModel):
    __inputs_scaler_filename = 'support_vector_regression_inputs_scaler.sav'
    __outputs_scaler_filename = 'support_vector_regression_outputs_scaler.sav'

    def __init__(self):
        super().__init__()
        self.__inputs_scaler = None
        self.__outputs_scaler = None

    def save(self):
        super().save()
        self._save_object(self.__inputs_scaler, self.__inputs_scaler_filename)
        self._save_object(self.__outputs_scaler, self.__outputs_scaler_filename)

    def load(self):
        super().load()
        self.__inputs_scaler = self._load_object(self.__inputs_scaler_filename)
        self.__outputs_scaler = self._load_object(self.__outputs_scaler_filename)

    def _get_model_instance(self):
        # Kernel: Gaussian Radial Basis Function
        return SVR(kernel = 'rbf')

    def _transform_input_features(self, inputs):
        if self.__inputs_scaler is None:
            self.__inputs_scaler = StandardScaler()
            return self.__inputs_scaler.fit_transform(inputs)

        return self.__inputs_scaler.transform(inputs)
    
    def _transform_outputs(self, outputs):
        reshaped_ouputs = outputs.reshape(len(outputs), 1)
        if self.__outputs_scaler is None:
            self.__outputs_scaler = StandardScaler()
            return self.__outputs_scaler.fit_transform(reshaped_ouputs).ravel()

        return self.__outputs_scaler.transform(reshaped_ouputs).ravel()

    def _inverse_transform_outputs(self, transformed_outputs):
        return self.__outputs_scaler.inverse_transform(transformed_outputs)