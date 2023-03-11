# LibraryManagementSystem
This is a Library Management System project that I'm working on using PostgreSQL and Python. The goal is to create an application that can efficiently manage a group of libraries. So far, I've created an admin page with the ability to search for books and add new books. Currently, I'm working on implementing the update and remove book options, which will make the system even more robust and user-friendly.
## Setting up the project
1. Start the PostgreSQL application, open terminal and connect to PostgreSQL using below command.  
   ````
   psql
1. Create a new database called **library** by running the following command:
   ```` 
    CREATE DATABASE library;
2. Connect to the newly created **library** database by typing
   ````
   \c library
3. Import the database schema by running the following command:
   ````
   \i <cloned path of repo>/LibraryManagementSystem/SQL\ queries/library_schema.sql
4. Import the database roles by running the following command:
   ````
   \i <cloned path of repo>/LibraryManagementSystem/SQL\ queries/library_roles.sql
5. Import the library data by running the following command:
   ````
   \i <cloned path of repo>/LibraryManagementSystem/SQL\ queries/library_data.sql
6. Install the necessary Python packages by running the following command:
   ````
   pip install -r <cloned path of repo>/Python\ file/requirments.txt
7. Finally, run the **librarian.py** file to start the application:
   ````
   python librarian.py