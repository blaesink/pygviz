from pygviz.net import *

def test_make_links():
    data = {
        "A": ["B", "C"],
        "B": ["C", "D"]
    }
    expected = [
        "A -- B",
        "A -- C",
        "B -- C",
        "B -- D"
    ]

    assert make_links(data) == expected

def test_make_graph():
    data = [
        "A -- B",
        "A -- C",
        "B -- C",
        "B -- D"
    ]
    expected = "graph{\nA -- B\nA -- C\nB -- C\nB -- D\n}"

    assert make_graph(data) == expected
