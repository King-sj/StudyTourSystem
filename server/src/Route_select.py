import time
import heapq
from DataType import *

'''
@param start_degree 起点度
@param destination_degree 终点度
@param average_degree 平均度
@param 目标道路
@return 拥挤度
'''
def get_crowd(road:Road,start_degree,destination_degree,average_degree):
    current_time = time.localtime(time.time())
    if current_time.tm_hour >= 0 and current_time.tm_hour < 7:time_coefficient = 0.5
    elif current_time.tm_hour >= 7 and current_time.tm_hour < 10:time_coefficient = 2
    elif current_time.tm_hour >= 10 and current_time.tm_hour < 17:time_coefficient = 1.5
    elif current_time.tm_hour >= 17 and current_time.tm_hour < 20:time_coefficient = 2
    else:time_coefficient = 0.5
    busy_coefficient:float = (start_degree + destination_degree) / 2.0 / average_degree
    road.crowd = time_coefficient * busy_coefficient
    return road.crowd 

'''
@param area 区域
@param road 道路
@param v 速度
@return 时间
'''
def get_time(area:Area,road:Road,v:float):
    check = False
    for value in area.road_group.values():
        for r in value:
            if r == road:check = True
    if not check:raise AttributeError('Road not in area')
    road.crowd = get_crowd(road,len(area.road_group[road.start]),
                        len(area.road_group[road.destination]),area.get_average_degree())
    return road.length/ v / (1 + road.crowd)

def get_shortest_road(area:Area,start:int,destination:int,mode:int = 0):
    heap = []
    prev = dict()
    st:Dict[int,bool] = dict();
    dist:Dict[int,float] = dict()

    for building in area.building_group.keys():
        dist[building] = float('inf')
        st[building] = False
    
    dist[start] = 0
    prev[start] = -1
    heapq.heappush(heap,(0,start))
    while(len(heap)>0):
        current = heapq.heappop(heap)
        if(st[current[1]]):continue
        st[current[1]] = True
        if current[1] == destination: return current[0],prev
        for e in area.road_group[current[1]]:
            if dist[e.start]+e.length < dist[e.destination]:
                dist[e.destination] = dist[e.start]+e.length
                prev[e.destination] = current[1]
                if(st[e.destination] == False):
                    heapq.heappush(heap,(dist[e.destination],e.destination))
    return -1,dict()


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
    return result[0] == 10 and result[1][10] == 1


