from typing import Dict, List, Optional
from datetime import datetime, timezone
import uuid  # For generating unique IDs

from .models import (
    Document,
    DocumentCreate,
    DocumentUpdate,
    DocumentStatus,
)


class DocumentStorage:
    def __init__(self):
        self._documents: Dict[str, Document] = {}  # <-- Provided, don't change

    def create_document(self, document_data: DocumentCreate) -> Document:
        """
        Create a new document and return it with generated ID

        Useful:
            uuid.uuid4() for IDs
            datetime.utcnow() for timestamps.

        Required Document fields:
            id
            title
            content
            document_type
            status (default: DRAFT)
            created_at
            updated_at
        """
        now = datetime.now(timezone.utc)
        document_id = str(uuid.uuid4())
        
        document = Document(
            id            = document_id,
            title         = document_data.title,
            content       = document_data.content,
            document_type = document_data.document_type,
            status        = DocumentStatus.DRAFT,
            created_at    = now,
            updated_at    = now,
        )

        self._documents[document_id] = document
        return document

    def get_document(self, document_id: str) -> Optional[Document]:
        """
        Get document by ID
        """
        raise NotImplementedError("TODO: Implement get_document")

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
        raise NotImplementedError("TODO: Implement update_document")

    def delete_document(self, document_id: str) -> bool:
        """
        Delete document, return True if successful
        """
        raise NotImplementedError("TODO: Implement delete_document")

    def list_documents(
        self,
        status: Optional[str] = None,
        document_type: Optional[str] = None,
    ) -> List[Document]:
        """
        List documents with optional filtering
        """
        raise NotImplementedError("TODO: Implement list_documents")