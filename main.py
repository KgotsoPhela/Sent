from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext
from io import StringIO
#import pdfkit
import os
#import tempfile
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

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
        options=["Quick guide","Analyze Text", "Analyze CSV"],
        icons=["exclamation-lg", "activity", "bar-chart"],
        orientation="horizontal"
    )
    if selected == "Analyze Text":
        text = st.text_input('Text here: ')
        if text:
            blob = TextBlob(text)
            st.write('Polarity: ', round(blob.sentiment.polarity, 2))
            st.write('Subjectivity: ', round(blob.sentiment.subjectivity, 2))
            st.write(" ")
           
    

        #pre = st.text_input('Clean Text: ')
        #if pre:
        #    st.write(
        #        cleantext.clean(
        #           pre,
        #            clean_all=False,
        #            extra_spaces=True,
        #            stopwords=True,
        #            lowercase=True,
        #            numbers=True,
        #            punct=True,
        #        )
        #    )
    elif selected == "Quick guide":
        st.write("**Polarity:** Positive values indicates positive sentiment, negative values for negative sentiment and 0 for Neutral.")
        st.write("**Subjectivity:** Measures how subjective or objective the text is. High subjectivity score indicates that the text is more opinionated or subjective, low score suggests a more objective or factual nature of the text.")

    elif selected == "Analyze CSV":
        #st.header('Lubanzi Sentiment Analysis - Analyze CSV')

        st.write("The uploaded CSV file should be in the following format...")
        data = {
            'ID': range(1, 3),
            'tweets': [
                "I am not happy with the services you provide",
                "The service and customer support was really great, I am happy",
            ],
        }
        df = pd.DataFrame(data)

        st.table(df)

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

        if upl:
            csv_data = upl.read().decode('utf-8')
            df = pd.read_csv(StringIO(csv_data))
            del df['ID']
            df['score'] = df['tweets'].apply(score)
            df['analysis'] = df['score'].apply(analyze)
            st.write(df.head(10))

            @st.cache
            def convert_df(df):
                # IMPORTANT: Cache the conversion to prevent computation on every rerun
                return df.to_csv(index=False).encode('utf-8')

            csv = convert_df(df)

            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='sentiment.csv',
                mime='text/csv',
            )

            # Calculate the count of each sentiment category
            sentiment_count = df['analysis'].value_counts()

            # Create a bar plot using Plotly
            fig = go.Figure(data=[go.Bar(x=sentiment_count.index, y=sentiment_count.values)])

            # Set the width of the bars
            fig.update_traces(width=0.4)

            # Set the title and axis labels
            fig.update_layout(
                title='Sentiment Analysis Based on The Provided Data',
                xaxis_title='Sentiment',
                yaxis_title='Count'
            )

            # Adjust the size of the plot
            fig.update_layout(
                width=800,  # Set the width of the plot
                height=400  # Set the height of the plot
            )

            # Display the plot in Streamlit
            st.plotly_chart(fig)

            # Summary
            neutral_count = df['analysis'].value_counts()['Neutral']
            positive_count = df['analysis'].value_counts()['Positive']
            negative_count = df['analysis'].value_counts()['Negative']
            st.write(
                "Based on our data we have "
                + str(neutral_count)
                + " Neutral Sentiment(s), "
                + str(negative_count)
                + " Negative Sentiment(s), and "
                + str(positive_count)
                + " Positive sentiment(s)."
            )

            # Generate PDF report
            if st.button('Generate PDF Report'):
                # Create a temporary HTML file to combine the data table and the plot
                temp_file = tempfile.NamedTemporaryFile(suffix='.html', delete=False)
                temp_filename = temp_file.name

                # Write the HTML content to the temporary file
                with open(temp_filename, 'w') as f:
                    f.write(df.to_html())  # Convert the DataFrame to HTML
                    f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))  # Convert the plot to HTML

                # Generate the PDF from the HTML file
                output_pdf = 'report.pdf'
                pdfkit.from_file(temp_filename, output_pdf)

                # Delete the temporary HTML file
                os.remove(temp_filename)

                # Provide the PDF file for download
                st.markdown(f"Download the PDF report: [report.pdf](./{output_pdf})")
elif selected == "Home":
    st.write("Home coming soon")

elif selected == "About":
    st.write("About coming soon...")
