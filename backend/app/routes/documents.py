from fastapi import APIRouter, HTTPException, UploadFile
from starlette.concurrency import run_in_threadpool

from app.services.pdf_validator import validate_pdf
from app.services.pdf_extractor import (
    extract_pdf_text,
    PDFExtractionError,
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)



@router.post("/upload", status_code=200)
async def upload_document(file: UploadFile):
    size = await validate_pdf(file)

    return {
        "message": "PDF validation successful",
        "size_bytes": size,
    }



@router.post("/extract")
async def extract_document(file: UploadFile):
    try:
        size = await validate_pdf(file)

        try:
            result = await run_in_threadpool(
                extract_pdf_text,
                file.file,
            )
        except PDFExtractionError as exc:
            raise HTTPException(
                status_code=422,
                detail=str(exc),
            ) from exc

        return {
            "size_bytes": size,
            **result,
        }
    finally:
        await file.close()