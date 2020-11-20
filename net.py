from typing import List, Mapping

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
    s+= "}"
    return s
