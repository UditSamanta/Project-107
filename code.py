import pandas as pd
import plotly.graph_objects as go

dataFrame = pd.read_csv('pixel_math_app_data.csv')
print(dataFrame)

studentData = dataFrame.loc[dataFrame['student_id'] == 'TRL_zet']
print(studentData)

print(studentData.groupby('level')['attempt'].mean())
figure = go.Figure(go.Bar(x = studentData.groupby('level')['attempt'].mean(), 
y = ['level1', 'level2', 'level3', 'level4'], orientation = 'h'
))
figure.show()