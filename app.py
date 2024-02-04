import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import youtube as yt
from target_based_analysis_page import target
from video_based_analysis_page import video
from aboutus import about_us
from PIL import Image 

def home():
    # st.write("Understanding Audience Feedback Effectively")

    st.markdown("<h3 style='text-align: center;'>Understanding Audience Feedback Effectively</h3>", unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.markdown("""<div style='border: 1px solid #e6e6e6; padding: 10px; border-radius: 5px;'><h2>Welcome to Sentiment-Tube</h2>
Here we delve into the heartbeat of YouTube conversations. Our cutting-edge sentiment analysis tools decode the emotions hidden in every comment, offering a unique perspective on audience engagement and content reception. Analyzing sentiments in comments provides valuable insights into audience reactions, preferences, and opinions, which can be beneficial for content creators, marketers, and platform administrators
""", unsafe_allow_html=True)

    pass

def main():
    im = Image.open('logo.png')#Title and App Icon
    st.set_page_config(page_title="Sentiment-Tube", page_icon = im)
    
    hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
    st.markdown(hide_default_format, unsafe_allow_html=True)#remove the Menu Button and Streamlit Icon
    st.image('logo.png', width=700)

    menu = ["Home", "Video Analysis", "Target Analysis", "About"]
    choice = st.sidebar.selectbox("Select Page", menu)

    if choice == "Home":
        home()
    elif choice == "Video Analysis":
        video()
    elif choice == "Target Analysis":
        target()
    elif choice == "About":
        about_us()
    
if __name__ == "__main__":
    main()
