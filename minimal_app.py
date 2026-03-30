# Ultra-simple FastAPI app for Railway - guaranteed to work
from fastapi import FastAPI
import os

app = FastAPI(title="ResolveAI API")

@app.get("/")
async def root():
    return {
        "message": "ResolveAI API is running",
        "status": "success",
        "service": "AI Smart Grievance System"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "ResolveAI API",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8001))
    uvicorn.run(app, host="0.0.0.0", port=port)
