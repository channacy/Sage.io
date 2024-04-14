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
Contain the application's configuration including the scenario configurations.

The configuration is run by the Core service.
"""
from taipy import Config, Scope, Frequency
import pandas as pd
from algorithms.algorithms import *
# #############################################################################
# PLACEHOLDER: Put your application's configurations here                     #
#                                                                             #
# Example:                                                                    #
# scenario_config = Config.configure_scenario("placeholder_scenario", [])     #
# Comment, remove or replace the previous lines with your own use case        #
# #############################################################################
## Input Data Nodes
path_to_csv = "data/student-scores.csv"
initial_dataset_cfg = Config.configure_data_node(id="initial_dataset",
                                                 storage_type="csv",
                                                 path=path_to_csv,
                                                 scope=Scope.GLOBAL)
                                                 
hours_cfg = Config.configure_data_node(id="n_hours", default_data=1)

n_predictions_cfg = Config.configure_data_node(id="n_predictions", default_data=1)
max_capacity_cfg = Config.configure_data_node(id="max_capacity", default_data=100)

cleaned_dataset_cfg = Config.configure_data_node(id="cleaned_dataset",
                                                 scope=Scope.GLOBAL) 

predictions_baseline_cfg = Config.configure_data_node(id="predictions_baseline")
predictions_ml_cfg = Config.configure_data_node(id="predictions_ml")

full_predictions_cfg = Config.configure_data_node(id="full_predictions")

metrics_baseline_cfg = Config.configure_data_node(id="metrics_baseline")
metrics_ml_cfg = Config.configure_data_node(id="metrics_ml")

clean_data_task_cfg = Config.configure_task(id="clean_data",
                                            function=clean_data,
                                            input=initial_dataset_cfg,
                                            output=cleaned_dataset_cfg,
                                            skippable=True)

predict_baseline_task_cfg = Config.configure_task(id="predict_baseline",
                                                  function=predict_baseline,
                                                  input=[cleaned_dataset_cfg, n_predictions_cfg, hours_cfg, max_capacity_cfg],
                                                  output=predictions_baseline_cfg)

predict_ml_task_cfg = Config.configure_task(id="task_predict_ml",
                                            function=predict_ml,
                                            input=[cleaned_dataset_cfg,
                                                   n_predictions_cfg, hours_cfg,
                                                   max_capacity_cfg],
                                            output=predictions_ml_cfg)


metrics_baseline_task_cfg = Config.configure_task(id="task_metrics_baseline",
                                            function=compute_metrics,
                                            input=[cleaned_dataset_cfg,
                                                   predictions_baseline_cfg],
                                            output=metrics_baseline_cfg)

metrics_ml_task_cfg = Config.configure_task(id="task_metrics_ml",
                                            function=compute_metrics,
                                            input=[cleaned_dataset_cfg,
                                                   predictions_ml_cfg],
                                            output=metrics_ml_cfg)

full_predictions_task_cfg = Config.configure_task(id="task_full_predictions",
                                            function=create_predictions_dataset,
                                            input=[predictions_baseline_cfg,
                                                   predictions_ml_cfg,
                                                  hours_cfg,
                                                  n_predictions_cfg,
                                                  cleaned_dataset_cfg],
                                            output=full_predictions_cfg)

scenario_cfg = Config.configure_scenario(id="scenario",
                                         task_configs=[clean_data_task_cfg,
                                                       predict_baseline_task_cfg,
                                                       predict_ml_task_cfg,
                                                       metrics_baseline_task_cfg,
                                                       metrics_ml_task_cfg,
                                                       full_predictions_task_cfg],
                                         frequency=Frequency.WEEKLY)