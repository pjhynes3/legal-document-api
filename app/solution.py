from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from .database import Base, engine
from .models import (
    Document,
    DocumentCreate,
    DocumentUpdate,
    DocumentStatus,
    DocumentType
)
from .document_service import DocumentService

from .database import Base, engine
from . import db_models


app = FastAPI(title="Legal Document Management API")

document_service = DocumentService()


@app.post("/documents", response_model=Document)
async def create_document(document_data: DocumentCreate):
    """Create a new document"""
    return document_service.create_document(document_data)


@app.get("/documents/{document_id}", response_model=Document)
async def get_document(document_id: str):
    """Get document by ID"""
    document = document_service.get_document(document_id)
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return document


@app.put("/documents/{document_id}", response_model=Document)
async def update_document(
    document_id: str,
    updates: DocumentUpdate,
):
    """Update document"""
    try:
        updated_document = document_service.update_document(document_id, updates)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    if updated_document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return updated_document


@app.delete("/documents/{document_id}")
async def delete_document(document_id: str):
    """Delete document"""
    deleted = document_service.delete_document(document_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"message": "Document deleted successfully"}


@app.get("/documents", response_model=List[Document])
async def list_documents(
    status: Optional[DocumentStatus] = Query(None),
    document_type: Optional[DocumentType] = Query(None),
):
    """List documents with optional filtering"""
    return document_service.list_documents(status, document_type)