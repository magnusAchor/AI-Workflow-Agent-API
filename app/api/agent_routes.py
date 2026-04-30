from fastapi import APIRouter
from app.graph.workflow import workflow

router = APIRouter()


@router.post("/agent")
def run_agent(payload: dict):
    try:
        result = workflow.invoke({
            "input": payload["input"],
            "article": None,
            "email": None,
            "final_output": None
        })

        return {
            "input": payload["input"],
            "article": result.get("article"),
            "email": result.get("email"),
            "final_output": result.get("final_output"),
            "status": "success"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }