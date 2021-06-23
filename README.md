# trip-planner

## Installation

Fork this repo and download it locally

Navigate there from the command line:

'''sh
cd trip_planner
'''


## Setup

Create a new environment called "trip-planner":

'''sh
conda create -n trip-planner python=3.8
conda activate trip-planner
'''

Install the required packages:

'''sh
pip install -r requirements.txt
'''

## Configure Environment Variables

Create a local .env file to this repo and put the following contents inside:

'''
SENDGRID_API_KEY="Private Sendgrid API Key"
SENDER_ADDRESS="Sender's email address"
'''

## Run

Run the program script:

'''py
python trip_planner.py