from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field

from app.db.session import get_connection
from app.api.auth import get_current_user

router = APIRouter(prefix="/posts", tags=["posts"])

# Schemas

class PostCreate(BaseModel):
    content: str = Field(min_length=1, max_length=5000)

class PostUpdate(BaseModel):
    content: str = Field(min_length=1, max_length=5000)

class PostOut(BaseModel):
    id: int
    user_id: int
    username: str
    content: str
    created_at: datetime
    updated_at: datetime

class User(BaseModel):
    id: int
    username: str

# ---- Helpers ----

def fetchone_to_dict(cur) -> Optional[dict]:
    row = cur.fetchone()
    if row is None:
        return None
    cols = [desc[0] for desc in cur.description]
    return dict(zip(cols, row))


def fetchall_to_dict(cur) -> List[dict]:
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    return [dict(zip(cols, row)) for row in rows]

# Routes

@router.post("", response_model=PostOut, status_code=status.HTTP_201_CREATED)
def create_post(payload: PostCreate, current_user: User=Depends(get_current_user)):
    conn = get_connection()
    cur = conn.cursor()

    try:
        # Inserting and creating a post
        cur.execute(
            """
            INSERT INTO posts (user_id, content)
            VALUES (%s, %s)
            RETURNING id  
            """,
            (current_user["id"], payload.content)
        )
        post_id = cur.fetchone()[0]

        # Crafting the final post info
        cur.execute(
            """
            SELECT
                p.id,
                p.content,
                p.created_at,
                p.updated_at,
                u.id as user_id,
                u.username
            FROM posts p
            JOIN users u ON u.id = p.user_id
            WHERE p.id = %s
            """,
            (post_id,),
        )

        post = fetchone_to_dict(cur)
        conn.commit
        return post

    finally:
        cur.close()
        conn.close()


    
