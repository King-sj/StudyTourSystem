import sys
sys.path.append('server')
from src.Route_select import *
from src.DataType import *
import random


def test_shortest_road():
    # 创建10个Building对象
    buildings = {i: Building((0,0),set(),str(i)) for i in range(1, 11)}

    # 创建10条Road对象，每条Road的起点和终点都是一个Building
    roads = {i: Road('road',i, (i % 10) + 1,i,0) for i in range(1, 11)}

    # 创建一个Area对象
    area = Area(dict(),dict(),set(),0,0)
    for b in buildings.values():area.add_building(b)
    for r in roads.values():area.add_road(r)
    result = get_shortest_road(area,1,10)
    assert result[0] == 10 and result[1][10] == 1

