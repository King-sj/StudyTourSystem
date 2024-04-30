import sys
sys.path.append(".\\server")
from src.Recommend import *
from src.DataType import *

def test_sort_up():
    test = [Building((0,0),set(),"d",0),Building((0,0),set(),"v",1),Building((0,0),set(),"b",2),Building((0,0),set(),"a",3)]
    expected_result = [Building((0,0),set(),"a",3),Building((0,0),set(),"b",2),Building((0,0),set(),"d",0),Building((0,0),set(),"v",1)]
    result = sort(test,"building_name")
    for x in range(0,4):
        assert result[x].building_name == expected_result[x].building_name

