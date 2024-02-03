import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.title("YouTube Video Sentiment Analysis")

    # Add a choice button to select between search for video or enter direct link
    search_or_direct = st.radio("Choose:", ("Search for Video", "Enter Youtube Link"))

    if search_or_direct == "Search for Video":
        # Create a text input field for the user to enter the search query
        search_query = st.text_input("Enter Search Query")

        # Add logic to search for the video based on the search query
        # This part is not implemented in the provided code snippet

    elif search_or_direct == "Enter Youtube Link":
        video_link = st.text_input("Enter YouTube Video Link")

        # Here you can use the video_link input for further processing

    categories = ['Positive', 'Neutral', 'Negative']
    sentiment_scores = np.random.randint(0, 100, size=len(categories))
    total_score = sum(sentiment_scores)
    probability_positive = sentiment_scores[0] / total_score
    probability_neutral = sentiment_scores[1] / total_score
    probability_negative = sentiment_scores[2] / total_score

    # Box around the probability with dynamic values
    st.markdown(f"""
    <div style='border: 1px solid #e6e6e6; padding: 10px; border-radius: 5px; background-color: #f9f9f9;'>
        <h4>Probability</h4>
        <p>Positive: {probability_positive:.2f}</p>
        <p>Total: {total_score}</p>
        <p>Neutral: {probability_neutral:.2f}</p>
        <p>Negative: {probability_negative:.2f}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style='border: 1px solid #e6e6e6; padding: 10px; border-radius: 5px; background-color: #f9f9f9;'>
        <h4>Sentiment Analysis</h4>
        <p>Sentiment : </p>
    </div>
    """, unsafe_allow_html=True)    
    # For demonstration, generating random sentiment analysis data

    # Display sentiment analysis data as a bar chart
    st.write("Sentiment Analysis Results:")
    fig, ax = plt.subplots()
    ax.bar(categories, sentiment_scores)
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Score')
    st.pyplot(fig)

if __name__ == "__main__":
    main()
