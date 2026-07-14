from fastapi import APIRouter
from fastapi.concurrency import run_in_threadpool

from models.request_models import UserInputRequest
from services.chat_service import generate_reply

router = APIRouter()


@router.post("/user_input")
async def get_user_input(request: UserInputRequest):
    response_text = await run_in_threadpool(
        generate_reply,
        request.session_id,
        request.input_text,
    )
    return {"response": response_text}
