from pydantic import BaseModel


class UserInputRequest(BaseModel):
    session_id: str = "default"
    input_text: str
