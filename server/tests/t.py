import sys
sys.path.append("server")
from src.ScopData.Scop import *
import motor.motor_asyncio
async def main():
  client = motor.motor_asyncio.AsyncIOMotorClient(
    'mongodb://localhost:27017/')
  db = client['StudyTourSystem']
  collection = db['score']
  await collection.create_index("name",unique=True)
  scops = await Scop_Manager.get_all()
  for scop in scops:
    name = scop["name"]
    province = scop["province"]
    city = scop["city"]
    await collection.insert_one({
      "name" : name,
      "province" : province,
      "city" : city,
      "score" : 0,
      "visited_person" : 0
    })

  client.close()
if __name__ == "__main__":
  import asyncio
  asyncio.run(main())
print("done")