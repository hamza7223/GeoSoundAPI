import spotipy
from spotipy.oauth2 import SpotifyOAuth
from geopy.geocoders import Nominatim
import geocoder



client_id = "28d1371f14454fe2a5865bdef76b3ce0"

scope = "user-library-read"
scope="user-read-currently-playing"
scope="user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

#gets the current song

result1 = sp.current_user_playing_track()
current_song= result1['item']['name']
current_artist = result1['item']['artists'][0]['name']
print("\nCURRENT TRACK --> "+current_song,"by :",current_artist)

#gets the current location of song being played 
g = geocoder.ip('me')
g.latlng
print("TRACK PLAYED AT --> "+g.city+","+g.state+","+g.country+","+g.postal+"\n")

city=str(g.city)
geolocator = Nominatim(user_agent="GetLoc")

getLoc = geolocator.geocode("Crunch fitness, "+ city)

#print(getLoc.address)







