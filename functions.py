import classes
import samples
from typing import Optional

# The purpose of this function is to take a song from user input (str) and return song details (song class)
def find_song(song_name:str) -> Optional[classes.Song]:
    lst=[]
    for song in samples.songs:
        if song_name.lower() == song.title.lower():
            return song
        elif song_name.lower()==song.album.lower() or song_name.lower()==song.artist.lower() or song_name.lower()==song.genre.lower():
            lst.append(song)
        elif song_name=='~':
            lst=samples.songs
    if len(lst)>0:
        if input('do you want want the song list sorted?(y/n): ').lower()=='y':
            sorted_songs(lst)
        for x in lst:
            print(x)
        y=input('Select a song from the list: ')
        return find_song(y)

    print('Song not Found :(')
    return None


# The purpose of this function is to get a rating from user input (str) and return the new song rating (song class)
def rate_song(song:classes.Song):
    condition=False
    while not condition:
        x = input("How would you rate this song between 0 and 5 stars? Enter a number please: ")
        condition=song.add_rating(x)
    y = input("Would you like the view the average song rating? Y/N: ")
    if y.lower() == 'y':
        return song.avg_ratings()

#this function takes class song and a string and return the attribute of the song (song class)
def get_attribute(song,attribute):
    attribute=attribute.lower()
    if attribute=='title':
        return song.title
    elif attribute=='genre':
        return song.genre
    elif attribute=='artist':
        return song.artist
    elif attribute=='album':
        return song.album
    elif attribute=='duration':
        return song.duration.minutes*60+song.duration.seconds
    elif attribute=='rating':
        return song.avg_ratings()

# This function sorts songs by certain attribute (in alphabetical order) (edits the list)
def sorted_songs(lst):
    atr=input("What attribute do you want to sort songs by(title/duration/genre/album/rating/artist): ")
    a=1
    while a<len(lst):
        b=a-1
        while get_attribute(lst[a],atr)<get_attribute(lst[b],atr) and b>=0:
            tmp=lst[a]
            lst[a]=lst[b]
            lst[b]=tmp
            a=b
            b-=1
        a+=1

# Main function call
# Starts program for users
# allows them to use each of the functions provided for various activities
def action():
    current_song=None
    while current_song is None:
        current_song=find_song(input('Enter song you want to search for ("~" for all song): '))
    print(current_song)
    a = input('Would you like to rate this song (Y/N)? ')
    if a.lower() == 'y':
        print(rate_song(current_song))



