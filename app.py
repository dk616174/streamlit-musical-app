import streamlit as st
import functions
import classes
import samples

st.set_page_config(page_title="Song App", layout="centered")
st.title("Song Lookup and Rating App")

# Input box
song_query = st.text_input("Search by song title, artist, album, or genre:")

# Helper to display song info nicely
def display_song(song: classes.Song):
    avg_rating = song.avg_ratings() if song.avg_ratings() is not None else "No ratings yet"
    duration = f"{song.duration.minutes}m {song.duration.seconds}s"
    st.markdown(f"""
    **🎶 Title:** {song.title}  
    **🎤 Artist:** {song.artist}  
    **💿 Album:** {song.album}  
    **⏱️ Duration:** {duration}  
    **🎧 Genre:** {song.genre}  
    **🔢 Track #:** {song.track_no}  
    **⭐ Avg. Rating:** {avg_rating}
    """, unsafe_allow_html=True)

# Search logic
if song_query:
    matching_songs = []

    # If '~', show all
    if song_query.strip() == "~":
        matching_songs = samples.songs
    else:
        for song in samples.songs:
            if (song_query.lower() in song.title.lower() or
                song_query.lower() in song.artist.lower() or
                song_query.lower() in song.album.lower() or
                song_query.lower() in song.genre.lower()):
                matching_songs.append(song)

    if matching_songs:
        song_titles = [f"{s.title} by {s.artist}" for s in matching_songs]
        selection = st.selectbox("Select a song to view details:", song_titles)
        current_song = matching_songs[song_titles.index(selection)]

        # Display the song
        display_song(current_song)

        # Rating section
        st.subheader("Rate This Song")
        new_rating = st.slider("Your Rating:", 0.0, 5.0, 3.0, 0.5)
        if st.button("Submit Rating"):
            current_song.add_rating(new_rating)
            st.success(f"Thanks! You rated this song {new_rating}/5")

        if st.button("Show Average Rating"):
            avg = current_song.avg_ratings()
            st.info(f"⭐ Average Rating: {avg if avg else 'No ratings yet.'}")
    else:
        st.warning("No matching songs found.")

st.header("➕ Add a New Song")

with st.form("add_song_form"):
    title = st.text_input("Title")
    artist = st.text_input("Artist")
    album = st.text_input("Album")
    minutes = st.number_input("Duration Minutes", min_value=0, value=3)
    seconds = st.number_input("Duration Seconds", min_value=0, max_value=59, value=30)
    genre = st.text_input("Genre")
    track_no = st.number_input("Track Number", min_value=1, value=1)

    submitted = st.form_submit_button("Add Song")

    if submitted:
        new_song = classes.Song(
            title=title,
            artist=artist,
            album=album,
            duration=classes.Duration(minutes, seconds),
            genre=genre,
            track_no=int(track_no)
        )
        samples.songs.append(new_song)
        st.success(f"🎉 '{title}' by {artist} added to the song list!")