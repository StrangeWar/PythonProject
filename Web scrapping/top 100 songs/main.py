import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

Client_ID = "b075dbc36f8546f3b6d337d2af14cf6b"
Client_Secret = "68f535930e5b403fa4f2b7b06d8f4ac9"

date = input("which year do you want to travel to? Type the date in this format yyyy-mm-dd: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
content = response.text
soup = BeautifulSoup(content, "html.parser")

songs = soup.select("li h3")

songs_list = [song.getText().strip() for song in songs[:100]]
song_uris = []

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/",
        client_id=Client_ID,
        client_secret=Client_Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

for song in songs_list:

    result = sp.search(q=f"track:{song}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, public="false", name=f"{date} Billboard 100")

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(URL)
