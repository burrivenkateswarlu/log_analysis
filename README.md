# log_analysis
BY VENKATESWARLU BURRI
## Project Overview
This project is to improve the skills of the sql database.This project results in printing the data in database as per the queries we have written.It gives the results of:
- What are the most popular three articles of all time.
- Who are the most popular article authors of all time.
- Days on which more than 1% of requests lead to errors.
## Project files

This project consists for the following files are:

- LogAnalysis_Udacity.py - this is the file we run
- README.md - consists the steps and result
- newsdata.sql -  it is a database file
- views.sql - it consists of views of database
- output.png -image of the result
## Requirements for the project
1. Python
2. Vagrant
3. VirtualBox
## Dependencies
- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
## How to Install and Run the Project
Install Vagrant & VirtualBox
- Create Vagrant file `vagrant init ubuntu/xenial64`
- Connect to VirtualMachine `vagrant up`
- Login to VirtualMachine `vagrant ssh`
- Exit from current directory  `cd ..`
- Again exit directory `cd ..`
- Change directory path `cd vagrant`
- Update ubunut version using command `sudo apt-get update`
## We have to install postgresql
- Install postgresql using command `sudo apt-get install postgresql`
- Connect to postgres using command `psql su - postgres`
## We have to install modules
- Import psycopg2 module to connect database using command `pip install psycopg2`
- Create super user vagrant
- Create news database with owner vagrant using command `create database news;`
- Change ownership of database using command `alter database news owner to vagrant;`
- Exit the current running status using command `\q`
- Logout from the current user using command `logout`
-load the data in local database using the command:
  ```
    $ psql -d news -f newsdata.sql
  ```
- run `python LogAnalysis_udacity.py`
Then will get output as in OutPut.jpg
