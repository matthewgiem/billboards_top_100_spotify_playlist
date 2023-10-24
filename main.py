import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from bs4 import BeautifulSoup
from secret_values import spotifyID, spotifySecretID

date = input("what year-month-day do you want the billboard top 100 for? ")


URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

top100 = soup.find_all("div", {"class": "o-chart-results-list-row-container"})


for song in top100:
    print(song.h3.text.strip())