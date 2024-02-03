import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import youtube as yt
from target_based_analysis_page import target
from video_based_analysis_page import video

def home():
    # Write You code here
    pass

def main():
    st.title("YouTube Video Sentiment Analysis")

    # Add a choice button to select between search for video or enter direct link
    menu = ["Home", "Video Analysis", "Target Analysis"]
    choice = st.sidebar.selectbox("Select Page", menu)

    if (choice != "Video Analysis" and choice != "Target Analysis") or choice == "Home":
        home()

    if choice == "Video Analysis":
        # Create a text input field for the user to enter the search query
        video()

    elif choice == "Target Analysis":
        target()
        

if __name__ == "__main__":
    main()
