from fastapi import FastAPI, HTTPException

import fu
from fu import User

app = FastAPI()


@app.get("/user/{user_name: str}", response_model=User)
async def root(user_name: str):
    ans = await fu.get_user(user_name)
    if ans is None:
        raise HTTPException(404, "Player was not found!")
    return ans


@app.post("/user/{user: User}")
async def root(user: User):
    await fu.post_user(user)
    return
