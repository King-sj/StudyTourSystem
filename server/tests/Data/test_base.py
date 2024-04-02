import sys
sys.path.append("..\\..")

from src.Recommend import *
from src.DataType import *

def test_sort_up():
    test = [Building((0,0),set(),"d"),Building((0,0),set(),"v"),Building((0,0),set(),"b"),Building((0,0),set(),"a")]
    expected_result = [Building((0,0),set(),"a"),Building((0,0),set(),"b"),Building((0,0),set(),"d"),Building((0,0),set(),"v")]
    result = sort(test,"building_name")
    for x in range(0,4):
        assert result[x].building_name == expected_result[x].building_name

def test_sort_down():
    test = [Building((0,0),set(),"d"),Building((0,0),set(),"v"),Building((0,0),set(),"b"),Building((0,0),set(),"a")]
    expected_result = [Building((0,0),set(),"v"),Building((0,0),set(),"d"),Building((0,0),set(),"b"),Building((0,0),set(),"a")]
    result = sort(test,"building_name",1)
    for x in range(0,4):
        assert result[x].building_name == expected_result[x].building_name