import sys
sys.path.append('server')
from src.Route_select import *
import random

def test_one():
    buildings = list()
    for i in range(0,10):
        buildings.append(Building((0,0),set(),str(i),i))
    area = Area(set(),dict(),set(),0)
    for i in range(0,10):
        random_start = random.randint(0,9)
        random_end = random.randint(0,9)
        random_length = random.randint(1,100)
        area.add_road(Road('road',buildings[random_start],buildings[random_end],random_length,0))
    result = get_shortest_road(area,0,9)
    print(result)
    assert result[0] == -1

test_one()