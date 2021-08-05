# Zendesk: Fall 2021 Co-Op Coding Challenge
## Introduction

Howdy!

This repository is my submission for Zendesk's Fall 2021 Co-Op Coding Challenge, as part of their internship application. It is an application utilized as a browser-based ticket viewer to read on a Zendesk account's list of tickets.

##  Technologies
For this project, the following technologies were used:

- **Python 3.6.7** and **pip3**
- **Flask** for the web framework
- **Bootstrap 5** for styling the ticket viewer
- **requests** to authenticate and send requests to the Zendesk API
- **.env** for environmental variables

## Requirements
The application was built with Python v3.6.7 on an AWS EC2 server running Ubuntu 18.04, but any sufficient machine with Python3.6 should suffice. 

One should have an account and a subdomain registered under Zendesk. For this specific challenge, it was accomplished by obtaining a [free trial](https://www.zendesk.com/register.). Additionally, the Zendesk account should populate a set of tickets from a dataset that could be obtained [here](https://gist.github.com/svizzari/c7ffed8e10d3a456b40ac9d18f34289c) using cURL or Postman. The user should also obtain a token from Zendesk for use of this application. Under Settings >> Channels >> API, one can add an API token to utilize for authentication purposes. Copy the token and store it in a safe place! 

Once these preliminary requirements are met, a `.env` file is required in the root directory of this service. They include variables relating to the server such as `SERVER_HOST`, which pertains to the host of the web server, and `SERVER_PORT`, which specifies what port the server would run on. Some Zendesk account-related items are needed as well, with `ZENDESK_EMAIL`, `ZENDESK_TOKEN`, `ZENDESK_DOMAIN` being one of the required sets of environmental variables.

Now, it's time to setup the enviroment! To create a new Python virtual environment, running `python3 -m venv` should suffice in making a virutal enviromemnt under the folder `venv`. Activate this virtual environment by running `source venv/bin/activate`, and run `pip3 install -r requirements.txt` to install some packages required to run this project.

That's it for setting things up! You can then run `python3 app.py` to start the web server and visit the website to go through the ticket viewer!

You can also run unit tests with `python3 test.py`.
