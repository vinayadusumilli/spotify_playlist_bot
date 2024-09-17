import spotipy
from dotenv import dotenv_values
from spotipy.oauth2 import SpotifyOAuth

config = {
    **dotenv_values(".env.shared"),
    **dotenv_values(".env.secret")
}


class SpotifyApi:
    def __init__(self):
        self.scope = "playlist-modify-private"
        self.user_id = ""
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=config["SPOTIPY_CLIENT_ID"],
            client_secret=config["SPOTIPY_CLIENT_SECRET"],
            redirect_uri=config["SPOTIPY_REDIRECT_URI"],
            username=config["SPOTIPY_USERNAME"],
            scope=self.scope,
            show_dialog=True,
            cache_path="token.txt",

        )
        )
        self.song_uris = []

    def get_token(self) -> None:
        self.user_id = self.sp.current_user()["id"]

    def create_uris(self, year, song_names):
        for song in song_names:
            result = self.sp.search(q=f"track:{song} year:{year}", type="track")
            try:

                uri = result["tracks"]["items"][0]["uri"]
                self.song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")

    def create_playlist(self, date):
        new_playlist = self.sp.user_playlist_create(
            user=self.user_id,
            name=f"{date}_top_100",
            public=False,
            collaborative=False,
            description=f"Top 100 songs of {date}"
        )
        self.sp.playlist_add_items(playlist_id=new_playlist["id"], items=self.song_uris)
