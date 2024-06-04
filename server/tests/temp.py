import sys
sys.path.append("server")
from src.ScopData import *
import random
async def main():
  db = await Scop_Manager.link_database()
  async for doc in db["scops"].find({}):
    await db["score"].update_one(
      {"name":doc["name"]},
      {
        "$set":{
          "name":doc["name"],
          "province":doc["province"],
          "city":doc["city"],
          "score": (3.0+random.random()*7) ,
          "visited_person":random.randint(1000,100000)
        }
      },
      upsert=True
    )

if __name__ == "__main__":
  import asyncio
  asyncio.run(main())