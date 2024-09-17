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

    def get_token(self) -> str:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=config["SPOTIPY_CLIENT_ID"],
            client_secret=config["SPOTIPY_CLIENT_SECRET"],
            redirect_uri=config["SPOTIPY_REDIRECT_URI"],
            username=config["SPOTIPY_USERNAME"],
            scope=self.scope,
            show_dialog=True,
            cache_path="token.txt",

        )
        )
        user_id = sp.current_user()["id"]
        return user_id
