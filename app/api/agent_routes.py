from fastapi import APIRouter, HTTPException
from app.graph.workflow import workflow

router = APIRouter()


@router.post("/agent")
def run_agent(payload: dict):
    """
    Receives natural language input,
    executes LangGraph workflow,
    returns structured output.
    """

    try:
        user_input = payload.get("input")

        if not user_input:
            raise HTTPException(
                status_code=400,
                detail="Missing 'input' field"
            )

        # Run LangGraph workflow
        result = workflow.invoke({
            "input": user_input,
            "summary": None,
            "email": None,
            "final_output": None
        })

        return {
            "input": user_input,
            "final_output": result.get("final_output"),
            "summary": result.get("summary"),
            "email": result.get("email"),
            "status": "success"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }