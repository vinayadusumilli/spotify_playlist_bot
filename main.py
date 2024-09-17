from web_data_manager import WebDataManager
from spotify_api import SpotifyApi

requested_date = input("Which year do you want to be playlist created(YYYY-MM-YY): ")
URL = f"https://www.billboard.com/charts/hot-100/{requested_date}/"

web_data = WebDataManager(URL)
songs_list = web_data.get_songs()
spotify = SpotifyApi()
spotify_userid = spotify.get_token()
