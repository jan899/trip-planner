# trip-planner

## Installation

Fork this repo and download it locally

Navigate there from the command line:

```sh
cd trip_planner
```


## Setup

Create a new environment called "trip-planner":

```sh
conda create -n trip-planner python=3.8
conda activate trip-planner
```

Install the required packages:

```sh
pip install -r requirements.txt
```

## Configure Environment Variables

Create a local .env file to this repo and put the following contents inside:

```
SENDGRID_API_KEY="_______________"
SENDER_ADDRESS="______________"

RAPID_API_KEY="______________"
RAPID_HOST="______________"
```

## Run

Run the program script locally:

```py
python trip_planner.py
```
Run the program script on a web application with Flask:

# Mac OS:

```sh
FLASK_APP=web_app flask run
```

# Windows OS:
... if `export` doesn't work for you, try `set` instead

```sh
export FLASK_APP=web_app
flask run
```

## [Deploying](/DEPLOYING.md)

Follow the deployment instructions to deploy the app to a remote server

## Testing

Run the below

```
pytest
```