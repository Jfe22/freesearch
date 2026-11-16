
from io import BytesIO

from fastapi.testclient import TestClient
from reportlab.pdfgen import canvas

from app.main import app

client = TestClient(app)


def create_pdf(page_texts):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)

    for text in page_texts:
        pdf.drawString(72, 750, text)
        pdf.showPage()

    pdf.save()
    return buffer.getvalue()


def upload_for_extraction(content):
    return client.post(
        "/documents/extract",
        files={
            "file": (
                "test.pdf",
                content,
                "application/pdf",
            )
        },
    )


def test_extract_single_page():
    content = create_pdf(["Hello FreeSearch"])

    response = upload_for_extraction(content)

    assert response.status_code == 200
    assert response.json()["page_count"] == 1
    assert response.json()["pages"][0] == {
        "page_number": 1,
        "text": "Hello FreeSearch",
    }


def test_extract_multiple_pages():
    content = create_pdf([
        "First page",
        "Second page",
    ])

    response = upload_for_extraction(content)

    assert response.status_code == 200

    pages = response.json()["pages"]

    assert len(pages) == 2
    assert pages[0]["page_number"] == 1
    assert "First page" in pages[0]["text"]
    assert pages[1]["page_number"] == 2
    assert "Second page" in pages[1]["text"]


def test_reject_invalid_pdf_structure():
    response = upload_for_extraction(
        b"%PDF-1.4\nnot a valid PDF"
    )

    assert response.status_code == 422


def test_reject_pdf_without_text():
    content = create_pdf([""])

    response = upload_for_extraction(content)

    assert response.status_code == 422
    assert response.json()["detail"] == (
        "No extractable text found in PDF"
    )


def test_reject_too_many_pages():
    content = create_pdf(["Page"] * 31)

    response = upload_for_extraction(content)

    assert response.status_code == 422
    assert "30-page limit" in response.json()["detail"]
