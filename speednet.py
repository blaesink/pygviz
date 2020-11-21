from typing import Mapping, List
from pygviz.utils import make_image

# A speednet is a faster way to link everything together
# than typing out everything.

# Example Data:
# {
#     "data": ["Tom", "Jerry", "Mike", "Jim"],
#     "rels": [(0,1,3), (2,0,1), (3,2,1)]
# }
# The first index in the tuple is the *root*.
# The *root* will connect to everything after it, creating the expected linkage
# 0 -- 1
# 0 -- 3
#
# The Goal is to set everything ONCE, then build off of the indices.
# A speednet should much faster in theory for small to
# medium-ish sized structures, where you can keep track of the indices and
# write through it quickly.

def link_relationships(data: dict):
    res = []
    for t in data.get("rels"):
        for i in t[1:]:
            root = data.get("data")[t[0]]
            link = data.get("data")[i]
            res.append(f"{root} -- {link}")
    return res

def make_graph(data: List[str]) -> str:
    s = "graph{\n"
    for l in data:
        s += (l + "\n")
    s += "}"
    return s

def make_speednet(data: Mapping[str, str], filename: str, ext:str="ext"):
    rels = make_relationships(data)
    final_graph = make_graph(rels)
    make_image(final_graph, ext, filename)
