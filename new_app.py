import streamlit as st
from transformers import pipeline

# Load the sentiment analysis model
sentiment = pipeline("sentiment-analysis")

# Define the Streamlit app
def app():
    # Set the app title
    st.title("Sentiment Analysis App")

    # Add a text input for the user to enter the text to analyze
    text = st.text_input("Enter some text:")

    # Analyze the sentiment of the text when the user clicks the button
    if st.button("Analyze"):
        result = sentiment(text)[0]
        st.write('Sentiment:', result['label'])
        st.write('Confidence:', result['score'])

# Run the app
if __name__ == "__main__":
    app()