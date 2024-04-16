import tkinter as tk
import subprocess

def download_song(song_name):
    try:
        search_query = f'ytsearch:{song_name} audio'
        cmd = ['youtube-dl', '--extract-audio', '--audio-format', 'mp3', '--output', 'downloads/%(title)s.%(ext)s', search_query]
        subprocess.run(cmd, check=True)
        print(f"Downloaded: {song_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading {song_name}: {str(e)}")

def download_from_gui():
    song_name = entry_song_name.get()
    download_song(song_name)

# GUI setup
root = tk.Tk()
root.title("YouTube Song Downloader")

# Frame for downloading songs
frame_download = tk.Frame(root)
frame_download.pack(pady=10)

label_song_name = tk.Label(frame_download, text="Song Name:")
label_song_name.grid(row=0, column=0)

entry_song_name = tk.Entry(frame_download, width=40)
entry_song_name.grid(row=0, column=1)

button_download_song = tk.Button(frame_download, text="Download Song", command=download_from_gui)
button_download_song.grid(row=1, column=0, columnspan=2)

root.mainloop()
