# Copyright 2021-2024 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

"""
This file is designed to contain the various Python functions used to configure tasks.

The functions will be imported by the __init__.py file in this folder.
"""

# ##################################################################################################################
# PLACEHOLDER: Put your Python functions here                                                                      #
#                                                                                                                  #
# Example:                                                                                                         #
# def place_holder_algorithm():                                                                                    #
#     pass                                                                                                         #
# Comment, remove or replace the previous lines with your own use case                                             #
# ##################################################################################################################

#  used an AutoRegressive model rather than a pure ML model 
from statsmodels.tsa.ar_model import AutoReg
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

def clean_data(initial_dataset: pd.DataFrame):
    print("     Cleaning data")
    cleaned_dataset = initial_dataset.copy()
    return cleaned_dataset

def predict_baseline(cleaned_dataset: pd.DataFrame, n_predictions: int, hours: int, max_score: int):
    print("     Predicting baseline")
    train_dataset = cleaned_dataset

    predictions = train_dataset['math_score'][-n_predictions:].reset_index(drop=True)
    predictions = predictions.apply(lambda x: min(x, max_score))
    return predictions

def predict_ml(cleaned_dataset: pd.DataFrame, n_predictions: int, hours: int, max_score: int):
    print("     Predicting with ML")
    # Select the train data
    train_dataset = cleaned_dataset

    # Fit the AutoRegressive model
    model = AutoReg(train_dataset["math_score"], lags=7).fit()

    # Get the n_predictions forecasts
    predictions = model.forecast(n_predictions).reset_index(drop=True)
    predictions = predictions.apply(lambda x: min(x, max_score))
    return predictions

def compute_metrics(historical_data, predicted_data):
    historical_to_compare = historical_data[-len(predicted_data):]['Value']
    rmse = mean_squared_error(historical_to_compare, predicted_data)
    mae = mean_absolute_error(historical_to_compare, predicted_data)
    return rmse, mae

def create_predictions_dataset(predictions_baseline, predictions_ml, day, n_predictions, cleaned_data):
    print("Creating predictions dataset...")

    ...
    predictions_dataset = pd.concat([
        historical_data["weekly_self_study_hours"],
        historical_data["math_score"].rename("Historical values"),
        create_series(predictions_ml, "Predicted values ML"),
        create_series(predictions_baseline, "Predicted values Baseline")
    ], axis=1)

    return predictions_dataset