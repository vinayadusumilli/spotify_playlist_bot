from web_data_manager import WebDataManager
from spotify_api import SpotifyApi
import datetime as dt

today = dt.datetime.now().date()
playlist_date = ""
check = True
while check:
    try:
        requested_date = input("Which year do you want to be playlist created(YYYY-MM-YY): ")
        list_requested_date = requested_date.split("-")
        date = dt.date(int(list_requested_date[0]), int(list_requested_date[1]), int(list_requested_date[2]))
    except ValueError:
        print("Please enter valid date...")
    except IndexError:
        print("Please enter valid date...")
    else:
        if date > today:
            print("Your selected past date please select present or past date....")
        else:
            playlist_date = str(date)
            check = False

year = playlist_date.split("-")[0]
URL = f"https://www.billboard.com/charts/hot-100/{playlist_date}/"

web_data = WebDataManager(URL)
songs_list = web_data.get_songs()
spotify = SpotifyApi()
spotify.get_token()
spotify_accesser = spotify.create_uris(year=year, song_names=songs_list)
spotify.create_playlist(date=playlist_date)
