from fastapi import FastAPI
from src.users.routers import router as user_router

app = FastAPI(title="Student Growth Backend (Modular)")

app.include_router(user_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
