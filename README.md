### My recording of learning Flask framework

*Absorbing ideologies from varies of design concept  must be really fun and educated.*

PS: I am currently migrating to python web framework from php Laravel.

0.create a database;
```shell script
CREATE DATABASE your_database CHARACTER SET UTF8MB4;
```
#set up this project
1.create an virtual environment
```shell script
cd this_project
python3 -m venv venv
```
2.activate the virtual environment
```shell script
. venv/bin/activate
```
3. install necessary libraries
```shell script
pip3 install -r requirements.txt
```
4.start running
```shell script
export FLASK_APP=index.py
flask run
```