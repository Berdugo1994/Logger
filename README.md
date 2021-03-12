ReadMe File:

The Logger includes only Backend.

To Test the logger use client-side such as : POSTMAN.

Adress: http://localhost:5000

The Logger writes to a local MySql Database.

The Database is saved even when the app is restarted or turnrd off.

There are 3 functions:

on localhost:5000 -> the logger writes to the DB the user : ip, REST - request type, data(content of message) , time in GMT 00:00)

on route /showall A.K.A :  localhost:5000/showall -> the logger return json file with all the data saved in the DB.(every entrie).

on route /cleardb A.K.A : localhost:5000/cleardb -> the logger clears all the log Table.


every interaction with the adress is printed.

every write to the logger is printed.

to see the prints run -> docker logs from_git_app_1 


To run the dockfile:

download the (.tar) file from the repository: https://drive.google.com/drive/folders/1__TtAppz1wCAAtfa2bGfBkm7ZnUxsXQ5?usp=sharing

cd to the file location

load the image with -> docker load --input , -i full.tar

run the script : docker build from_git_app -> will create also the mysql image.

run the script : docker image ls -> to make sure the repository loaded

run the script : docker-compose up -d -> to create the compose container 

OPEN POSTMAN AND ENJOY!


**In case you had problems , you can:**

1.download this repository

2.cd to the folder.

3.docker-compose up

4.and you are good to go.


(you should see 2 new images).
