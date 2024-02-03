from youtube import Youtube as yt
import streamlit as st
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt
from googleapiclient.discovery import build

st.title("Target Analysis")

target = st.text_input("Enter the target:")

if target:
    # Providing the API key
    api_key = "AIzaSyDFFVUkYavn8C3BMAssUShtVVz7NAupOlE"

    # Initializing object of youtube class
    target_analysis = yt(api_key)

    # Getting Youtube API service
    youtube_api_service = target_analysis.get_youtube_api_service()

    # Getting video ids
    video_ids = target_analysis.search_videos(youtube_api_service, target)

    # Fetching comment for each video and then storing it into the single pandas dataframe
    data = pd.DataFrame()

    for video_id in video_ids:
        temp = target_analysis.get_data(video_id)
        data = pd.concat([data, temp], ignore_index=True)
        
    # Getting comments
    comments = target_analysis.get_comments(data)

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