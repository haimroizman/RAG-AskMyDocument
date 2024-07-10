# AskMyDocService

AskMyDocService is a FastAPI-based service that answers questions based on the content of a provided document. It uses
OpenAI's language model and Pinecone for vector storage.

## Project Structure

AskMyDocService/
│
├── app/
│ ├── init.py
│ ├── api.py
│ └── service.py
│
├── data/
│ └── python_exercise.docx
│
├── .env
├── Dockerfile
├── docker-compose.yml
├── main.py
└── requirements.txt

## Requirements

- Docker
- Docker Compose

## Environment Variables

Create a `.env` file in the root directory and add your OpenAI and Pinecone API keys:
_******* I've already added my OpenAI and Pinecone API keys in the .env file, If you want to change fill comfortable to
change it.**********_
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key

_******* I've already added my OpenAI and Pinecone API keys in the .env file, If you want to change fill comfortable to
change it.**********_

## Setup

1. **Build the Docker image:**

    ```sh
    docker-compose build
    ```

2. **Run the container:**

    ```sh
    docker-compose up -d
    ```

3. **Stop the container:**

    ```sh
    docker-compose down
    ```
4. **Check the logs:**

    ```sh
    docker-compose logs
    ```

## Usage

Once the container is running, you can interact with the service via HTTP requests.

### Example using `curl`

```sh
curl -X POST "http://127.0.0.1:8000/query" -H "Content-Type: application/json" -d '{"query": "What is the exercise about?"}'
```

## Run Locally

1. **install dependencies**

```sh
pip install -r requirements.txt
```

2. **run the application**

```sh
uvicorn app.api:app --host 0.0.0.0 --port 8000 --reload
```
