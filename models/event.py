from pydantic import BaseModel


class Message(BaseModel):
    from_id: int
    text: str
    attachments: list | None
