from pytube import YouTube, Search

def read_song_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        song_list = [line.strip() for line in file.readlines()]
    return song_list

def download_songs(song_list):
    for song_name in song_list:
        try:
            # Search for the song on YouTube
            search_results = Search(song_name)
            first_result = search_results.results[0]

            # Get the video details and download the audio
            video = YouTube(first_result.watch_url)
            video_stream = video.streams.filter(only_audio=True).first()
            video_stream.download(output_path='downloads', filename_prefix='')

            print(f"Downloaded: {song_name}")
        except Exception as e:
            print(f"Error downloading {song_name}: {str(e)}")

if __name__ == "__main__":
    # Use double backslashes or a raw string to avoid the unicode error
    songs_file_path = r'C:\Users\edelnista\Documents\songs.txt'

    # Read song list from the file
    songs = read_song_list(songs_file_path)

    # Download songs
    download_songs(songs)
