from DataType import *

def make_comment(comment:Comment,Object):
    if not (isinstance(Object, Journal) or isinstance(Object, Area)):
        return
    if(isinstance(Object, Journal)):
        Object.journal_comments.append(comment)
    else:
        Object.comment_group.append(comment)