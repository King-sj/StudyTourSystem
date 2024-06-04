import sys
sys.path.append("server")
from src.ScopData import *
async def main():
  suc,res = await Scop_Manager.get_history(
    "tSwooauuMH3PhQgOgrgHtLW3nWUK7qjL"
  )
  pass

if __name__ == "__main__":
  import asyncio
  asyncio.run(main())