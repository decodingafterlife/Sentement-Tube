import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import warnings

# Suppress Streamlit warnings
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)

def pie_chart(df):
    """
    Generate a pie chart to visualize sentiment distribution.

    Parameters:
    - df: DataFrame containing 'label' column indicating sentiment.

    Returns:
    None
    """
    sentiment_counts = df.groupby(['label']).size()
    fig, ax = plt.subplots(figsize=(6, 6), dpi=100)
    sentiment_counts.plot.pie(ax=ax, autopct='%1.1f%%', startangle=270, fontsize=12)
    st.pyplot(fig)

def positive_wordcloud(merged_df):
    """
    Generate a word cloud for positive comments.

    Parameters:
    - merged_df: DataFrame containing 'label' and 'comment' columns.

    Returns:
    None
    """
    positive_comments = merged_df['Comment'][merged_df["label"] == 'POS']
    stop_words = ["https", "co", "RT"] + list(STOPWORDS)
    positive_wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=stop_words).generate(str(positive_comments))
    plt.figure()
    plt.title("Positive comments - Wordcloud")
    plt.imshow(positive_wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot()

def negative_wordcloud(merged_df):
    """
    Generate a word cloud for negative comments.

    Parameters:
    - merged_df: DataFrame containing 'label' and 'comment' columns.

    Returns:
    None
    """
    negative_comments = merged_df['Comment'][merged_df["label"] == 'NEG']
    stop_words = ["https", "co", "RT"] + list(STOPWORDS)
    negative_wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=stop_words).generate(str(negative_comments))
    plt.figure()
    plt.title("Negative comments - Wordcloud")
    plt.imshow(negative_wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot()

def neutral_wordcloud(merged_df):
    """
    Generate a word cloud for neutral comments.

    Parameters:
    - merged_df: DataFrame containing 'label' and 'comment' columns.

    Returns:
    None
    """
    neutral_comments = merged_df['Comment'][merged_df["label"] == 'NEU']
    stop_words = ["https", "co", "RT"] + list(STOPWORDS)
    positive_wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=stop_words).generate(str(neutral_comments))
    plt.figure()
    plt.title("Neutral comments - Wordcloud")
    plt.imshow(positive_wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot()




