import joblib
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, fbeta_score


class ClassificationModel:
    def __init__(self):
      self.__model = None
  
    """Trains the model by reading the data from file, preprocessing and training the model
    """
    def train(self):
      train_inputs, train_outputs, test_inputs, test_outputs = self._split_data()
      self.__model = self._get_model_instance()
      self.__model.fit(
        self._transform_inputs(train_inputs),
        self._transform_outputs(train_outputs),
      )
      return self._evaluate(test_inputs, test_outputs)

    def predict(self, items):
      """Predicts the value of the list of given values

      Args:
        items (array): Items to predict outcomes

      Returns:
          array: List of predicted outcomes
      """      
      inputs = self._transform_inputs(self._preprocess_inputs(pd.DataFrame(items).values))
      return self._inverse_transform_outputs(self.__model.predict(inputs))
    
    def load(self):
      """Loads the serialized model

      Raises:
          Exception: If not implemented
      """
      raise Exception('Method not implemented')

    def save(self):
      """Save a serialized version of the model to a file

      Raises:
          Exception: If not implemented
      """
      raise Exception('Method not implemented')

    def _get_model_instance(self):
      """Gets the internal model instance

      Raises:
          Exception: If not implemented

      Returns:
          object: The model instance
      """
      raise Exception('Method not implemented')

    def _split_data(self):
      """Splits the data into training and test sets

      Raises:
          Exception: If not implemented

      Returns:
          tuple: Returns a tuple containing the following (train_inputs, train_outputs, test_inputs, test_outputs)
      """      
      raise Exception('Method not implemented')

    def _save_model(self, file_path):
      self._save_object(self.__model, file_path)

    def _load_model(self, file_path):
      self.__model = self._load_object(file_path)

    def _save_object(self, obj, file_path):
      """Serializes a given object and saves it to a file

      Args:
          obj (object): Object to store
          file_path (string): Path of the file to store the object
      """      
      joblib.dump(obj, file_path)
    
    def _load_object(self, file_path):
      """Loads a serialized object from a file

      Args:
          file_path (string): Path of the file where object is stored

      Returns:
          Object: The deserialized object
      """      
      return joblib.load(file_path)

    def _preprocess_inputs(self, inputs):
      """Performs some preprocessing tasks to the inputs

      Args:
          inputs (any): Inputs to process

      Returns:
          any: Processed inputs
      """      
      return inputs

    def _preprocess_outputs(self, outputs):
      """Performs some preprocessing tasks to the outputs

       Args:
          outputs (any): Outputs to process

      Returns:
          any: Processed outputs
      """      
      return outputs

    def _transform_inputs(self, inputs):
      """Performs some transformation to inputs before being passed to the ML model

       Args:
          inputs (any): inputs to transform

      Returns:
          any: Transformed inputs
      """ 
      return inputs
    
    def _transform_outputs(self, outputs):
      """Performs some transformation to outputs before being used by ML model

       Args:
          outputs (any): outputs to transform

      Returns:
          any: Transformed outputs
      """ 
      return outputs

    def _inverse_transform_outputs(self, transformed_outputs):
      """Performs some inverse transformation to outputs

       Args:
          transformed_outputs (any): outputs to inverse transform

      Returns:
          any: inverse transformed outputs
      """
      return transformed_outputs

    def _evaluate(self, test_inputs, test_outputs):
      """Evaluates the classification model against the test set

      Args:
        test_inputs (any): Inputs of the test set
        test_outputs (any): Outputs of the test set

      Returns:
          Object: Evaluation metrics

                  accuracy_score
                  confusion_matrix
                  f0.5_score
                  f1_score
                  f2_score
      """      
      transformed_outputs = self._transform_outputs(test_outputs)
      predictions = self.__model.predict(self._transform_inputs(test_inputs))
      length = len(transformed_outputs)

      return {
        'accuracy_score': accuracy_score(
          transformed_outputs,
          predictions,
        ),
        'confusion_matrix': confusion_matrix(
          transformed_outputs,
          predictions,
        ),
        'f0.5_score': fbeta_score(
          transformed_outputs,
          predictions,
          beta = 0.5,
        ),
        'f1_score': fbeta_score(
          transformed_outputs,
          predictions,
          beta = 1.0,
        ),
        'f2_score': fbeta_score(
          transformed_outputs,
          predictions,
          beta = 2.0,
        ),
        'comparison': np.concatenate(
          (
            test_inputs.reshape(length, 1),
            predictions.reshape(length, 1),
            transformed_outputs.reshape(length, 1),
          ),
          1,
        ),
      }