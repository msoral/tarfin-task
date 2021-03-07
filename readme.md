# Tarfin Interview Task

## Setup:

#### 1. Manually

 Clone the repo and install dependencies with:

    pip install -r requirements.txt
    
 Before running the app for the first time run the following in order.
 
    python model/preprocess.py
    python model/train.py
    python model/predict.py 
    python init.py
    
 Start the app by executing:

    python app.py
    
 The API listens on port 5000 of local host. To get a prediction send a request to:  
  `http://localhost:5000/api/v1/predict/{my_id}`
    

## API

The API runs at localhost://5000

#### Get prediction by ID
**Definition**

`GET /prediction/<id>`

**Response**

    {
    "id": 1,
    "prediction": 0.7661
    }
