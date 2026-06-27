from pydantic import BaseModel
from enum import Enum
from typing import Optional
from datetime import datetime


class DocumentType(str, Enum):
    CONTRACT = "contract"
    CORRESPONDENCE = "correspondence"
    CASE_FILE = "case_file"


class DocumentStatus(str, Enum):
    DRAFT = "draft"
    REVIEWED = "reviewed"
    FINAL = "final"


class DocumentCreate(BaseModel):
    title: str
    content: str
    document_type: DocumentType


class DocumentUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    status: Optional[DocumentStatus] = None


class Document(BaseModel):
    id: str
    title: str
    content: str
    document_type: DocumentType
    status: DocumentStatus = DocumentStatus.DRAFT
    created_at: datetime
    updated_at: datetime