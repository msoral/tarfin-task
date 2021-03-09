# Tarfin Interview Task

## Setup:

 Clone the repo and install dependencies with:

    pip install -r requirements.txt
    
 Before running the app for the first time run the following in order.

    python init.py
    
 Start the app by executing:

    python wsgi.py
    

## API

The API runs at localhost://5000

#### Get prediction by ID
**Definition**

`GET /api/v1/prediction`

**Input**

`{"id": "1"}`

**Response**

    {
    "id": 1,
    "prediction": 0.7661
    }
