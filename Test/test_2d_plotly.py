import numpy as np
import plotly.graph_objects as go


fig = go.Figure()

x = np.linspace(-2 + 0.01, 0.25 - 0.01, 500)
y = 0

px = np.array([])
py = np.array([])

acc = 25
for n in range(0, acc):
    y = y ** 2 + x
    px = np.append(px, x)
    py = np.append(py, y)


fig.add_trace(
    go.Scatter(
        x=px, y=py,
        hoverinfo='skip',
        mode='markers',
        showlegend=False,
        marker=dict(
            size=1,
            color='blue'
        )
    )
)

fig.show()
