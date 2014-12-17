import spotipy
import sys
import spotipy.util as util
import os
import csv

os.environ["SPOTIPY_CLIENT_ID"] = ""
os.environ["SPOTIPY_CLIENT_SECRET"] = ""
os.environ["SPOTIPY_REDIRECT_URI"] = ''

scope = 'playlist-modify-public user-library-modify user-library-read' 

username = ''
track_id = [0]

token = util.prompt_for_user_token(username, scope)



j=1
songs={}

with open("songs.csv",'rb') as f:
	reader = csv.DictReader(f, delimiter = ',')
	for line in reader:
		songs[j] = {}
		songs[j]['artist'] = line['artist']
		songs[j]['track']= line["track"]

		j+=1




if token:
	sp = spotipy.Spotify(auth=token)
	spotify =spotipy.Spotify()
	sp.trace = False
	playlist_name=raw_input('Enter your playlist name: ')
	playlists = sp.user_playlist_create(username,playlist_name)
	playlist_id = playlists['id']
	print('Playlist Name: ' + playlists['name']+ ' with id: ' +playlist_id)

	for num in songs:
		song_name = songs[num]['track']
		artist_name = songs[num]['artist']
		
		results = spotify.search(q = 'track:' + song_name+' + artist:'+artist_name,limit =1, type = 'track')
		
		song_id = results['tracks']['items'][0]['uri']
		track_id[0]=song_id
		sp.user_playlist_add_tracks(username, playlist_id, track_id, position = None)
	
	

else:
	print "Can't get token for", username


#song_name = results['tracks']['items'][0]['name']
#song_artist = results['tracks']['items'][0]['artists'][0]['name']
#song_id = results['tracks']['items'][0]['id']
#song_album = results['tracks']['items'][0]['album']['name']


#songs ={
#	song_id:{
#	'artist': song_artist,
#	'track': song_name,
#	'album':song_album	
#	}
	
#}

