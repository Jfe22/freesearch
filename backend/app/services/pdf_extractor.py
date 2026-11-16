
from pypdf import PdfReader
from pypdf.errors import PdfReadError

MAX_PAGES = 30
MAX_PAGE_TEXT_CHARS = 100_000


class PDFExtractionError(Exception):
    pass


def extract_pdf_text(file) -> dict:
    try:
        file.seek(0)
        reader = PdfReader(file, strict=True)

        if reader.is_encrypted:
            raise PDFExtractionError(
                "Password-protected PDFs are not supported"
            )

        page_count = len(reader.pages)

        if page_count > MAX_PAGES:
            raise PDFExtractionError(
                f"PDF exceeds the {MAX_PAGES}-page limit"
            )

        pages = []

        for index, page in enumerate(reader.pages):
            text = (page.extract_text() or "").strip()

            if len(text) > MAX_PAGE_TEXT_CHARS:
                raise PDFExtractionError(
                    "Extracted page text exceeds the limit"
                )

            pages.append({
                "page_number": index + 1,
                "text": text,
            })

        if not any(page["text"] for page in pages):
            raise PDFExtractionError(
                "No extractable text found in PDF"
            )

        return {
            "page_count": page_count,
            "pages": pages,
        }

    except PdfReadError as exc:
        raise PDFExtractionError(
            "Invalid or unreadable PDF"
        ) from exc
