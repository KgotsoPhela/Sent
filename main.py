from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext
from io import StringIO
import plotly.graph_objects as go


# FIRST EXPANDER
st.header('Lubanzi Sentiment Analysis')
with st.expander('Analyze Text'):
    text = st.text_input('Text here: ')
    if text:
        blob = TextBlob(text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))


  #  pre = st.text_input('Clean Text: ')
  #  if pre:
  #      st.write(cleantext.clean(pre, clean_all=False, extra_spaces=True,
  #                               stopwords=True, lowercase=True, numbers=True, punct=True))


                                             # SECOND EXPANDER
with st.expander('Analyze CSV'):

    st.write("The uploaded CSV file should be in the following format...")
    data = {
    'ID': range(1, 3),
    'tweets':[
        "Message or customer feedback number 1",
        "Message or customer feedback number 2",    ]
    }
    df = pd.DataFrame(data)
    st.dataframe(df)
    upl = st.file_uploader('Upload file')

    def score(x):
        blob1 = TextBlob(x)
        return blob1.sentiment.polarity

    def analyze(x):
        if x >= 0.5:
            return 'Positive'
        elif x <= -0.2:
            return 'Negative'
        else:
            return 'Neutral'
