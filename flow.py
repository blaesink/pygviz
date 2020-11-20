from typing import List


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
