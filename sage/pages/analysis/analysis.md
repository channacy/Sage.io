# 🔮 Analysis
# Create your scenario (predict math score based on weekly self study hours):

<|layout|columns=3 1 1 1 1|
<|{scenario}|scenario_selector|>

**Weekly Self Study Hours** <br/>
<|{hours}|number|active={scenario}|>

**Max Score** <br/>
<|{max_capacity}|number|active={scenario}|>

**Number of predictions** <br/>
<|{n_predictions}|number|active={scenario}|>

<br/> <|Save|button|on_action=save|active={scenario}|>
|>

<|{scenario}|scenario|on_submission_change=submission_change|>

<|{predictions_dataset}|chart|x=Hours|y[1]=Historical values|type[1]=bar|y[2]=Predicted values ML|y[3]=Predicted values Baseline|>

# Data Node Exploration

<|layout|columns=1 5|
<|{data_node}|data_node_selector|>

<|{data_node}|data_node|>
|>