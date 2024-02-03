from youtube import Youtube as yt
import streamlit as st
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt
from googleapiclient.discovery import build
import analysis
from wordcloud import WordCloud, STOPWORDS
# import warnings

# # Suppress Streamlit warnings
# st.set_option('deprecation.showfileUploaderEncoding', False)
# st.set_option('deprecation.showPyplotGlobalUse', False)

def video():

    st.title("Video Analysis")

    video_link = st.text_input("Enter video link:")

    if video_link:
        # Providing the API key
        api_key = "AIzaSyCkAd4mhamfZoxGmW5_32Hvi-WZaCPHg0o"

        # Initializing object of youtube class
        video_analysis = yt(api_key)

        # Getting Youtube API service
        youtube_api_service = video_analysis.get_youtube_api_service()

        # Getting video id based on the link
        video_id = video_analysis.get_video_id(video_link)

        # Getting max number of comments from the user
        max_results = st.number_input("Enter maximum number of comments", value=100, min_value = 1, max_value = 200)

        button = st.button("Analyze")

        if button:

            data = video_analysis.get_data(video_id, max_results)

            # if data == None:
            #     st.write("HTTP Error!!! Access Denied")
            #     return

            video_details = video_analysis.get_video_details(youtube_api_service, video_id)

            if video_details:
                title = video_details['title']
                description = video_details['description']

                st.write("Title: " + title)
                # st.write(f"Description: {description}")

            st.dataframe(data, hide_index=True)


            # Getting comments
            comments = video_analysis.get_comments(data)
            
            # Set up the inference pipeline using a model from the Hub
            sentiment_analysis = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")

            predictions = None
            # Making predictions
            if comments:
                predictions = sentiment_analysis(comments)
            else:
                st.write("No commets found")


            # Visualize the sentiments

            df2 = pd.DataFrame(predictions)

            # Visualize the sentiments
            df = analysis.pie_chart(df2)
            # Merge the DataFrames column-wise
            merged_df = pd.concat([data, df2], axis=1)

            # Plotting the wordcloud for the particular category
            analysis.positive_wordcloud(merged_df)
            analysis.negative_wordcloud(merged_df)
            analysis.neutral_wordcloud(merged_df)

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

            




