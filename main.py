from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext
from io import StringIO
import pdfkit
import os
import tempfile
import plotly.graph_objects as go
#from streamlit_option_menu import option_menu

# Set up the sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Analysis", "About"],
        icons=["house", "bar-chart", "book"],
        menu_icon="list"
    )

# Main app content
if selected == "Analysis":
    st.header('Lubanzi Sentiment Analysis')
    selected = option_menu(
        menu_title=None,
        options=["Analyze Text", "Analyze CSV"],
        icons=["activity", "bar-chart"],
        orientation="horizontal"
    )
