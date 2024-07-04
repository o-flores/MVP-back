from pydantic import BaseModel

class MessageSchema(BaseModel):
  message: str
  code: int

def list_message(message: MessageSchema):
  return {"message": message.message}, message.code