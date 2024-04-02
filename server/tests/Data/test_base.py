import sys
sys.path.append('D:\\学习\\大二\\数据结构课程设计\\游学系统\\StudyTourSystem\\server')

from src.Recommend.Recommend import *
from src.Data.DataType import *

def test_sort():
    test = [Building((0,0),set(),"d"),Building((0,0),set(),"v"),Building((0,0),set(),"b"),Building((0,0),set(),"a")]
    expected_result = [Building((0,0),set(),"a"),Building((0,0),set(),"b"),Building((0,0),set(),"d"),Building((0,0),set(),"v")]
    result = sort(test,"building_name")
    for x in range(0,4):
        assert result[x].building_name == expected_result[x].building_name