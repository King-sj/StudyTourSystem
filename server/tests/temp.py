import sys
sys.path.append("server")
from src.ScopData import *
import random
async def main():
  db = await Scop_Manager.get_jours("颐和园")
  pass

if __name__ == "__main__":
  import asyncio
  asyncio.run(main())