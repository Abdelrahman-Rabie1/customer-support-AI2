from fastapi import FastAPI
from app.routers import home , colleges

app = FastAPI(title="Banha National University API")


app.include_router(home.router)
app.include_router(colleges.router, prefix="/colleges", tags=["Colleges"])

@app.get("/")
def root():
    return {"status": "ok", "message": "API is running"}