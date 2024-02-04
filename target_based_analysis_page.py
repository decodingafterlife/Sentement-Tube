from youtube import Youtube as yt
import streamlit as st
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt
from googleapiclient.discovery import build
import analysis
from wordcloud import WordCloud, STOPWORDS
import warnings

# Suppress Streamlit warnings
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)

def target():

    st.title("Target Analysis")

    target = st.text_input("Enter the target:")

    if target:
        # Providing the API key
        api_key = "your-api-key"

        # Initializing object of youtube class
        target_analysis = yt(api_key)

        # Getting Youtube API service
        youtube_api_service = target_analysis.get_youtube_api_service()

        

        # Getting max number of comments from the user
        max_results = st.number_input("Enter maximum number of videos", value=5, min_value = 1, max_value = 20)

        button = st.button("Analyze")

        if button:

            # Getting video ids
            video_ids = target_analysis.search_videos(youtube_api_service, target, max_results)

            # Fetching comment for each video and then storing it into the single pandas dataframe
            data = pd.DataFrame()

            # Fetching comment for the each video
            for video_id in video_ids:
                temp = target_analysis.get_data(video_id)
                data = pd.concat([data, temp], ignore_index=True)

            # Displaying the title of each video
            target_details = []
            for video_id in video_ids:
                target_details.append(target_analysis.get_video_details(youtube_api_service, video_id))
            
            st.write("Titles:")
            for video in target_details:
                if video:
                    title = video['title']
                    st.write(title)

            #showing fetched comments
            st.dataframe(data, hide_index=True)
                
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

            df2 = pd.DataFrame(predictions)

            # Visualize the sentiments
            df = analysis.pie_chart(df2)
            # Merge the DataFrames column-wise
            merged_df = pd.concat([data, df2], axis=1)

            # Plotting the wordcloud for the particular category
            analysis.positive_wordcloud(merged_df)
            analysis.negative_wordcloud(merged_df)
            analysis.neutral_wordcloud(merged_df)

            # Displaying results
            st.dataframe(merged_df, hide_index=True)


            # Download the data
            @st.cache_data
            def convert_df(df):
                return df.to_csv().encode('utf-8')

            csv = convert_df(merged_df)

            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='large_df.csv',
                mime='text/csv',
            )
