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
 
 
 
 -- ORDERING DATA WITH SQL

-- Select all columns from the Album table
-- Sort the results by title
select * from Album
order by Title;


-- Select all columns from the Album table
-- Sort the results by title descending
select * from Album
order by Title desc;


-- Select all columns from the Album table
-- Sort by ArtistId, and within that by Title
select * from Album
order by ArtistId, Title;


-- Select all columns from the Album table
-- Sort by ArtistId Ascending, and within that by Title Descending
select * from Album
order by ArtistId, Title Desc;


-- Join the Track and Album tables to show track names and album titles.
-- Sort by Album title, then by Track Name
select Track.Name, Album.Title from Track
join Album on Track.AlbumId = Album.AlbumId
order by Album.Title, Track.Name;


/*
  Select the Invoice Date, BillingCite and Total from the Invoice table
  Sort by Total, descending. And limit to the top 5 results

  Expected :
    2013-11-13 00:00:00	  Prague	      25.86
    2012-08-05 00:00:00	  Fort Worth	  23.86
    2010-02-18 00:00:00	  Budapest	    21.86
    2011-04-28 00:00:00	  Dublin	      21.86
    2010-01-18 00:00:00	  Vienne	      18.86
*/

select InvoiceDate, BillingCity, Total from Invoice
order by Total desc
limit 5;



/*
    CHALLENGES
    ----------

    Complete the following exercises, the expected results are shown, you need to write the queries.
*/

/*
  BRONZE CHALLENGES
  -----------------

  1. Select the InvoiceDate, BillingAddress, and Total from the Invoices table,
     Ordered by InvoiceDate Descending

     Expected : 412 rows (starting with the following)
     2013-12-22 00:00:00	  12,Community Centre	                        1.99
     2013-12-14 00:00:00	  Porthaninkatu 9	                            13.86
     2013-12-09 00:00:00	  Rua dos Campeões Europeus de Viena, 4350	  8.91
*/


/*
  2. We need to fire the last three people hired.
     Select the EmployeeId, LastName, FirstName and HireDate
     of the 3 Employees with the most recent HireDate

     Expected : 3 rows (starting with the following)
      8	  Laura	  Callahan	  2004-03-04 00:00:00
      7	  Robert	King	      2004-01-02 00:00:00
      5	  Steve	  Johnson	    2003-10-17 00:00:00
*/

/*
  SILVER CHALLENGES
  -----------------

  3. Disaster, we've heard from Steve Johnson's lawyers.
     He claims that Michael Mitchell was hired on the same day as him,
     but was hired later in the day. Mitchell should have been let go, not him.

     Confirm this by extending the number of results and make sure nobody else was
     hired on that day.

     Then modify the query to return the correct 3 people.

     Continue to use HireDate as the primary sort column, but use EmployeeId as the tie breaker.
     Assume that a higher EmployeeId means they were hired later.

     Expected : 3 rows (starting with the following)
      8	  Laura	  Callahan	  2004-03-04 00:00:00
      7	  Robert	King	      2004-01-02 00:00:00
      6	  Michael	Mitchell	  2003-10-17 00:00:00
*/



/*
  GOLD CHALLENGES
  -----------------

  4. Create a query that shows our 10 biggest invoices by Total value, in descending order.
     If two invoices have the same Total, the more recent should appear first.
     The query should also show the Name of the Customer

     An Easy way to show the name would be to include the FirstName and LastName columns from
     the Customer table. However, if you use the concatenation operator you can combine those
     fields into one column in the results.

     Expected: 10 rows

      Helena Holý	            2013-11-13 00:00:00	  25.86
      Richard Cunningham	    2012-08-05 00:00:00	  23.86
      Hugh O'Reilly	          2011-04-28 00:00:00	  21.86
      Ladislav Kovács	        2010-02-18 00:00:00	  21.86
      Victor Stevens	        2011-05-29 00:00:00	  18.86
      Astrid Gruber	          2010-01-18 00:00:00	  18.86
      Luis Rojas	            2010-01-13 00:00:00	  17.91
      Isabelle Mercier	      2012-10-06 00:00:00	  16.86
      František Wichterlová	  2012-09-05 00:00:00	  16.86
      Bjørn Hansen	          2011-06-29 00:00:00	  15.86
*/




-- AGGREGATING DATA WITH SQL

-- Aggregate functions allow us to calculate some value from data.
/*
    Count how many rows are in the Customer Table
    Expected : 59
 */
select count(*) from Customer;
/*
    What Happens if we replace the wildcard '*' with a column?
    The answer is still 59. The count() function counts how many 'rows' are in the query results.
    The '*' or column name(s) only affects how many columns there are.
    Expected : 59
 */
select count(FirstName) from Customer;
/*
    What can you do to change the number of 'rows' in the results, so that count returns a different value?
    How about filtering, with a Where clause?
    If we count the number of customers called Frank, we find there are only 2
    Expected : 2
 */
select count(*) from Customer
where FirstName = "Frank";
/*
    The count function is concerned only with the number of rows in a query result. It says nothing about the
    actual data values. But there are other aggregate functions. Like the following:
 */
-- Expected : Almeida
select min(LastName) from Customer;
-- Expected : Zimmermann
select max(LastName) from Customer;
-- Expected : 5.651941747572825
select avg(Total) from Invoice;
-- Expected : 5.65
select round(avg(Total),2) from Invoice;
/*
  Aggregate Functions can sometimes allow us to verify the same information from two sources.
  Here is the Total value for Invoice 2
  Expected : 3.96
*/
select total from Invoice where InvoiceId = 2;
/*
  Here's what we get by taking the line items from that invoice, multiplying the Price by Quantity,
  to get the total for each line item. Then using the sum function to get the total for the the invoice.
  Expected : 3.96
*/
select sum(UnitPrice * Quantity) from InvoiceLine
where InvoiceId = 2;
/*
    BRONZE CHALLENGES
    -----------------
 */
-- On what date was our most recent employee hired?
-- Expected : 2002-04-01 00:00:00
-- What is the date of mirth of our youngest employee?
-- Expected : 1973-08-29 00:00:00
-- How Many Customers is Employee 4 the Sales Support Agent For?
-- Expected : 20
/*
    SILVER CHALLENGES
    -----------------
    How Many Customers is Jane Peacock the Sales Support Agent For?
    You'll need to join the Employee and Customer Tables for this one.
    Expected : 21
*/
/*
    GOLD CHALLENGES
    -----------------
    Which Media Type is most popular?
    How could you answer this with a single query?
    You probably can't based on what you know so far. We'll get there.
    For now, you can use a separate query for each media type so see how many tracks use it.
    Expected : MPEG audio file
*/


-- GROUPING DATA WITH SQL
/*
    When we looked at aggregate functions, we applied them to entire query results.
    We could get the maximum value in a particular field across all rows, or some subset
    of the rows, if we use a where clause.
    Often what we really want to do us group our data into a number of subsets, and use the aggregate
    functions on each of those. For example, counting how many tracks use each of the 5 different Media Types.
    SQL Provides a GROUP BY feature that allows us to do this.
*/
/*
  Group By The AlbumId in the Track Table
  Show the number of rows in each group
  The results aren't very useful. We can see how many tracks are on each album,
  but not which album each result is for.
*/
select count(*) from Track
group by AlbumId;
/*
  Group By The AlbumId in the Track Table
  Show the number of rows in each group, and the AlbumId for each.
  Better, now we can see which album each row relates to. But it's still only an Id
*/
select AlbumId, count(*) from Track
group by AlbumId;
/*
  Group By The AlbumId in the Track Table
  Show the number of rows in each group, and the Album Title for each.
  Now we can see the title of the album each row relates to.
*/
select Album.Title, count(*) from Track
  join Album on Track.AlbumId = Album.AlbumId
group by Track.AlbumId;
/*
    The key to the group by is that the repeating value in the grouped column (AlbumId) defines a group
    of rows, that gets collapsed into one row. You can then use an Aggregate Function on that group, just as
    you previously did on entire query results.
    All of the aggregate functions work just as before.
*/
-- Find the Cheapest Track On Each Album
select AlbumId, Min(UnitPrice) from Track
group by AlbumId;
-- Find the Most Expensive Track On Each Album
select AlbumId, Max(UnitPrice) from Track
group by AlbumId;
-- Find the total cost of each album
select AlbumId, Round(Sum(UnitPrice), 2) from Track
group by AlbumId;
-- Find the total cost of each album
-- But join to the Album table to include the Title of the Album
select Album.Title, Round(Sum(UnitPrice), 2) from Track
  Inner Join Album on Track.AlbumId = Album.AlbumId
group by Track.AlbumId;
/*
    BRONZE CHALLENGES
    -----------------
 */
-- How many customers do we have in the City of Berlin
-- Expected : 2
/*
    SILVER CHALLENGES
    -----------------
    How much has been made in sales for the track "The Woman King"
    You'll need to find how many sales there are for each track in the InvoiceLine table,
    multiply by the Unit Price,
    join to the Track table to bring in the Track Name,
    and filter to find the deatils for "The Woman King"
    Expected : 3.98
*/
/*
    GOLD CHALLENGES
    -----------------
    Create a list of the top 5 acts by number of tracks.
    The table should include the name of the artist and the number of tracks they have.
    You will need to link from the Track
    Iron Maiden     213
    U2              135
    Led Zeppelin      114
    Metallica         112
    Deep Purple     92
 */