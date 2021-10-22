


This project used Pthyon and SQLAlchemy to examine climate data and explore the climate Database in Hawaii. 
I used a SQLite database to extract data on weather measurements at weather stations in Hawaii. The data was first explored to find any interesting insights, using SQLAlchemy to query the database.

 I retrieved the last 12 months of precipitation data by querying the 12 preceding months of data. 

* Selected only the `date` and `prcp` values.

* Loaded the query results into a Pandas DataFrame and set the index to the date column.

* Sorted the DataFrame values by `date`.

* Plotted the results using the DataFrame `plot` method.


<img width="352" alt="climate_change_1" src="https://user-images.githubusercontent.com/46588030/137401655-8a826e27-0791-41e7-a16d-0fb26325b101.png">


<img width="368" alt="climate_change_2" src="https://user-images.githubusercontent.com/46588030/137401697-797d7a19-3d70-4342-a229-7b89eeb2a24d.png">


