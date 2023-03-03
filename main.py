from pytube import YouTube
import moviepy.editor as mp
import os
import pyfiglet

# Define variables 
author_name = "Muhamad Iqbal Nurmanditya"
github_url = "https://github.com/iqbalmind"
linkedin_url = "https://www.linkedin.com/in/iqbalmind/"
text = "YTDLpython"

ascii_art = pyfiglet.figlet_format(text)


def main_menu():
    print(ascii_art)
    print("Welcome to the Python YouTube downloader!")
    print("Please select an option:")
    print("1. Download video")
    print("2. Convert video to mp3")
    print("3. Information")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        download_video()
        main_menu()  # Repeat the process
    elif choice == "2":
        convert_to_mp3()
        main_menu()  # Repeat the process
    elif choice == "3":
        info()
        main_menu()  # Repeat the process
    elif choice == "4":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice.")
        main_menu()


def download_video():

    # Enter the YouTube video URL
    url = input("Enter the YouTube video URL: ")

    # Create a YouTube object
    yt = YouTube(url)

    # Display video information
    print("Title:", yt.title)
    print("Views:", yt.views)

    # Select video resolution
    print("Please select the video resolution:")
    print("1. 360p")
    print("2. 720p")
    print("3. 1080p")
    print("4. 2160p")
    res_choice = input("Enter your choice (1-4): ")

    # Get the video with the selected resolution
    if res_choice == "1":
        video = yt.streams.filter(res="360p").first()
    elif res_choice == "2":
        video = yt.streams.filter(res="720p").first()
    elif res_choice == "3":
        video = yt.streams.filter(res="1080p").first()
    elif res_choice == "4":
        video = yt.streams.filter(res="2160p").first()
    else:
        print("Invalid choice.")
        return

    # Download the video
    print(f"Downloading {yt.title}...")
    video.download()

    pass


def convert_to_mp3():

    # Convert the video to mp3
    # Enter the YouTube video URL
    url = input("Enter the YouTube video URL: ")

    # Create a YouTube object
    yt = YouTube(url)

    # Display video information
    print("Title:", yt.title)
    print("Views:", yt.views)
    print("Channel:", yt.author)
    print("Published on:", yt.publish_date)

    # Select video resolution
    print("Please select the video resolution:")
    print("1. 360p")
    print("2. 720p")
    print("3. 1080p")
    print("4. 2160p")
    res_choice = input("Enter your choice (1-4): ")

    # Get the video with the selected resolution
    if res_choice == "1":
        video = yt.streams.filter(res="360p").first()
    elif res_choice == "2":
        video = yt.streams.filter(res="720p").first()
    elif res_choice == "3":
        video = yt.streams.filter(res="1080p").first()
    elif res_choice == "4":
        video = yt.streams.filter(res="2160p").first()
    else:
        print("Invalid choice.")
        return

    print("Converting video to mp3...")
    clip = mp.VideoFileClip(video.default_filename)
    clip.audio.write_audiofile(video.default_filename[:-4] + ".mp3")
    pass

def info():
    print("Author Name:", author_name)
    print("GitHub URL:", github_url)
    print("LinkedIn URL:", linkedin_url)
    print("YTDLpython is a Python package that provides a simple way to download YouTube videos using the YouTube Data API. It uses the Pytube library under the hood to download videos and provides a command-line interface (CLI) for ease of use.")
    input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
