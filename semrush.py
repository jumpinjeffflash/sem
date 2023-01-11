@st.experimental_memo

def get_chart_92107987():
import plotly.graph_objects as go

rawData = [
{'direct': 74,'search': 21,'PSR': 5,'label':'uship'},
{'direct': 92,'search': 7,'PSR': 2,'label':'shiply'},
{'direct': 37,'search': 62,'PSR': 1,'label':'goshare'},
{'direct': 61,'search': 35,'PSR': 4,'label':'flockfreight'},
{'direct': 92,'search': 3,'PSR': 6,'label':'citizenshipper'},
];

def makeAxis(title, tickangle):
return {
title': title,
titlefont': { 'size': 20 },
tickangle': tickangle,
tickfont': { 'size': 15 },
tickcolor': 'rgba(0,0,0,0)',
ticklen': 5,
showline': True,
showgrid': True
}

fig = go.Figure(go.Scatterternary({
mode': 'markers',
a': [i for i in map(lambda x: x['journalist'], rawData)],
b': [i for i in map(lambda x: x['developer'], rawData)],
c': [i for i in map(lambda x: x['designer'], rawData)],
text': [i for i in map(lambda x: x['label'], rawData)],
marker': {
symbol': 100,
color': '#DB7365',
size': 14,
line': { 'width': 2 }
}
}))

fig.update_layout({
ternary': {
sum': 100,
aaxis': makeAxis('Journalist', 0),
baxis': makeAxis('<br>Developer', 45),
caxis': makeAxis('<br>Designer', -45)
},
annotations': [{
showarrow': False,
text': 'Simple Ternary Plot with Markers',
x': 0.5,
y': 1.3,
font': { 'size': 15 }
}]
})


tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
st.plotly_chart(fig, theme="streamlit")
with tab2:
st.plotly_chart(fig, theme=None)