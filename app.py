import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import youtube as yt
import target_based_analysis_page
import video_based_analyis_page

def main():
    st.title("YouTube Video Sentiment Analysis")

    # Add a choice button to select between search for video or enter direct link
    menu = ["Video Analysis", "Target Analysis"]
    choice = st.sidebar.selectbox("Select Page", menu)

    if choice == "Video Analyis":
        # Create a text input field for the user to enter the search query
        video_based_analyis_page.show()

    elif choice == "Target Analysis":
        target_based_analyis_page.show()
        

if __name__ == "__main__":
    main()
