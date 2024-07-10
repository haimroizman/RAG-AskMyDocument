from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv, find_dotenv
from app.service import AskMyDocService
import asyncio

load_dotenv(find_dotenv(), override=True)

app = FastAPI()

doc_path = "data"
openai_api_key = os.getenv("OPENAI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")

document_service = AskMyDocService(doc_path, openai_api_key, pinecone_api_key, use_pinecone=True)


class QueryRequest(BaseModel):
    query: str


@app.post("/query")
async def ask_question(request: QueryRequest):
    try:
        # Using asyncio.to_thread to run the blocking query method in a separate thread
        answer = await asyncio.to_thread(document_service.query, request.query)
        if not answer:
            raise HTTPException(status_code=404, detail="Answer not found")
        return {"query": request.query, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
