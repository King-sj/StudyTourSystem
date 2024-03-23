'''
# @param Location 位置
# @param Name 名称
# @param Function 功能
'''
class Building:
    Location = tuple()
    Name:str = ""
    Function:set[str] = set()
    def __init__(self,Location,Function,Name):
        self.Location = Location
        self.Name = Name
        self.Function = Function
    
