from typing import Tuple,Set,List
import time
'''
## @type Location 位置
## @type Name 名称
## @type Function 功能
## @type Text 文本
'''
Location = Tuple[float,float]
Function = Set[str]
Name = str
Text = List[str]

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
    def getBuildingLocation(self):
        return self.__buildingLocation
    def getBuildingName(self):
        return self.__buildingName
    def getBuildingFunction(self):
        return self.__buildingFunction
    def setBuildingFunction(self,function):
        self.__buildingFunction = set(function)
    def setBuildingName(self,name):
        self.__buildingName = str(name)
    def setBuildingLocation(self,location):
        self.__buildingLocation = tuple(location)

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
    def getCommentOwner(self):
        return self.__commentOwner
    def getCommentText(self):
        return self.__commentText
    def getCommentScore(self):
        return self.__commentScore
    def getCommentTime(self):
        return self.__commentTime
    def setCommentOwner(self,owner):
        self.__commentOwner = str(owner)
    def setCommentText(self,text):
        self.__commentText = list(text)
    def setCommentScore(self,score):
        self.__commentScore = score
    def setCommentTime(self,time):
        self.__commentTime = tuple(time)

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

    def getJournalName(self):
        return self.__journalName
    def getJournalGrade(self):
        return self.__journalGrade
    def getJournalContent(self):
        return self.__journalContent
    def getJournalComment(self):
        return self.__journalComment
    def getJournalDate(self):
        return self.__journalDate
    def setJournalName(self,name):
        self.__journalName = str(name)
    def setJournalGrade(self,grade):
        self.__journalGrade = grade
    def setJournalContent(self,content):
        self.__journalContent = list(content)
    def setJournalComment(self,comment):
        self.__journalComment = set(comment)
    def setJournalDate(self,date):
        self.__journalDate= tuple(date)