from fastapi import FastAPI

app = FastAPI(title="Student Growth Backend")

@app.get("/health")
def health_check():
    return {"status": "ok"}