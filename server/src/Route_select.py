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
    dis = dict()
    dis[start] = 0
    heapq.heappush(heap,(0,start))
    for building_id in area.building_group.keys():
        if building_id != start:dis[building_id] = float('inf')
    while(len(heap)>0):
        current = heapq.heappop(heap)
        if current[1] == destination: return current[0],prev
        for e in area.road_group[current[1]]:
            if dis[e.start]+e.length < dis[e.destination]:
                dis[e.destination] = dis[e.start]+e.length
                heapq.heappush(heap,(dis[e.destination],e.destination))
                prev[e.destination] = current[1]
    return -1,prev
