import motor.motor_asyncio
import pydantic
import json
from fastapi import Query

__client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
__users = __client['PerfectGame']['users']


class User(pydantic.BaseModel):
    user_name: str = Query('', min_length=1, max_length=50)
    x: int
    y: int


async def get_user(user_name) -> dict:
    ans = await __users.find_one({'user_name': user_name})
    return ans


async def post_user(user: User):
    info = json.loads(user.json())
    if await __users.find_one({'user_name': user.user_name}) is None:
        return await __users.insert_one(info)
    else:
        return await __users.replace_one({'user_name': user.user_name}, info)

