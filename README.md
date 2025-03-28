# Deploying a Pretrained Sentiment Analysis Model with FastAPI

This tutorial demonstrates how to deploy a pretrained Hugging Face sentiment analysis model using FastAPI. It is intended for developers, machine learning (ML) engineers, and data scientists seeking to expose ML models through a RESTful API using Python-based tools.

This guide follows best practices in documentation as outlined in the [Google Developer Style Guide](https://developers.google.com/style), prioritizing clarity, precision, and reader-first communication.

---

## Objectives

By the end of this guide, you will learn how to:

- Load a pretrained model using Hugging Face Transformers.
- Serve model predictions through an HTTP endpoint using FastAPI.
- Test the endpoint using `curl`, Postman, or Swagger UI.
- Understand the structure of a production-friendly ML API deployment.

---

## Project structure

```c#
fastapi-ml-api/ 
├── app.py # Core application file with model and endpoint 
├── requirements.txt # Python package dependencies 
├── README.md # Project documentation (this file) 
├── LICENSE # MIT License for project use 
└── .github/ 
    └── ISSUE_TEMPLATE/ 
    └── bug_report.md # Template for structured bug reporting
```

---

## Prerequisites

- Python 3.8 or later
- Familiarity with Python, REST APIs, and the command line
- A virtual environment (recommended)

---

## Setup instructions

 ```bash
git clone https://github.com/MeelahMe/fastapi-ml-api.git
cd fastapi-ml-api
```
## Create and activate a virtual environment (recommended)

```bash
python -m venv venv
```
Activate the environment:
- On macOS/Linux

```bash
source venv/bin/activate 
```
- On Windows:

```bash
venv\\Scripts\\activate
```
You should now see your terminal prompt prefixed with (venv).

## Install required packages

```bash
pip install -r requirements.txt
```
This will install:

- FastAPI for creating the web application.
- Uvicorn as the ASGI server.
- Transformers for accessing pretrained models.
- Torch as the backend deep learning framework.

## Verify files are present 

- app.py
- requirements.txt
- README.md
- .github/ISSUE_TEMPLATE/bug_report.md
- LINCENSE

## Run the application server

```bash
uvicorn app:app --reload
```
The --reload flag enables automatic server restart on code changes.

Expected output:

```bash
INFO:     Uvicorn running on http://127.0.0.1:8000
```
## Open the API docs

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Usage instructions

Once your application server is running, you can interact with the API using the Swagger UI, command-line tools like curl, or API clients such as Postman.

## Usage Swagger UI (recommended for exploration)

1. Open your browser and navigate to:

```bash
http://127.0.0.1:8000/docs
```

2. Locate the `POST /predict` endpoint in the list.
3. Click **Try it out**.
4. In the request body input, enter sample text:

```json
{
  "text": "This is a fantastic project!"
}
```
5. Click **Execute**.
6. The response section below will display the prediction result.

This is ideal for quickly verifying functionality and exploring the API.

## Using `curl` (Command Line)

To send a request directly from the terminal:

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Deploying models is easier than ever."}'
```
Expected output: 
```json
{
  "result": [
    {
      "label": "POSITIVE",
      "score": 0.9997
    }
  ]
}
```


