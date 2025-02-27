import motor.motor_asyncio
from redis import asyncio as aioredis
import hashlib
import random
import string


async def link_redis():
  """连接到Redis"""
  redis_client = await aioredis.from_url('redis://localhost')
  return redis_client


async def link_mongo():
  client = motor.motor_asyncio.AsyncIOMotorClient(
        'mongodb://localhost:27017/')
  db = client['StudyTourSystem']
  collection = db['users']
  return collection


async def generate_captcha(email: str, length: int = 6):
  """生成验证码"""
  captcha = ''.join(random.choice(string.digits) for _ in range(length))
  await store_captcha(email, captcha)
  return captcha


async def store_captcha(account, captcha):
  """存储验证码到Redis，设置5分钟过期"""
  redis_client = await link_redis()
  await redis_client.setex(f"{account}-captcha", 300, captcha)


async def exist_user(account: str) -> bool:
  """判断用户是否存在"""
  collection = await link_mongo()
  res = await collection.find_one({"account": account})
  return res is not None


async def verify_captcha(account: str, captcha: str) -> bool:
  """验证验证码"""
  redis_client = await link_redis()
  stored_captcha = await redis_client.get(f"{account}-captcha")
  if stored_captcha is None or stored_captcha.decode('utf-8') != captcha:
    return False
  return True


async def register_account(account, password, captcha) -> tuple[bool, str]:
  """注册账户，先检查验证码是否正确，然后存储账号和加密后的密码到MongoDB"""
  # 检查用户是否存在
  if await exist_user(account):
    return (False, "用户已存在")
  # 验证验证码
  if await verify_captcha(account, captcha) is False:
    return (False, "验证码错误或已过期")

  # 加密密码
  hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
  collection = await link_mongo()
  await collection.insert_one({
    "account":account,
    "password":hashed_password
  })
  return (True, '')


async def login(account: str, psw: str) -> tuple[bool, str]:
  """登录"""
  collection = await link_mongo()
  res = await collection.find_one({"account":account})
  if res is None:
    return (False, "用户不存在")
  # 验证密码
  if res["password"] != hashlib.sha256(psw.encode('utf-8')).hexdigest():
    return (False, "密码错误")
  return (True, await generate_token(account))


async def generate_token(account:str) -> str:
  """生成token"""
  redis_client =await link_redis()
  # 判断是否存在token
  token = await redis_client.get(account+"-token")
  if token:
    return token.decode('utf-8')
  # 生成token
  letters = string.ascii_letters + string.digits
  while True:
    random_string = ''.join(random.choice(letters) for _ in range(32))
    if (not await redis_client.exists(random_string)):
      break
  """存储token到Redis, 设置0.5day过期"""
  await redis_client.setex(random_string, 60*60*12, account)
  await redis_client.setex(account+"-token", 60*60*12, random_string)
  return random_string

async def test():
  redis_client = await link_redis()
  keys = await redis_client.keys("*")
  for key in keys:
    print(key)
  res = await login("2175616761@qq.com","12345678")
  print(res)
  pass

if __name__ == "__main__":
  import asyncio
  asyncio.run(test())