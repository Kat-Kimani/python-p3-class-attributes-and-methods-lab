# class Song:
#     genres=[]
#     artists=[]
#     song_count=0
#     genre_count={}
#     artist_count={}

#     def __init__(self, name, artist, genre):
       
#         self.name = name
#         self.artist = artist
#         self.genre = genre
#         self.add_song_to_count()
#         self.add_to_genres()
#         self.add_to_artists()
#         self.add_to_genre_count()
#         self.add_to_artist_count()
        
#     @classmethod
#     def add_song_to_count(cls, increment=1):
#         cls.song_count += increment


#     @classmethod
#     def add_to_genres(cls):
#         if cls.genre not in cls.genres:
#             cls.genres.append(cls.genre)

#     @classmethod
#     def add_to_artists(cls):
#         if cls.artist not in cls.artists:
#              cls.artists.append(cls.artist)     

#     @classmethod
#     def add_to_genre_count(cls):
#         if cls.genre in cls.genre_count:
#             cls.genre_count[cls.genre]+=1
#         else:
#             cls.genre_count[cls.genre]=1   

#     @classmethod
#     def add_to_artist_count(cls):
#         if cls.artist in cls.artist_count:
#             cls.artist_count[cls.artist]+=1
#         else:
#             cls.artist_count[cls.artist] 



# song1 =  Song("99 Problems", "Jay Z", "Rap")
# song2 =    Song("Halo", "Beyonce", "Pop")
# song3 =    Song("Smells Like Teen Spirit", "Nirvana", "Rock")

# print(Song.genre_count)

class Song:
    count = 0
    genres = []
    artists = []
    genre_count = dict()
    artist_count = dict()

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
        self.add_song_to_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1


    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1