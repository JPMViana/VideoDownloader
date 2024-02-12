#########################################################################################################
############################ Created by: JOAO PEDRO on 2024-02-11 #######################################
#########################################################################################################

from pytube import YouTube

def download_video(url):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution
    try:
        video.download(videos)
        print(f"Video {yt.title} downloaded successfully")    
    except:
        print("An error occurred")  


def download_audio(url):
    yt = YouTube(url)
    audio = yt.streams.get_audio_only()
    try:
        audio.download(audios)
        print(f"Audio {yt.title} downloaded successfully")
    except: 
        print("An error occurred")


def main():
    url = input("Enter the video URL: ")
    path = input("Enter the path to save the file: ")
    print("1. Download video\n2. Download audio")
    option = int(input("Enter the option: "))
    if option == 1:
        download_video(url, path)
    elif option == 2:
        download_audio(url, path)
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
