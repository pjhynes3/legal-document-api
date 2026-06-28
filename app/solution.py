from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional

from .models import (
    Document,
    DocumentCreate,
    DocumentUpdate,
)
from .document_service import DocumentService


app = FastAPI(title="Legal Document Management API")

document_service = DocumentService()


@app.post("/documents", response_model=Document)
async def create_document(document_data: DocumentCreate):
    """Create a new document"""
    raise HTTPException(status_code=501, detail="Not implemented")


@app.get("/documents/{document_id}", response_model=Document)
async def get_document(document_id: str):
    """Get document by ID"""
    raise HTTPException(status_code=501, detail="Not implemented")


@app.put("/documents/{document_id}", response_model=Document)
async def update_document(
    document_id: str,
    updates: DocumentUpdate,
):
    """Update document"""
    raise HTTPException(status_code=501, detail="Not implemented")


@app.delete("/documents/{document_id}")
async def delete_document(document_id: str):
    """Delete document"""
    raise HTTPException(status_code=501, detail="Not implemented")


@app.get("/documents", response_model=List[Document])
async def list_documents(
    status: Optional[str] = Query(None),
    document_type: Optional[str] = Query(None),
):
    """List documents with optional filtering"""
    raise HTTPException(status_code=501, detail="Not implemented")