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

#Historical Dataset sourced from Kaggle
#Link: https://www.kaggle.com/datasets/mexwell/student-scores

"""
A page of the application.
Page content is imported from the home.md file.

Please refer to https://docs.taipy.io/en/latest/manuals/gui/pages for more details.
"""

from taipy.gui import Markdown
import requests 
import pandas as pd
from decouple import config
from canvasapi import Canvas

canvas_api_url = "https://canvas.instructure.com/"
canvas_token = config('CANVAS_API_KEY')
canvas_course_id = 9291105
sos_login = 108174326168978981092
student_id = 111745213

canvas = Canvas(canvas_api_url, canvas_token)

course = canvas.get_course(canvas_course_id)
assignments_data = course.get_user_in_a_course_level_assignment_data(student_id)
assignment_df = pd.json_normalize(assignments_data)
home = Markdown("pages/home/home.md")

path_to_csv = "data/student-scores.csv"
historical_df = pd.read_csv(path_to_csv)

math_median = historical_df['math_score'].median()
history_median = historical_df['history_score'].median()
physics_median = historical_df['physics_score'].median()
chemistry_median = historical_df['chemistry_score'].median()
biology_median = historical_df['biology_score'].median()
english_median = historical_df['english_score'].median()
geography_median = historical_df['geography_score'].median()
medians = [("Math", math_median), ("History",history_median), ("Physics", physics_median), ("Chemistry", chemistry_median), ("Biology", biology_median), ("English", english_median), ("Geography", geography_median)]
median_data = pd.DataFrame(medians, columns= ["Subject", "Score"])

math_vs_study_hours_data = {
    "Hours": historical_df["weekly_self_study_hours"],
    "Scores": historical_df["math_score"]
}
