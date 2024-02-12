#########################################################################################################
############################ Created by: JOAO PEDRO on 2024-02-11 #######################################
#########################################################################################################

from pytube import YouTube
import streamlit as st

def check_url():
    if st.session_state.url == "":
        return
    try:
        url = st.session_state.url
        yt = YouTube(url)
    
    except:
        st.error("Invalid URL")
        return
    
    check = yt.check_availability()
    if check == False:
        st.error("The Video download is not available")
    else:
        show_video_info(yt)

def show_video_info(yt):
    tbmImg = st.image(yt.thumbnail_url)
    tumbTitle = st.subheader(yt.title)

def download_video():
    url = st.session_state.url
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download()
    st.success("Video downloaded successfully")

def download_audio():
    url = st.session_state.url
    yt = YouTube(url)
    audio = yt.streams.get_audio_only() 
    audio.download()
    st.success("Audio downloaded successfully")

st.set_page_config(
    page_title="Youtube Downloader", 
    page_icon="🎵", 
    layout="centered", 
    # initial_sidebar_state="expanded"
    )


st.title("Youtube Downloader" )
st.subheader("Download videos and audios from Youtube in best quality")
st.text("Version 1.0 Developed by Joao Pedro")


st.text_input("URL:", key="url" , placeholder="Paste the Video URL and press 'Enter'" , on_change=check_url)

if st.button("Download Video"):
    download_video()

if st.button("Download Audio"):
    download_audio()


st.divider()
st.text("Fortaleza, Brazil 2024/02/12")


