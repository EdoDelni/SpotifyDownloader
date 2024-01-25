from pytube import YouTube, Search
import tkinter as tk
from tkinter import filedialog

def read_song_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        song_list = [line.strip() for line in file.readlines()]
    return song_list


def download_songs(song_list):
    for search_term in song_list:
        try:
            # Search for the song on YouTube using the term
            search_results = Search(search_term)
            first_result = search_results.results[0]

            # Get the video details and download the audio
            video = YouTube(first_result.watch_url)
            video_stream = video.streams.filter(only_audio=True).first()
            video_stream.download(output_path='downloads', filename_prefix='')

            print(f"Downloaded: {video.title}")
        except Exception as e:
            print(f"Error downloading {search_term}: {str(e)}")


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)

def download_from_gui():
    file_path = entry_path.get()
    songs = read_song_list(file_path)
    download_songs(songs)

def download_single_song():
    song_info = {
        'link': entry_link.get(),
        'name': entry_name.get()
    }
    download_songs([song_info])

# GUI setup
root = tk.Tk()
root.title("YouTube Song Downloader")

# Frame for selecting file
frame_file = tk.Frame(root)
frame_file.pack(pady=10)

label_path = tk.Label(frame_file, text="Song List Path:")
label_path.grid(row=0, column=0)

entry_path = tk.Entry(frame_file, width=40)
entry_path.grid(row=0, column=1)

button_browse = tk.Button(frame_file, text="Browse", command=select_file)
button_browse.grid(row=0, column=2)

# Frame for downloading songs
frame_download = tk.Frame(root)
frame_download.pack(pady=10)

label_link = tk.Label(frame_download, text="YouTube Link:")
label_link.grid(row=0, column=0)

entry_link = tk.Entry(frame_download, width=40)
entry_link.grid(row=0, column=1)

label_name = tk.Label(frame_download, text="Song Name:")
label_name.grid(row=1, column=0)

entry_name = tk.Entry(frame_download, width=40)
entry_name.grid(row=1, column=1)

button_download = tk.Button(frame_download, text="Download Single Song", command=download_single_song)
button_download.grid(row=2, column=0, columnspan=2)

# Button to download from file
button_download_file = tk.Button(root, text="Download Songs from File", command=download_from_gui)
button_download_file.pack(pady=20)

root.mainloop()
