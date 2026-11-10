from fastapi import APIRouter, UploadFile

from app.services.pdf_validator import validate_pdf

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post("/upload", status_code=200)
async def upload_document(file: UploadFile):
    size = await validate_pdf(file)

    return {
        "message": "PDF validation successful",
        "size_bytes": size,
    }

