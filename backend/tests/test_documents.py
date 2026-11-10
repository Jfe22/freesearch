
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# Ficheiro de teste com assinatura PDF, não é um PDF completo.
FAKE_PDF = b"%PDF-1.4\nsample content"


def upload(filename, content, content_type):
    return client.post(
        "/documents/upload",
        files={
            "file": (filename, content, content_type)
        },
    )


def test_valid_pdf_signature():
    response = upload(
        "example.pdf",
        FAKE_PDF,
        "application/pdf",
    )

    assert response.status_code == 200
    assert response.json()["size_bytes"] == len(FAKE_PDF)


def test_empty_pdf():
    response = upload(
        "empty.pdf",
        b"",
        "application/pdf",
    )

    assert response.status_code == 400


def test_invalid_extension():
    response = upload(
        "example.txt",
        FAKE_PDF,
        "application/pdf",
    )

    assert response.status_code == 415


def test_invalid_content_type():
    response = upload(
        "example.pdf",
        FAKE_PDF,
        "text/plain",
    )

    assert response.status_code == 415


def test_invalid_signature():
    response = upload(
        "example.pdf",
        b"not a real pdf",
        "application/pdf",
    )

    assert response.status_code == 415


def test_file_too_large():
    content = FAKE_PDF + b"x" * (10 * 1024 * 1024)

    response = upload(
        "large.pdf",
        content,
        "application/pdf",
    )

    assert response.status_code == 413


def test_missing_file():
    response = client.post("/documents/upload")

    assert response.status_code == 422

