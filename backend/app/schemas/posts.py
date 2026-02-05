from pydantic import BaseModel, Field

class PostCreate(BaseModel):
    content: str = Field(min_length=1, max_length=5000)

class PostOut(BaseModel):
    id: int
    user_id: int
    content: str
    created_at: str
    updated_at: str


