import streamlit as st
from PIL import Image   

def about_us():

    st.header("About Us")
    
    st.markdown("""<div style='border: 1px solid #e6e6e6; padding: 10px; border-radius: 5px;'><h2>Welcome to Sentiment-Tube</h2>

Ever watched a YouTube video and wondered what others really think about it? With YouTube removing the dislike button, it's become harder to gauge public sentiment. But worry not! Our website is here to help.

Simply paste the YouTube link or enter the title, and we'll analyze the comments to provide you with a clear understanding of the video's sentiment. Whether it's positive, negative, or neutral, we've got you covered.

Say goodbye to uncertainty and make informed decisions about the content you watch. Try it now and discover the true sentiment behind any YouTube video!
</div>
""", unsafe_allow_html=True)
