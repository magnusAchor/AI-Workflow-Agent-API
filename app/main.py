from fastapi import FastAPI
from app.api.agent_routes import router

app = FastAPI(
    title="AI Workflow Agent API",
    version="1.0.0"
)

# Register routes
app.include_router(router)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "AI Workflow Agent API is running"
    }