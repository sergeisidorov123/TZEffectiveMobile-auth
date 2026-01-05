from fastapi import APIRouter, Depends
from src.core.permissions import check_permission

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.get("/")
def list_docs(
    _: None = Depends(check_permission("documents", "read")),
):
    return ["doc1", "doc2"]


@router.post("/")
def create_doc(
    _: None = Depends(check_permission("documents", "create")),
):
    return {"status": "created"}
