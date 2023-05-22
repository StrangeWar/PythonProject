import os
import sys
import threading
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube, Playlist


class YouTubeDownloaderGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("YouTube Downloader")
        self.master.resizable(False, False)

        # Set the window icon
        icon_path = os.path.join(os.path.dirname(__file__), "youtube_icon.ico")
        if os.path.exists(icon_path):
            self.master.iconbitmap(icon_path)

        # Create the URL input label and entry widget
        url_label = tk.Label(self.master, text="Video URL:")
        url_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.url_input = tk.Entry(self.master, width=50)
        self.url_input.grid(row=0, column=1, padx=5, pady=5)

        # Create the resolution selector label and option menu
        resolution_label = tk.Label(self.master, text="Resolution:")
        resolution_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.resolution_variable = tk.StringVar(self.master)
        self.resolution_variable.set("720p")
        resolution_options = ["144p", "240p", "360p", "480p", "720p", "1080p"]
        resolution_menu = tk.OptionMenu(self.master, self.resolution_variable, *resolution_options)
        resolution_menu.grid(row=1, column=1, padx=5, pady=5)

        # Create the output directory label and browse button
        output_directory_label = tk.Label(self.master, text="Output directory:")
        output_directory_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.output_directory_path = tk.StringVar(self.master)
        output_directory_entry = tk.Entry(self.master, textvariable=self.output_directory_path, width=50)
        output_directory_entry.grid(row=2, column=1, padx=5, pady=5)

        browse_button = tk.Button(self.master, text="Browse", command=self.select_output_directory)
        browse_button.grid(row=2, column=2, padx=5, pady=5)

        # Create the download button and status label
        download_button = tk.Button(self.master, text="Download", command=self.start_download)
        download_button.grid(row=3, column=0, padx=5, pady=5)

        self.status_label = tk.Label(self.master, text="")
        self.status_label.grid(row=3, column=1, padx=5, pady=5)

        # Create the progress bar
        self.progress_bar = tk.ttk.Progressbar(self.master, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    def select_output_directory(self):
        # Open a file dialog to select an output directory
        output_directory = filedialog.askdirectory()

        if output_directory:
            self.output_directory_path.set(output_directory)

    def start_download(self):
        video_url = self.url_input.get()
        resolution = self.resolution_variable.get()
        output_directory = self.output_directory_path.get()

        if not video_url:
            self.status_label.config(text="Error: Please enter a video URL")
            return
        elif not resolution:
            self.status_label.config(text="Error: Please select a resolution")
            return
        elif not output_directory:
            self.status_label
        # Disable the download button and clear the status label
        self.status_label.config(text="")
        self.progress_bar["value"] = 0
        download_button = self.master.focus_get()
        download_button["state"] = "disabled"

        # Create a new thread to download the video
        download_thread = threading.Thread(target=self.download_video, args=(video_url, resolution, output_directory))
        download_thread.start()

    def download_video(self, video_url, resolution, output_directory):
        try:
            # Create a YouTube object and get the highest resolution stream
            youtube_video = YouTube(video_url)
            video_stream = youtube_video.streams.filter(res=resolution).first()

            # Create the output directory if it doesn't exist
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)

            # Download the video
            self.status_label.config(text="Downloading...")
            video_filename = video_stream.default_filename
            video_path = os.path.join(output_directory, video_filename)
            video_stream.download(output_directory)

            # Update the status label and progress bar
            self.status_label.config(text="Download complete")
            self.progress_bar["value"] = 100

        except Exception as e:
            # Handle errors and re-enable the download button
            self.status_label.config(text=f"Error: {str(e)}")
            download_button = self.master.focus_get()
            download_button["state"] = "normal"

    def select_playlist_file(self):
        # Open a file dialog to select a playlist file
        playlist_file = filedialog.askopenfilename()

        if playlist_file:
            self.playlist_file_path.set(playlist_file)

    def start_playlist_download(self):
        playlist_file = self.playlist_file_path.get()
        output_directory = self.output_directory_path.get()

        if not playlist_file:
            self.status_label.config(text="Error: Please select a playlist file")
            return
        elif not output_directory:
            self.status_label.config(text="Error: Please select an output directory")
            return

        # Disable the download button and clear the status label
        self.status_label.config(text="")
        self.progress_bar["value"] = 0
        download_button = self.master.focus_get()
        download_button["state"] = "disabled"

        # Create a new thread to download the playlist
        download_thread = threading.Thread(target=self.download_playlist, args=(playlist_file, output_directory))
        download_thread.start()

    def download_playlist(self, playlist_file, output_directory):
        try:
            # Read the video URLs from the playlist file
            with open(playlist_file, "r") as f:
                video_urls = [url.strip() for url in f.readlines()]

            # Create the output directory if it doesn't exist
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)

            # Download each video in the playlist
            for i, video_url in enumerate(video_urls):
                youtube_video = YouTube(video_url)
                video_stream = youtube_video.streams.filter(progressive=True).first()

                self.status_label.config(text=f"Downloading video {i + 1} of {len(video_urls)}...")
                video_filename = video_stream.default_filename
                video_path = os.path.join(output_directory, video_filename)
                video_stream.download(output_directory)

                self.progress_bar["value"] = (i + 1) / len(video_urls) * 100

            # Update the status label and progress bar
            self.status_label.config(text="Download complete")
            self.progress_bar["value"] = 100

        except Exception as e:
            # Handle errors and re-enable the download
            self.status_label.config(text=f"Error: {str(e)}")
            download_button = self.master.focus_get()
            download_button["state"] = "normal"

    def quit(self):
        # Destroy the main window and quit the application
        self.master.destroy()
        sys.exit()


def main():
    # Create and run the application
    root = tk.Tk()
    app = YouTubeDownloaderGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
