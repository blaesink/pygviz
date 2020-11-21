from typing import List, Mapping
from pygviz.utils import make_image


def make_relationships(data: dict) -> List[str]:
    rels = []
    for k in data.keys():
        for v in data[k]:
            rels.append(f"{k} -> {v}")
    return rels

def graph(data: List[str]):
    s = "digraph{\n"
    for l in data:
        s += l + "\n"
    s += "}"
    return s

def make_flow(data: Mapping[str, str], filename: str, ext:str="ext"):
    rels = make_relationships(data)
    final_graph = graph(rels)
    make_image(final_graph, ext, filename)
