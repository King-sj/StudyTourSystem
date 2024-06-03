import sys
sys.path.append("server")
from src.ScopData import *
async def main():
  res = await Scop_Manager.get_hot_scop()
  pass

if __name__ == "__main__":
  import asyncio
  asyncio.run(main())