from typing import Optional



class Song:
    # Initialize a new Song object.
    # input: title as a string
    # input: artist as a string
    # input: album as a string
    # input: duration as a Duration object
    # input: genre as a string
    # input: track_no as an integer
    def __init__(self,title:str,artist:str,album:str,duration,genre:str,track_no:int):
        self.title=title
        self.artist=artist
        self.album=album
        self.duration=duration
        self.genre=genre
        self.track_no=track_no
        self.ratings=[]

    # The purpose of this function is to add a rating to the Song object.
    # input: rating as a float (value between 0 and 5)
    # output: boolean indicating success or error message if invalid
    def add_rating(self,rating):
        try:
            rating=float(rating)
            if 0 <= rating <= 5:
                self.ratings.append(rating)
                return True
            else:
                print("Invalid entry. Please enter a number between 0 and 5")
        except ValueError or TypeError as e:
            print('Invalid input: ' ,e)

    # The purpose of this function is to compute and return the average of all ratings for the Song object.
    # input: none
    # output: optional float representing the average rating or a string if no ratings are present
    def avg_ratings(self) -> Optional[float] or Optional[str]:
        if self.ratings:
            return round(sum(self.ratings) / len(self.ratings), 2)
        else:
            a = "No ratings yet"
            print(a)

    # Generate a string representation of the Song object and its attributes.
    # input: Song object
    # output: string representation including title, artist, album, duration, genre, track_no, and average rating
    def __repr__(self) -> str:
        return '\nSong Title: {}\nArtist: {}\nAlbum: {}\nDuration: {}\nGenre: {}\nTrack_No: {}\navg_ratings: {}\n'.format(self.title, self.artist,self.album,self.duration,self.genre,self.track_no,self.avg_ratings())

class Duration:
    # Initialize a new Duration object.
    # input: minutes as an integer
    # input: seconds as an integer
    def __init__(self, minutes:int, seconds: int):
        self.minutes = minutes
        self.seconds = seconds


    # Provide a developer-friendly string representation of the object.
    # input: Duration for which a string representation is desired.
    # output: string representation
    def __repr__(self) -> str:
        return 'Duration({}, {})'.format(self.minutes, self.seconds)


    # Compare the Duration object with another value to determine equality.
    # input: Duration against which to compare
    # input: Another value to compare to the Duration
    # output: boolean indicating equality
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Duration and
                self.minutes == other.minutes and
                self.seconds == other.seconds)
