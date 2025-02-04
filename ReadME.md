# LSEG Chatbot
## This `README.md` file provides instructions for three different options to run the LSEG Chatbot application using Docker or directly with Python.

### Option 1 

You can use the docker image which has been built and uploaded to my dockerhub.
Commands to run: 

1. docker pull shubhamk137/lseg-chatbot:latest
2. docker run -p 5000:5000 shubhamk137/lseg-chatbot:latest

This will start the application on localhost at port 5000, accessible at http://127.0.0.1:5000

### Option 2

You can clone the repository and use the dockerfile to build the docker image and run the application.
Commands to run:

1. git clone https://github.com/kumasbz/lseg-chatbot.git for HTTPS **or** git clone git@github.com:kumasbz/lseg-chatbot.git for SSH
2. cd lseg-chatbot
3. docker build -t lseg-chatbot .
4. docker run -p 5000:5000 lseg-chatbot

This will start the application on localhost at port 5000, accessible at http://127.0.0.1:5000

### Option 3

You can clone the repository and run the flask applciation using python commands.
Commands to run:

1. git clone https://github.com/kumasbz/lseg-chatbot.git for HTTPS **or** git clone git@github.com:kumasbz/lseg-chatbot.git for SSH
2. cd lseg-chatbot
3. pip install -r requirements.txt
4. python app.py

This will start the application on localhost at port 5000, accessible at http://127.0.0.1:5000