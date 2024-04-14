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

# Code adapted from the official Taipy documentation
# Source: https://docs.taipy.io/en/release-3.0/knowledge_base/tutorials/complete_application/step_01/step_01/

import taipy as tp
from taipy.gui import Gui, navigate

from taipy import Core, Rest
from pages import *


pages = {
    "/": "<|menu|lov={page_names}|on_action=menu_action|>",
    "Sage-io": home,
	"Analysis": analysis,
	"GPT": feedback,
	"Evaluation": performance
}

page_names = [page for page in pages.keys() if page != "/"]

def menu_action(state, action, payload):
    page = payload["args"][0]
    navigate(state, page)

if __name__ == "__main__":
    rest = Rest()
    # core = Core()
    # core.run()
    # #############################################################################
    # PLACEHOLDER: Create and submit your scenario here                           #
    #                                                                             #
    # Example:                                                                    #
    # from configuration import scenario_config                                   #
    # scenario = tp.create_scenario(scenario_config)                              #
    # scenario.submit()                                                           #
    # Comment, remove or replace the previous lines with your own use case        #
    # #############################################################################

    gui = Gui(pages=pages)
    tp.run(gui, rest, run_browser=False, use_reloader=True, title="Sage.io", port = 5009)
