import os

class Node:
    def __init__(self,name):
        self.name = name
        self.targets = []

    def connect(self,target,style={}):
        res = {
            "target":target.name,
        }
        for k in style:
            res[k] = style[k]
        self.targets.append(res)

    def mconnect(self,*targets:list,style={}):
        for t in targets:
            self.connect(t,style)

def rconnect(target,*args,**kwargs):
    """Connects *args to target instead of having to do multiple connects"""
    for a in args:
        a.connect(target,**kwargs)

def recip(a,b,style={}):
    """Connect two nodes to each other"""
    a.connect(b,style)
    b.connect(a,style)

def graph(nodes:list,styles:list=[]) -> str:
    s = "graph{\n"
    for n in nodes:
        for t in n.targets:
            style = ','.join([f"{x}=\"{t[x]}\"" for x in t.keys() if x != "target"])
            s += f"\t\"{n.name}\" -- \"{t['target']}\"[{style}]\n"
    s += '}'
    return s

def digraph(nodes:list,styles:list=[]) -> str:
    s = "digraph{\n"
    for m in styles:
        if not isinstance(m,str):
            return 0
        s += f"\n{m}"
    for n in nodes:
        for t in n.targets:
            style = ','.join([f"{x}=\"{t[x]}\"" for x in t.keys() if x != "target"])
            s += f"\t\"{n.name}\" -> \"{t['target']}\"[{style}]\n"
    s += '}'
    return s

def generate(graph: str,filename,backend="dot",ext="png"):
    with open(f"{filename}.dot",'w') as f:
        f.write(graph)
    os.system(f"{backend} -T{ext} {filename}.dot -o {filename}.{ext}")

# FIXME TODO XXX
def stylestr(d:dict={},nodes=[]):
    s = "\tnode["
    s += ','.join([f"{x}=\"{d[x]}\"" for x in d.keys() if x != 'target'])
    s += ']\n\t'
    if len(nodes) > 1:
        s += "\"" + nodes[0].name + "\""
        for n in nodes[1:]:
            s += ',' + "\"" + n.name + "\""
    #elif len(nodes) == 0:
    #    s += "\"" + nodes[0].name + "\""
    s += ';\n'
    return s
