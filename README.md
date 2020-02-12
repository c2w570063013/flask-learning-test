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
4.create config.py in this project's root dir and website's dir

5.create tables
```shell script
python3 create_tables.py
```

6.start running on development mode
```shell script
export FLASK_APP=index.py
# if you run this project on server on debug mode, you should add:--host=0.0.0.0 at the end. i.e.
# flask run --host=0.0.0.0 
flask run   #this is for local environement
```

## running in production with Nginx and gunicorn....
>the following operations was derived from Corey Schafer's youtube video
1.create a nginx config file 
```shell script
server {  
        listen 80;
        server_name flask.crosseverycorner.xyz; # change to your domain

        location /static {
            alias /home/wayne/python/flask-learning-test/website/static;
        }
        location / {
            proxy_pass http://localhost:8000;
            include /etc/nginx/proxy_params;
            proxy_redirect off;
        }
}
```
2.allow http tcp traffic(it's not necessary for most servers)
```shell script
sudo ufw allow http/tcp
sudo ufw delete allow 5000 # delte 5000 port allow
sudo ufw enable
``` 
3.restart nginx
```shell script
sudo nginx -t
sudo nginx -s reload
```
4.check out how many cpu cores on your server
```shell script
nproc --all
#the worder numbers depends on the number of core. 
```
5.run gunicorn
```shell script
gunicorn -w 3 index:app #index means the index.py and app means the app in this file
```
6.install supervisor
```shell script
sudo apt install supervisor
```
7.add precess to supervisor
```shell script
sudo vim /etc/supervisor/conf.d/flask_test.conf

[program:flask_test]
directory=/home/wayne/python/flask-learning-test
command=/home/wayne/python/flask-learning-test/venv/bin/gunicorn -w 3 index:app
user=wayne
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/var/log/flask_test/flask_test.err.log
stdout_logfile=/var/log/flask_test/flask_test.out.log
```
8.create log dir and touch corresponding files
```shell script
sudo mkdir -p /var/log/flask_test/
sudo touch /var/log/flask_test/flask_test.err.log
sudo touch /var/log/flask_test/flask_test.out.log
```
9.restart supervisor
```shell script
sudo supervisorctl reload
```