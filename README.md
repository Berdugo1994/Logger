ReadMe File:

Logger API : writes every visit to a local MySql DB.

Using python - flask library, and Docker Compose tool for multi-container Docker applications

To Test the logger use client such as : POSTMAN.

Adress: http://localhost:5000

The Logger writes to a local MySql Database.

The Database is saved even when the app is restarted or turned off.

There are 3 functions:

on localhost:5000 -> the logger writes to the DB the user : ip, REST - request type, data(content of message) , time in GMT 00:00)

on route /showall :  localhost:5000/showall -> the logger return json file with all the data saved in the DB.(every entrie).

on route /cleardb  : localhost:5000/cleardb -> the logger clears / initiaite all the log Table. **to initialize the db do this first. only at the first time**


every interaction with the adress is printed.

every write to the logger is printed.

to see the prints run -> docker logs from_git_app_1 


To run the dockfile:

1.clone this repository

2.cd to the folder.

3.run : docker-compose up

4.and you are good to go.


(you should see 2 new images).
