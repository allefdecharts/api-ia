from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from .db import vectorstore
from .chat import get_ai_response

app = FastAPI()

class RequestBody(BaseModel):
    prompt: str
    context: str
    history: str

@app.get("/")
def read_root(): 
    
    return {"message": "Welcome to API!"}

@app.post("/generate-response/")
def generate_response(request_body: RequestBody):
    try:
        prompt = request_body.prompt
        context = request_body.context
        history = request_body.history
        docs = vectorstore.similarity_search(prompt, search_kwargs={"k": 2})
        context = " ".join(f"contexto {i+1}: {doc.page_content}." for i, doc in enumerate(docs))
        content = get_ai_response(prompt, context, history)
        return {"message": f"Welcome to {content}!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}