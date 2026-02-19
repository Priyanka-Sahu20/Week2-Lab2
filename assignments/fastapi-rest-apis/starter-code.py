"""
FastAPI REST API Assignment - Starter Code

This starter code provides the foundation for building a REST API with FastAPI.
Your task is to implement the endpoints for managing items.

Instructions:
1. Install FastAPI and uvicorn: pip install fastapi uvicorn
2. Implement the endpoints as specified in the assignment
3. Test your API using the interactive documentation at http://localhost:8000/docs
4. Run: uvicorn starter-code:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(
    title="Item Management API",
    description="A simple REST API for managing items",
    version="1.0.0"
)

# Data Models
class Item(BaseModel):
    """Pydantic model for an item"""
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float


# Sample data storage (in-memory)
items_db = [
    {"id": 1, "name": "Laptop", "description": "High-performance laptop", "price": 999.99},
    {"id": 2, "name": "Mouse", "description": "Wireless mouse", "price": 29.99}
]

# TODO: Implement your endpoints below

# GET /items - Retrieve all items
# GET /items/{item_id} - Retrieve a specific item
# POST /items - Create a new item
# PUT /items/{item_id} - Update an existing item
# DELETE /items/{item_id} - Delete an item


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to the Item Management API"}
