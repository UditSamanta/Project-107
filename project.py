import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

dataFrame = pd.read_csv('pixel_math_app_data.csv')
print(dataFrame)

print(dataFrame.groupby(['student_id', 'level'])['attempt'].mean())
mean = dataFrame.groupby(['student_id', 'level'])['attempt'].mean()
figure = px.scatter(mean, x = 'student_id', y = 'level', color = 'attempt')
figure.show()