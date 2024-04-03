import time
import heapq
from src.DataType import *

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
    if road.start not in area.building_group or road.destination not in area.building_group:
        raise AttributeError('AttributeError:building is not exist')
    if road not in area.road_group[road.start] or road not in area.road_group[road.destination]:
        raise AttributeError('AttributeError:road is not exist')
    if v <= 0:
        raise AttributeError('AttributeError:speed must be positive')
    start_degree = len(area.road_group[road.start])
    destination_degree = len(area.road_group[road.destination])
    return road.length / v \
    / (1+get_crowd(road,start_degree,destination_degree,area.get_average_degree()))

def get_shortest_road(area:Area,start:int,destination:int,mode:int = 0):
    heap = []
    prev = dict()
    dis = dict()
    for building in area.building_group:
        if building.building_id == start:
            dis[building.building_id] = 0.0
            heapq.heappush(heap,(0.0,start))
        else:dis[building.building_id] = float('inf')
    while(len(heap)>0):
        current = heapq.heappop(heap)
        if current[0] == destination: return current[1],prev
        for e in area.road_group[current[0]]:
            if dis[e.start.building_id]+e.length < dis[e.destination.building_id]:
                dis[e.destination.building_id] = dis[e.start.building_id]+e.length
                heapq.heappush(heap,(dis[e.destination.building_id],e.destination.building_id))
                prev[e.destination.building_id] = current[0]
    return -1,prev
