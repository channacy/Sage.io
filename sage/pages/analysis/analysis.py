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
A page of the application.
Page content is imported from the analysis.md file.

Please refer to https://docs.taipy.io/en/latest/manuals/gui/pages for more details.
"""

from taipy.gui import Markdown, notify
import datetime as dt
import pandas as pd

scenario = None
data_node = None
hours = 1
n_predictions = 40
max_capacity = 200

predictions_dataset = {"Hours":[0], 
                       "Predicted values ML":[0],
                       "Predicted values Baseline":[0],
                       "Historical values":[0]}

def submission_change(state, submittable, details: dict):
    if details['submission_status'] == 'COMPLETED':
        notify(state, "success", 'Scenario completed!')
        state['scenario'].on_change(state, 'scenario', state.scenario)
    else:
        notify(state, "error", 'Something went wrong!')

def save(state):
    print("Saving scenario...")
    # Get the currently selected scenario

    # Change the default parameters by writing in the Data Nodes
    state.scenario.hours.write(int(state.hours))
    state.scenario.n_predictions.write(int(state.n_predictions))
    state.scenario.max_capacity.write(int(state.max_capacity))
    notify(state, "success", "Saved!")

def on_change(state, var_name, var_value):
    if var_name == "scenario" and var_value:
        state.hours = state.scenario.hours.read()
        state.n_predictions = state.scenario.n_predictions.read()
        state.max_capacity = state.scenario.max_capacity.read()

        if state.scenario.full_predictions.is_ready_for_reading:
            state.predictions_dataset = state.scenario.full_predictions.read()
        else:
            state.predictions_dataset = predictions_dataset
            
analysis = Markdown("pages/analysis/analysis.md")