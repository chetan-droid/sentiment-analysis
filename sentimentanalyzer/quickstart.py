import streamlit as st
import pandas as pd
import numpy as np
import requests
from plotly.offline import iplot
import plotly.graph_objs as go
import plotly.express as px
# from pandas.io.json import json_normalize
# from streamlit. import StopExecution, RerunException

fig = go.Figure()
st.write("""
# Twitter Sentiment Analysis App

""")

st.write('Sentiment analysis is the interpretation and classification of emotions (positive, negative and neutral)')
st.set_option('deprecation.showfileUploaderEncoding', False)

st.sidebar.header('User Input(s)')
st.sidebar.subheader('Single Tweet analysis')
single_review = st.sidebar.text_input('Enter single tweet below:')

st.sidebar.subheader('Multi Tweets Analysis')
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
    count_positive = 0
    count_negative = 0
    count_neutral = 0
    for i in range(input_df.shape[0]):
        url = 'http://127.0.0.1:8000/analyzer/?text='+str(input_df.loc[i])
        r = requests.get(url)
        result = r.json()["sentiment"]
        probabilities = r.json()["probabilities"]
        if result == 'positive':
            count_positive+=1
        elif result == 'negative':
            count_negative+=1
        else:
            count_neutral+=1
    
    x = ["Positive", "Negative", "Neutral"]
    y = [count_positive, count_negative, count_neutral]

    layout = go.Layout(
        title= 'Multiple Tweet Anaysis',
        xaxis= dict(title = 'Catergory'),
        yaxis= dict(title = "Number of tweets"),)

    fig.update_layout(dict1 = layout, overwrite=True)
    fig.add_trace(go.Bar(name= "Multi Tweets", x=x, y=y))
    st.plotly_chart(fig, use_container_width=True)

    #Pie Chart
    pie_data = [count_positive, count_negative, count_neutral]
    pie_labels = ['Positive', 'Negative', 'Neutral']
    colors = ['#66CC99', '#FF6666', '#FFCC99']
    fig2 = go.Figure(data=[go.Pie(labels=pie_labels, values=pie_data, hole=.4, marker_colors=colors)])
    fig2.update_layout(title='Sentiment Distribution of Multiple Tweets', showlegend=False)
    st.plotly_chart(fig2, use_container_width=True)

elif single_review:
    url = 'http://127.0.0.1:8000/analyzer/?text='+single_review
    r = requests.get(url)
    print("L2")
    print(r.content)
    result = r.json()["sentiment"]
    probabilities = r.json()["probabilities"]
    if result == 'positive':
        st.write("""#Great! This tweet is positive 😊""")
        score = 1
    elif result == 'negative':
        st.write("""#Oops! This tweet is negative ☹""")
        score = -1
    else:
        st.write(""" Tweet is neither postive nor negative, it's neutral😑""")
        score = 0
    st.write(f"Probability: {probabilities: .2f}")

    # create a gauge chart
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        title = {'text': "Sentiment Score"},
        gauge = {
            'axis': {'range': [-1, 1], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [-1, -0.5], 'color': 'red'},
                {'range': [-0.5, 0.5], 'color': 'yellow'},
                {'range': [0.5, 1], 'color': 'green'}],
            'threshold': {
                'line': {'color': "white", 'width': 4},
                'thickness': 0.75,
                'value': score}
        }))
    st.plotly_chart(fig, use_container_width=True)

else:
    st.write("""## ← Enter user input from the sidebar to see the nature of the tweet.""")

st.sidebar.subheader("""Created by BACET❤""")
st.sidebar.image("D:\Projects\Report\logo-tweet.jpg", width=600)
