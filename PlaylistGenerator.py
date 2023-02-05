import tkinter as tk
import pandas as pd
from Levenshtein import distance

class PlaylistGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Playlist Generator")
        
        self.artist_label = tk.Label(self, text="Artist:")
        self.artist_input = tk.Entry(self)
        
        self.generate_button = tk.Button(self, text="Generate Playlist", command=self.generate_playlist)

        self.artist_label.pack()
        self.artist_input.pack()
        self.generate_button.pack()

        self.df = pd.read_csv("kpop_music_videos.csv")

        self.playlist_box = tk.Listbox(self, font=("Helvetica", 12), bg='#ADD8E6', fg='white')
        self.playlist_box.pack()

        
    def generate_playlist(self):
        # Retrieve the user's input
        artist = self.artist_input.get()
        
        # Create an empty list to store the distances
        distances = []
        
        # Iterate through the dataset
        for index, row in self.df.iterrows():
            # Calculate the Levenshtein distance
            dist = distance(artist, row['Artist'])
            # Append the distance and the index to the list
            distances.append((dist, index))
        
        # Sort the list by distance
        distances.sort()
        
        # Get the indices of the closest songs
        closest_indices = [i for d, i in distances[:10]]
        
                # Get the song names of the closest songs
        playlist = self.df.iloc[closest_indices]['Song Name']

        # Clear the Listbox
        self.playlist_box.delete(0, tk.END)

        # Insert the songs into the Listbox
        for song_name in playlist:
            self.playlist_box.insert(tk.END, song_name)

if __name__ == '__main__':
    app = PlaylistGenerator()
    app.mainloop()

