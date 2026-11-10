from fastapi import FastAPI

from app.routes.documents import router as documents_router


app = FastAPI(
    title="FreeSearch",
    version="0.1.0",
)


app.include_router(documents_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
