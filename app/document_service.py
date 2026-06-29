from typing import List, Optional

from .models import (
    Document,
    DocumentCreate,
    DocumentUpdate,
    DocumentStatus,
)
from .storage import DocumentStorage
from .cache import cache_get, cache_set, cache_delete


class DocumentService:
    def __init__(self):
        self.storage = DocumentStorage()

    def create_document(self, document_data: DocumentCreate) -> Document:
        """
        Create new document with business logic validation
        """
        return self.storage.create_document(document_data)

    def get_document(self, document_id: str) -> Optional[Document]:
        """
        Get document with caching
        """
        # TODO: Implement get with cache-aside pattern
        # Hint: Check cache first, then storage
        cache_key = f"document:{document_id}"

        cached_document = cache_get(cache_key)
        if cached_document is not None:
            return cached_document
        # not in cache? now we grab from storage & put it in cache
        document = self.storage.get_document(document_id)
        if document is not None:
            cache_set(cache_key, document)
        return document

    def update_document(
        self,
        document_id: str,
        updates: DocumentUpdate,
    ) -> Optional[Document]:
        """
        Update document with validation
        """
        # TODO: Implement update with business rules
        # Consider:
        #   status transition validation
        #   cache invalidation
        document = self.storage.get_document(document_id)
        if document is None:
            return None
        
        if updates.status is not None:
            if not self._is_valid_status_transition(document.status, updates.status):
                raise ValueError("Invalid status transition")
        
        updated_document = self.storage.update_document(document_id, updates)

        cache_key = f"document:{document_id}"
        cache_delete(cache_key)
        return self.update_document

    def delete_document(self, document_id: str) -> bool:
        """
        Delete document with cleanup
        """
        # TODO: Implement deletion with cache cleanup
        if not self.storage.delete_document(document_id):
            return False
        cache_key = f"document:{document_id}"
        cache_delete(cache_key)
        return True
    
    def list_documents(
        self,
        status: Optional[str] = None,
        document_type: Optional[str] = None,
    ) -> List[Document]:
        """
        List documents with optional filtering.

        For this exercise, simply return filtered results from storage.
        Do NOT implement caching for list operations.
        """
        # TODO: Implement document listing with filters
        return self.storage.list_documents(status, document_type)

    def _is_valid_status_transition(
        self,
        current: DocumentStatus,
        new: DocumentStatus,
    ) -> bool:
        """
        Validate status transitions

        Valid transitions:
            draft -> reviewed
            reviewed -> final
            final -> final

        Same status is always valid.
        """
        if current == new:  # same status is always valid
            return True
        
        valid_transitions = {
            DocumentStatus.DRAFT: DocumentStatus.REVIEWED,
            DocumentStatus.REVIEWED: DocumentStatus.FINAL,
        }
        return valid_transitions.get(current) == new