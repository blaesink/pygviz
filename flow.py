from typing import List


class Flow:
    """A flow is a dictionary that parses everything and makes a chart from there."""
    def __init__(self, data: dict={}):
        self.data = data

    def make_relationships(self):
        rels = []
        for k in self.data.keys():
            for v in self.data[k]:
                rels.append(f"{k} -> {v}")
        return rels

    def graph(self):
        rels = self.make_relationships()
        s = "digraph{\n"
        for r in rels:
            s += r + "\n"
        s += "}"
        return s


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
