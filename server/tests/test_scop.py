from src.ScopData import Scop_Manager
import sys
sys.path.append(".\\server")


def test_mongo():
  print(Scop_Manager.get_all())
