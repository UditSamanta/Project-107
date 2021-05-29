import pandas as pd
import plotly.graph_objects as go

dataFrame = pd.read_csv('pixel_math_app_data.csv')
print(dataFrame)

print(dataFrame.groupby('level')['attempt'].mean())
figure = go.Figure(go.Bar(x = dataFrame.groupby('level')['attempt'].mean(), 
y = ['level1', 'level2', 'level3', 'level4'], orientation = 'h'
))
figure.show()