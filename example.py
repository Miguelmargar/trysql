Track Name, Genre Name, MediaType Name, Album Title, Artist Name

1. Get Name from track (Name)
    select Name as Track from Track;
    
2. Get the column from track that I'll join to Genre on
    select Name as Track, GenreId from Track;
    
3. Join to Genre and select the Name
    select Track.Name as Track, Genre.Name as Genre
    from Track join Genre 
    on Track.GenreId = Genre.GenreId;
  
4. Get the column that we will join *from* to the MediaType Table
    select Track.Name as Track, Genre.Name as Genre, MediaTypeId 
    from Track join Genre
    on Track.GenreId = Genre.GenreId;
    
5. Get the MediaType Name
    select Track.Name as Track, Genre.Name as Genre, MediaType.Name as MediaType 
    from Track 
    join Genre on Track.GenreId = Genre.GenreId
    join MediaType on Track.MediaTypeId = MediaType.MediaTypeId
    
6. Get the column that we will join *from* to the Album Table
    select Track.Name as Track, Genre.Name as Genre, MediaType.Name as MediaType, Track.AlbumId 
    from Track 
    join Genre on Track.GenreId = Genre.GenreId
    join MediaType on Track.MediaTypeId = MediaType.MediaTypeId
    
7. Get the Title of the Album
    select Track.Name as Track, Genre.Name as Genre, MediaType.Name as MediaType, Album.Title as Album 
    from Track 
    join Genre on Track.GenreId = Genre.GenreId
    join MediaType on Track.MediaTypeId = MediaType.MediaTypeId
    join Album on Track.AlbumId = Album.AlbumId
    
8. Get the column that we join *from* to the Artist Table
    select Track.Name as Track, Genre.Name as Genre, MediaType.Name as MediaType, Album.Title as Album, Album.ArtistId 
    from Track 
    join Genre on Track.GenreId = Genre.GenreId
    join MediaType on Track.MediaTypeId = MediaType.MediaTypeId
    join Album on Track.AlbumId = Album.AlbumId
    
9. Get the Name of the Artist
    select Track.Name as Track, Genre.Name as Genre, MediaType.Name as MediaType, Album.Title as Album, Artist.Name as Artist 
    from Track 
    join Genre on Track.GenreId = Genre.GenreId
    join MediaType on Track.MediaTypeId = MediaType.MediaTypeId
    join Album on Track.AlbumId = Album.AlbumId
    join Artist on Album.ArtistId = Artist.ArtistId 