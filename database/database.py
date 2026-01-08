from config import DB_URL, DB_NAME
from motor.motor_asyncio import AsyncIOMotorClient


# clients setup 
_client = AsyncIOMotorClient(DB_URL) 
_db = _client[DB_NAME] 
_users = _db.users # collection name "users"

# save id 
async def add_user(user_id: int):
  await _users.update_one(
    {"_id": user_id}, {"$setOnInsert": {"_id": user_id}}, upsert=True
  )
  
# get all users 
async def get_all_users() -> list[int]:
  curser = _users.find({}, {"_id": 1}) 
  return [doc["_id"] async for doc in curser] 
  
# delete users [bot blocked or deactivated account cleanup] 
async def del_user(user_id: int):
  await _users.delete_one({"_id": user_id}) 
