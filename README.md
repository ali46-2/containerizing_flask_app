A simple Python app that uses the Flask web framework as an endpoint to get inference from a machine learning model. The machine learning model takes years of experience as input, and returns the predicted salary.

## Installation
### Docker
  If you have Docker installed then you can use the following commands inside the root folder of this project.
  - Create image from Dockerfile
  ```
  docker build -t flask_model_inference .
  ``` 
  - Create container from image and run the container
    - `PORT` is the port number that you want to run the app on
  ```
  docker run --name flask_model_inference_container -p PORT:5000 flask_model_inference
  ```
  - The app is now running on `localhost:PORT`. The model inference endpoint is at `localhost:PORT/api`. You can send a GET request with the input passed into the url to get the result as JSON.
  - Example usage for `PORT` 8000
  ```
  localhost:8000/api/5
  ```
### Local
  If you prefer to run the app locally, then you can use the following commands inside the root folder of this project. These instructions are assuming you are using Windows.
  - Create virtual environment
  ```
  python -m venv venv
  ```
  - Activate virtual environment
  ```
  .\venv\Scripts\activate
  ```
  - Install required packages
  ```
  pip install -r requirements.txt
  ```
  - Run the app
  ```
  python .\scripts\server.py
  ```
  - The app is now running on `localhost:5000`. The model inference endpoint is at `localhost:5000/api`. You can send a GET request with the input passed into the url to get the result as JSON.
  - Example usage
  ```
  localhost:5000/api/5
  ```
