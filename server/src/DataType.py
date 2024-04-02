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
@param building_location 位置
@param building_name 名称
@param building_function 功能
'''
class Building:
    building_location:Location = tuple()
    building_name:Name = ""
    building_function:Function = set()
    def __init__(self,location,function,name):
        self.building_location = location
        self.building_name = name
        self.building_function = function
    def __eq__(self, other):
        if isinstance(other, Building):
            return self.building_location == other.building_location and \
                    self.building_name == other.building_name and \
                    self.building_function == other.building_function
        return False
    

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
@param start 起点
@param destination 终点
@param length 路径长度
@param crowd 拥挤度
@param type 路径类型
'''
class Road:
    start:Building
    destination:Building
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

'''
@param building_group 建筑组
@param road_group 路径组
@param comment_group 评论组
@param grade 评分
'''
class Area:
    building_group:Set[Building] = set()
    road_group:Dict[Building,Set[Road]] = dict()
    comment_group:Set[Comment] = set()
    grade:float = 0
    
    def __init__(self,building,road,comment,grade):
        self.building_group = building
        self.road_group = road
        self.comment_group = comment
        self.grade = grade
    def get_average_degree(self):
        total = 0.0
        for value in self.road_group.values():
            total += len(value)
        return total / len(self.road_group)