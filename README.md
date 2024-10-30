# Sage.io

![image](https://github.com/user-attachments/assets/02a418d3-cdf9-4ddd-bef5-743920c66e32)

**Inspiration**
Struggling in classes and finding a solution to help view and receive feedback from academic studies and classes.

**What it does**
shows a dashboard of user's grades and assignments from Canvas as well as historical data containing info about study hours, subject exam scores, extracurriculars, etc. (web app built using taipy)
uses GPT API to recommend studying tips and interactive quizzes based on current performance
trained AI that predicts grade outcomes

**How we built it**
taipy as the web app framework | sklearn & pandas for data analytics
Canvas API to get student + coursework data
AutoRegressive model to predict math exam scores based on weekly number of hours for self studying

**Challenges we ran into**
encountered a bug with producing predicted exam results on the front-end
Accomplishments that we're proud of
clean and navigable UX/UI
connecting to Canvas API
finely tuning the GPT Turbo 3.5 API

**What we learned**
learned how to build a web app using a newly learned framework, taipy
What's next for Sage.io
improving the Analytics page and adding more metrics for prediction (other subject exam scores)
creating an evaluation page showing baseline vs machine learning predicted values
