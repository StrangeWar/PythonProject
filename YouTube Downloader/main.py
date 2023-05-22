import os
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from pytube import YouTube, Playlist
from pytube.exceptions import RegexMatchError, VideoUnavailable, VideoPrivate
from tqdm import tqdm
import threading
from ttkthemes import ThemedStyle

def download_video(video_url, resolution, output_path):
    try:
        # Create a YouTube object and get the video stream for the selected resolution
        yt = YouTube(video_url)
        stream = yt.streams.filter(res=resolution).first()

        # Set the output file path to the selected output directory and the video title with the .mp4 extension
        output_file = os.path.join(output_path, f"{yt.title}.mp4")

        # Download the video and update the progress bar
        stream.download(output_path=output_path, filename=yt.title)
        progress_bar["value"] = 100
        status_label.config(text="Video download complete!")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")


    # Download the video
    try:
        stream.download(output_path=output_path, filename=f'{yt.title}.mp4', on_progress=lambda chunk, file_handle, bytes_remaining: progress_bar.update(len(chunk)))
    except:
        progress_bar.close()
        status_label.config(text="Error: download failed")
        return

    # Close the progress bar and update the status label
    progress_bar.close()
    status_label.config(text="Download complete!")

def download_playlist(playlist_url, output_path, status_label):
    # Create a Playlist object
    try:
        playlist = Playlist(playlist_url)
    except (RegexMatchError, VideoUnavailable, VideoPrivate) as e:
        status_label.config(text="Error: " + str(e))
        return

    # Create a progress bar for the download
    progress_bar = tqdm(total=len(playlist.video_urls), desc=f'Downloading playlist {playlist.title}...')

    # Loop through each video in the playlist and download it
    for video_url in playlist.video_urls:
        try:
            video = YouTube(video_url)
            stream = video.streams.filter(res='720p').first()
            stream.download(output_path=output_path, filename=f'{video.title}.mp4')
        except:
            status_label.config(text=f"Error: download failed for video {video_url}")
            continue
        progress_bar.update(1)

    # Close the progress bar and update the status label
    progress_bar.close()
    status_label.config(text="Download complete!")

def start_download_video():
    # Get the YouTube video URL from the user
    url = url_entry.get()

    # Get the selected video resolution
    resolution = resolution_var.get()

    # Get the output directory path from the user
    output_path = output_path_var.get()

    # Start the download in a separate thread
    t = threading.Thread(target=download_video, args=(url, resolution, output_path, status_label))
    t.start()

def start_download_playlist():
    # Get the YouTube playlist URL from the user
    playlist_url = playlist_url_entry.get()

    # Get the output directory path from the user
    output_path = output_path_var.get()

    # Start the download in a separate thread
    t = threading.Thread(target=download_playlist, args=(playlist_url, output_path, status_label))
    t.start()

# Create the GUI window
window = Tk()
window.title("YouTube Video Downloader")
window.geometry("600x400")

# Set the window icon
icon_image = PhotoImage(file="icon.png")
window.iconphoto(True, icon_image)

# Set the window style
style = ThemedStyle(window)


style.set_theme("breeze")

# Add a label for the video URL input
url_label = Label(window, text="Video URL:")
url_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

# Add an entry field for the video URL input
url_entry = Entry(window, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

# Add a label for the resolution selector
resolution_label = Label(window, text="Resolution:")
resolution_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

# Add a combo box for the resolution selector
resolution_var = StringVar()
resolution_var.set("720")
resolution_combo = Combobox(window, textvariable=resolution_var, values=["144", "240", "360", "480", "720", "1080"])
resolution_combo.grid(row=1, column=1, padx=10, pady=10, sticky=W)

# Add a label for the output directory input
output_path_label = Label(window, text="Output Path:")
output_path_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

# Add an entry field for the output directory input
output_path_var = StringVar()
output_path_entry = Entry(window, width=50, textvariable=output_path_var)
output_path_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

# Add a button to open a file dialog for selecting the output directory
def browse_output_path():
    output_path = filedialog.askdirectory()
    output_path_var.set(output_path)

browse_button = Button(window, text="Browse", command=browse_output_path)
browse_button.grid(row=2, column=2, padx=10, pady=10, sticky=W)

# Add a button to start the download
download_button = Button(window, text="Download Video", command=start_download_video)
download_button.grid(row=3, column=1, padx=10, pady=10, sticky=W)

# Add a label for the playlist URL input
playlist_url_label = Label(window, text="Playlist URL:")
playlist_url_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)

# Add an entry field for the playlist URL input
playlist_url_entry = Entry(window, width=50)
playlist_url_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)

# Add a button to start the playlist download
playlist_download_button = Button(window, text="Download Playlist", command=start_download_playlist)
playlist_download_button.grid(row=5, column=1, padx=10, pady=10, sticky=W)

# Add a status label to display messages to the user
status_label = Label(window, text="")
status_label.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky=W)

# Add a progress bar to display the download progress
progress_bar = Progressbar(window, orient=HORIZONTAL, length=400, mode='determinate')
progress_bar.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

# Start the GUI main loop
window.mainloop()
