from typing import List, Mapping
from pygviz.utils import make_image

# Nets connect things bidirectionally (two way street between them)

def make_links(data: Mapping[str, str]) -> List[str]:
    res = []
    for k in data.keys():
        for v in data[k]:
            res.append(f"{k} -- {v}")
    return res

def make_graph(data: List[str]) -> str:
    s = "graph{\n"
    for l in data:
        s += f"{l}\n"
    s += "}"
    return s

def make_net(data: Mapping[str, str], filename: str, ext: str="png"):
    relationships = make_links(data)
    final_graph = make_graph(relationships)
    make_image(final_graph, ext, filename)
