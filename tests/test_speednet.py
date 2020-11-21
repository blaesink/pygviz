from pygviz.speednet import *

def test_speednet():
    test_data = {
        "data": ["Tom", "Jerry", "Mike", "Jim"],
        "rels": [(0,1,3), (2,0,1), (3,2,1)]
    }

    expected = [
        "Tom -- Jerry",
        "Tom -- Jim",
        "Mike -- Tom",
        "Mike -- Jerry",
        "Jim -- Mike",
        "Jim -- Jerry"
    ]

    assert link_relationships(test_data) == expected

def test_graph():
    test_data = [
        "Tom -- Jerry",
        "Tom -- Jim",
        "Mike -- Tom",
        "Mike -- Jerry",
        "Jim -- Mike",
        "Jim -- Jerry"
    ]

    expected = "graph{\nTom -- Jerry\nTom -- Jim\nMike -- Tom\nMike -- Jerry\nJim -- Mike\nJim -- Jerry\n}"

    assert make_graph(test_data) == expected
