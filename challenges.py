-- SELECTING DATA WITH SQL

-- Select a column from a table
-- Expected : 275 rows
select Name from Artist;

-- Select more than one column from a table
-- Expected : 59 rows
select FirstName, LastName from Customer;

/*
   Select all columns from a table
   The '*' is a wild card
   Expected 3503 rows
*/
select * from Track;


/*
   In all of the examples above, we retrieve data from every row in the table.
   We can filter the results using a WHERE clause.
   Expected : 44 rows
*/
Select * from Track
Where Composer = 'U2';


/*
   If you are a U2 fan, and look at the results of the query above,
   you'll see that the tracks that have AlbumId 232 are from the album Achtung Baby
   Let's confirm that by selecting that album from the Albums table
   Expected : 1 row
*/
Select * from Album
Where AlbumId = 232;


/*
   Notice that the Album table has an ArtistId (150 in this case for U2)
   The Track table did not have an ArtistId.
   So, to find the Artist for a Track we need to look in the Album Table
   Expected : 3503 rows
*/
Select * from Track
JOIN Album on Track.AlbumId = Album.AlbumId;

/*
   The Join pulls in the rows from the Track table,
   then for each row it adds the data from the Album table.
   So, after the query above you can now see the ArtistId for each Track
   But there is also a lot of other info that we don't need. Let's narrow things down

   This query will return
   The 'Name' from the Tracktable,
   The 'Title' from the Album table,
   And the 'ArtistId' from the Album table
*/
Select Name, Title, ArtistId from Track
JOIN Album on Track.AlbumId = Album.AlbumId;


/*
   There are two problems with the data from the previous query.
   'Name and Title' are confusing field names, it should be 'Track and Album'
   And secondly, We have the ArtistId, rather than the name of the Artist.

   Let's tackle the names of the columns using aliases
*/
Select Name as Track, Title as Album, ArtistId from Track
JOIN Album on Track.AlbumId = Album.AlbumId;


/*
   Now, let's get the name of the artist, rather than the ArtistId

   Procedure for Joining to an additional table.

   1. Find the table you want to join to,
*/
select * from Artist;


/*
   2. Find the column(s) you want to add to the query.
      In this case we want the Name Column from the Artist Table
*/

/*
   3. Find the columns you can join on.
      In this case, the new table has an ArtistId column, and so does our existing query
*/

/*
   4. Add the column we want to the select clause,
      and introduce a Join on the columns that can be joined.

      Expected: This query, is almost correct, but will throw an error
      [1] [SQLITE_ERROR] SQL error or missing database (ambiguous column name: Name)

      Try This: Run the query and see if you get the error to occur before moving on to the fix.
      Read the Error and try to come up with a theory about what might be wrong. Don't worry if your
      idea isn't correct.
*/

Select Name as Track, Title as Album, ArtistId, Name as Artist from Track
JOIN Album on Track.AlbumId = Album.AlbumId
JOIN Artist on Album.ArtistId = Artist.ArtistId;

/*
   The Track table has a column called Name, and so does the Artist Table.
   So, when we say 'Name as Track', or 'Name as Artist', there are two columns called Name
   The RDBMS can't choose which one to pick, even though it looks obvious to us,
   so we have to be unambiguous.

   We can prefix the two 'Name' fields with the table we mean to use.
   If you do this, you will find you get a similar error for ArtistId. It is also ambiguous,
   so we need to fix that too.

   It doesn't matter if you select the ArtistId from Album or Artist table. Both are the same.
   NOTE: Even though both are the same, the RDBMS won't make that leap of judgement. It puts the
   burden on you to be unambiguous. Get used to that.
*/

Select Track.Name as Track, Title as Album, Album.ArtistId, Artist.Name as Artist from Track
JOIN Album on Track.AlbumId = Album.AlbumId
JOIN Artist on Album.ArtistId = Artist.ArtistId;


/*
   5. If you don't need the Id column that you used in the join, you can get rid of it from the results.
      In this case we drop ArtistId from the select part of the query.
*/
Select Track.Name as Track, Title as Album, Artist.Name as Artist from Track
JOIN Album on Track.AlbumId = Album.AlbumId
JOIN Artist on Album.ArtistId = Artist.ArtistId;


/*
  Recap Joins:
    1. Find the table you want to join to.
    2. Find the column in that table that you want to add to your query results.
    3. Figure out the columns that you can join on.
    4. Add the column you need to your query [step 2], and create a join [step 3]
    5. Optionally remove the Id column from the query
 */


/* Combining Joins and Filters

   Earlier we filtered our results using a Where clause.
   We can still do that in exactly the same way even if our query is built up using joins.

   If you add a where clause to your previous query, you can filter the results down.
   For example, if you one want results for a particular artist
 */


Select Track.Name as Track, Title as Album, Artist.Name as Artist from Track
JOIN Album on Track.AlbumId = Album.AlbumId
JOIN Artist on Album.ArtistId = Artist.ArtistId
WHERE Artist = "U2";


-- Or a particular Artist and Track
Select Track.Name as Track, Title as Album, Artist.Name as Artist from Track
JOIN Album on Track.AlbumId = Album.AlbumId
JOIN Artist on Album.ArtistId = Artist.ArtistId
WHERE Artist = "U2" and Track = "Pride (In The Name Of Love)";


-- Or just a given Track name, regardless of artist or album
Select Track.Name as Track, Title as Album, Artist.Name as Artist from Track
JOIN Album on Track.AlbumId = Album.AlbumId
JOIN Artist on Album.ArtistId = Artist.ArtistId
WHERE Track = "Believe";


/* This is the power of SQL
   As you learn each new piece of the syntax you can combine them to make ever more powerful queries.
   This can also be one of SQL's challenges. The complexity of SQL queries can grow rapidly.
   It takes skill and experience to construct SQL Queries in such a way that they can be read easily.
   You'll see examples of more complex queries as you progress through the examples
 */


/*
    CHALLENGES
    ----------

    Complete the following exercises, the expected results are shown, you need to write the queries.
 */

/*
  BRONZE CHALLENGES
  -----------------

  1. Select the 'Name' column from the 'MediaType' table

  Expected:

  MPEG audio file
  Protected AAC audio file
  Protected MPEG-4 video file
  Purchased AAC audio file
  AAC audio file
*/


/*
  2. Select the 'FirstName', 'LastName' and 'Title' Columns from the 'Employee' Table,
     Filtering the results to only those with a Title of 'IT Staff'

     Expected:
     Robert	  King	    IT Staff
     Laura	  Callahan	IT Staff
 */


/*
  3. Join the 'Track' table and the 'MediaType' table to create a query
     that shows the Name of the Track, and the Name of the Media Type.
     Both tables have a 'MediaTypeId' column that you can join on.
     Both tables also have 'Name' columns, so you'll need to use aliases

     Expected: 3503 rows (Here's a sample, actual tracks may be different)
     For Those About To Rock (We Salute You)	    MPEG audio file
     Balls to the Wall	                          Protected AAC audio file
     Fast As a Shark	                            Protected AAC audio file

 */


/*
  SILVER CHALLENGES
  -----------------

  4. Similar Query to above, but join the track table to the Genre table,
     show the names of the tracks and genres in the results.
     Figure out the columns you can join on, any aliases that you need.
     Filter the results to only show 'Jazz' tracks

     Expected: 130 rows (Here's a sample, actual tracks may be different)
     Desafinado	                              Jazz
     Garota De Ipanema	                      Jazz
     Samba De Uma Nota Só (One Note Samba)	  Jazz
*/

/*
  5. Create a Query that shows:
      The name of a track, the name of it's MediaType, and the name of it's genre.
      You'll need to join 3 tables together with the appropriate join columns.
      Add a filter to only show tracks with a MediaType of "Protected AAC audio file"
      and a Genre of "Soundtrack"

      If you create the query properly, there should be only one matching track.

      Expected: 1 row
      Koyaanisqatsi	    Protected AAC audio file	    Soundtrack
*/



/*
  GOLD CHALLENGES
  -----------------
  6. Create a query that shows
        PlayList Name
        Track Name
        Album Title
        Artist Name

        Filter to only show results for the 'Grunge' playlist

    Expected: 15 rows (example)
    Grunge	  Hunger Strike	      Temple of the Dog	      Temple of the Dog
    Grunge	  Man In The Box	    Facelift	              Alice In Chains
    Grunge	  Evenflow	          Ten	                    Pearl Jam
 */


/*
  GOLD CHALLENGES
  -----------------
  7. Find a playlist that contains only 1 track.

    Expected: I'm not going to tell you, that'd be too easy.
*/

/*
  8. Draw an ER diagram of the Chinook Database
     Show all 11 tables and the relationships between them.
*/


/*
  EXPERIMENT
  -----------------
  9. Play with the data, create your own queries and joins until you are comfortable with what you've learned.

 10. There are there questions you can't easily answer right now with what you've learned.

        Which genre has the most tracks?
        Which Artist has sold the most tracks?
        Which Artist has recorded in the most genres?

     Try to come up with some more questions that you can't answer,
     then return to those questions after the next lesson.
 */