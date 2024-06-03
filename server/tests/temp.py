import sys
sys.path.append("server")
from src.ScopData import *
async def main():
  res = await Scop_Manager.uploadJour(
    "hhhh",
    "颐和园",
    3.5,
    "北京",
    "北京",
    "SsK7MpWPJ1sdjRYaKYDg7QWPCD1rXqmD"
  )
  pass

if __name__ == "__main__":
  import asyncio
  asyncio.run(main())