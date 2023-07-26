import streamlit as st
import openai

# Set up your OpenAI API key
# = "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"
#openai.api_key = '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'

#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



openai.api_key = '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'
# Define the Streamlit app layout
def app():
    # Set the page title
    st.title("SDS Text Sentiment Classifier")

    # Create a text input box for the user to enter a tweet
    tweet_input = st.text_input("Enter a text:")

    # Create a button to trigger the classification
    classify_button = st.button("Classify Sentiment")

    # When the classify button is clicked
    if classify_button:
        # Call the OpenAI API for classification
        parameters = {
            "model": "text-davinci-002",
            "prompt": f"Please classify the sentiment of the following tweet:\n\n{tweet_input}\n\nSentiment:",
            "max_tokens": 100,
        }
        response = openai.Completion.create(**parameters)

        # Extract the predicted sentiment from the API response
        sentiment = response.choices[0].text.strip()

        # Display the predicted sentiment
        st.write("Predicted Sentiment: ", sentiment)

# Run the Streamlit app
if __name__ == "__main__":
    app()



# Set up your OpenAI API key
openai.api_key = "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"

# Define the Streamlit app layout
def app():
    # Set the page title
    st.title("SDS Mini ChatGPT")

    # Create a text input box for the user to enter a question
    question_input = st.text_input("Enter a question:", key="question_input")

    # Initialize the answer variable
    answer = ""

    # When the question_input changes
    if question_input:
        # Call the OpenAI API for Q&A
        prompt = f"What is the answer to the following question:\n\n{question_input}\n\nAnswer:"
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
        )

        # Extract the answer from the API response
        answer = response.choices[0].text.strip()

    # Display the answer
    st.write("Answer: ", answer)

# Run the Streamlit app
if __name__ == "__main__":
    app()




