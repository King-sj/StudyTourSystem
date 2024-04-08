from typing import Tuple,Set,List,Dict
import time
'''
@type Location 位置
@type Name 名称
@type Function 功能
@type Text 文本
'''
Location = Tuple[float,float]
Function = Set[str]
Name = str
Text = List[str]

'''
@brief 建筑类
@param building_id 建筑 ID
@param building_location 位置
@param building_name 名称
@param building_function 功能
'''
class Building:
    building_id:int = 0x0000000000000000
    building_location:Location = tuple()
    building_name:Name = ""
    building_function:Function = set()
    def __init__(self,location,function,name,id=0):
        self.building_location = location
        self.building_name = name
        self.building_function = function
        self.building_id = id
    def __eq__(self, other):
        if isinstance(other, Building):
            return self.building_id == other.building_id
        return False
    def __hash__(self):return self.building_id

'''
@brief 评论类
@param comment_owner 评论者
@param comment_text 评论内容
@param comment_score 评论分数
'''
class Comment:
    comment_owner:Name = ""
    comment_text:Text = list()
    comment_score:int = 0
    comment_time:Tuple = time.localtime(time.time())

    def __init__(self,owner,text,score,time):
        self.commentOwner = owner
        self.commentText = text
        self.commentScore = score
        self.commentTime = time
    
'''
@brief 日记类
@param journal_name 日记名称
@param journal_grade 日记评分
@param journal_content 日记内容
@param journal_comment 日记评论
@param journal_date 日记日期
'''
class journal:
    journal_name:Name = ""
    journal_grade:float = 0
    journal_content:Text = list()
    journal_comment:Set[Comment]
    journal_date:Tuple = time.localtime(time.time())

    def __init__(self,name,grade,content,comment,date):
        self.journalName = name
        self.journalGrade = grade
        self.journalContent = content
        self.journalComment = comment
        self.journalDate = date

'''
@param start 起点 id
@param destination 终点 id
@param length 路径长度
@param crowd 拥挤度
@param type 路径类型
'''
class Road:
    start:int
    destination:int
    length:float
    crowd:float
    type:str
    def __init__(self,type,start,destination,length,crowd):
        self.start = start
        self.type = type
        self.destination = destination
        self.length = length
        self.crowd = crowd
    def __eq__(self, other):
        if isinstance(other, Road):
            return self.start == other.start and \
                    self.destination == other.destination and \
                    self.length == other.length and \
                    self.crowd == other.crowd and \
                    self.type == other.type
        return False
    def __hash__(self):
        return hash((self.start, self.destination, self.length, self.crowd, self.type))
        

'''
@param building_group 建筑组
@param road_group 路径组
@param comment_group 评论组
@param grade 评分
@param area_id 区域 ID
'''
class Area:
    area_id:int = 0x0000000000000000
    building_group:Dict[int,Building] = dict()
    road_group:Dict[int,Set[Road]] = dict()
    comment_group:Set[Comment] = set()
    grade:float = 0
    def __init__(self,building_group,road_group,comment_group,grade,area_id):
        self.building_group = building_group
        self.road_group = road_group
        self.comment_group = comment_group
        self.grade = grade
        self.area_id = area_id

    def get_average_degree(self):
        total = 0.0
        for value in self.road_group.values():
            total += len(value)
        return total / len(self.building_group)
    
    def add_building(self,building):
        building.building_id = len(self.building_group) + 1 + self.area_id
        self.building_group[building.building_id] = building

    def add_road(self,road:Road):
        if road.start not in self.building_group.keys() or road.destination not in self.building_group.keys():
            raise AttributeError('AttributeError:building is not exist')
        if road.start not in self.road_group.keys():
            self.road_group[road.start] = set()
        if road.destination not in self.road_group.keys():
            self.road_group[road.destination] = set()
        self.road_group[road.start].add(road)
        self.road_group[road.destination].add(Road(road.type,road.destination,road.start,road.length,road.crowd))

    def get_building(self,id):
        if id not in self.building_group.keys():
            raise AttributeError('AttributeError:building is not exist')
        return self.building_group[id]
    
    def __hash__(self):return self.area_id
