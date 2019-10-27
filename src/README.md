Prerequisites
Python3 and Pip3.7 (or pip3)

Installing
First, create a virtual environment

python3 -m virtualenv env
After creating the virtual environment, start the environment using the following command.

source env/bin/activate
Now, install all the dependencies as specified in requirements.txt

make init
Be sure to set the environment variable for flask

export FLASK_APP=app.py
Running the server
To start the server, run the following command

flask run