from fastapi import HTTPException, UploadFile

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MiB
CHUNK_SIZE = 1024 * 1024  # 1 MiB
PDF_SIGNATURE = b"%PDF-"


async def validate_pdf(file: UploadFile) -> int:
    filename = file.filename or ""

    if not filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=415,
            detail="File must have a .pdf extension",
        )

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=415,
            detail="Invalid PDF content type",
        )

    try:
        header = await file.read(len(PDF_SIGNATURE))

        if not header:
            raise HTTPException(
                status_code=400,
                detail="File is empty",
            )

        if header != PDF_SIGNATURE:
            raise HTTPException(
                status_code=415,
                detail="Invalid PDF signature",
            )

        size = len(header)

        while chunk := await file.read(CHUNK_SIZE):
            size += len(chunk)

            if size > MAX_FILE_SIZE:
                raise HTTPException(
                    status_code=413,
                    detail="File exceeds the 10 MiB limit",
                )

        return size

    finally:
        await file.close()
