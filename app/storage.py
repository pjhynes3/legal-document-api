from typing import Dict, List, Optional
from datetime import datetime, timezone
from .database import SessionLocal
from .db_models import DocumentRow
import uuid  # For generating unique IDs

from .models import (
    Document,
    DocumentCreate,
    DocumentUpdate,
    DocumentStatus,
    DocumentType
)


class DocumentStorage:
    def __init__(self):
        self._documents: Dict[str, Document] = {}  # <-- Provided, don't change

    def create_document(self, document_data: DocumentCreate) -> Document:
        now = datetime.now(timezone.utc)
        document_id = str(uuid.uuid4())

        document_row = DocumentRow(
            id=document_id,
            title=document_data.title,
            content=document_data.content,
            document_type=document_data.document_type.value,
            status=DocumentStatus.DRAFT.value,
            created_at=now,
            updated_at=now,
        )

        db = SessionLocal()
        db.add(document_row)
        db.commit()
        db.refresh(document_row)
        db.close()

        return Document(
            id=document_row.id,
            title=document_row.title,
            content=document_row.content,
            document_type=DocumentType(document_row.document_type),
            status=DocumentStatus(document_row.status),
            created_at=document_row.created_at,
            updated_at=document_row.updated_at,
        )

    def get_document(self, document_id: str) -> Optional[Document]:
        """
        Get document by ID
        """
        return self._documents.get(document_id)

    def update_document(
        self,
        document_id: str,
        updates: DocumentUpdate,
    ) -> Optional[Document]:
        """
        Update document and return updated version

        Hint:
            Remember to update the updated_at timestamp.
        """
        document = self._documents.get(document_id)
        if document is None:
            return None
        if updates.title is not None:
            document.title = updates.title
        if updates.content is not None:
            document.content = updates.content
        if updates.status is not None:
            document.status = updates.status

        # IMPORTANT : update timestamp!
        document.updated_at = datetime.now(timezone.utc)

        self._documents[document_id] = document
        return document
    
    def delete_document(self, document_id: str) -> bool:
        """
        Delete document, return True if successful
        """
        if document_id not in self._documents:
            return False
        del self._documents[document_id]
        return document_id not in self._documents

    def list_documents(
        self,
        status: Optional[DocumentStatus] = None,
        document_type: Optional[DocumentType] = None,
    ) -> List[Document]:
        """
        List documents with optional filtering
        """
        # if no status or doc type, list all. otherwise match those
        documents = list(self._documents.values())

        if status is not None:
            documents = [
                document 
                for document in documents
                if document.status == status
            ]

        if document_type is not None:
            documents = [
                document 
                for document in documents
                if document.document_type == document_type
            ]

        return documents
