from youtube import Youtube as yt
import streamlit as st
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt
from googleapiclient.discovery import build

st.title("Video Analysis")

video_link = st.text_input("Enter video link:")

if video_link:
    # Providing the API key
    api_key = "AIzaSyDFFVUkYavn8C3BMAssUShtVVz7NAupOlE"

    # Initializing object of youtube class
    video_analysis = yt(api_key)

    # Getting Youtube API service
    youtube_api_service = video_analysis.get_youtube_api_service()

    # Getting video id based on the link
    video_id = video_analysis.get_video_id(video_link)

    # Getting info about the video in Pandas Dataframe
    max_results = st.number_input("Enter number of comments you want to scrape:")

    data = video_analysis.get_data(video_id)


    # Getting comments
    comments = video_analysis.get_comments(data)
    
    # Set up the inference pipeline using a model from the 🤗 Hub
    sentiment_analysis = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")

    predictions = None
    # Making predictions
    if comments:
        predictions = sentiment_analysis(comments)
    else:
        st.write("No commets found")


    # Visualize the sentiments

    sentiment_count = pd.DataFrame(predictions, columns=['label'])
    sentiment_counts = sentiment_count.groupby(['label']).size()

    fig = plt.figure(figsize=(6, 6), dpi=100)
    ax = plt.subplot(111)
    sentiment_counts.plot.pie(ax=ax, autopct='%1.1f%%', startangle=270, fontsize=12, label="")
    st.pyplot(fig)




