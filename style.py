from typing import List, Mapping
# The style component adds the ability to style your graphs!

def add_color_to_link(data: str, color: str) -> str:
    """Adds the style you want to the relationship string"""
    data += f" [fillcolor = {color}]"
    return data

def add_linestyle(data: str, linestyle: str) -> str:
    """Adds a line style to the link"""
    data += f" [linestyle = {linestyle}]"
    return data

def multistyle(data: str, style: Mapping[str, str]) -> str:
    """Add multiple styles to the link"""
    data += " ["
    for k in style.keys():
        data += f"{k} = {style[k]};"
    data += "]"
    return data
