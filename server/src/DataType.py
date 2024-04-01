from typing import Tuple,Set,List
import time
'''
## @type Location 位置
## @type Name 名称
## @type Function 功能
## @type Text 文本
## @type Road 道路
'''
Location = Tuple[float,float]
Function = Set[str]
Name = str
Text = List[str]
Road = Tuple[str,str,float,float]

'''
## @brief 建筑类
## @param buildingLocation 位置
## @param buildingName 名称
## @param buildingFunction 功能
'''
class Building:
    buildingLocation:Location = tuple()
    buildingName:Name = ""
    buildingFunction:Function = set()
    '''
    ## @brief 初始化函数和修改以及获取成员变量的函数
    '''
    def __init__(self,location,function,name):
        self.__buildingLocation = location
        self.__buildingName = name
        self.__buildingFunction = function

'''
## @brief 评论类
## @param commentOwner 评论者
## @param commentText 评论内容
## @param commentScore 评论分数
'''
class Comment:
    commentOwner:Name = ""
    commentText:Text = list()
    commentScore:int = 0
    commentTime:Tuple = time.localtime(time.time())

    def __init__(self,owner,text,score,time):
        self.__commentOwner = owner
        self.__commentText = text
        self.__commentScore = score
        self.__commentTime = time
    
'''
## @brief 日记类
## @param journalName 日记名称
## @param journalGrade 日记评分
## @param journalContent 日记内容
## @param journalComment 日记评论
## @param journalDate 日记日期
'''
class journal:
    journalName:Name = ""
    journalGrade:float = 0
    journalContent:Text = list()
    journalComment:Set[Comment]
    journalDate:Tuple = time.localtime(time.time())

    def __init__(self,name,grade,content,comment,date):
        self.__journalName = name
        self.__journalGrade = grade
        self.__journalContent = content
        self.__journalComment = comment
        self.__journalDate = date

class area:
    buildingGroup:Set[Building] = set()