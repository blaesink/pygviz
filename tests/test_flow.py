#!/usr/bin/env python3

from pygviz.flow import make_graph, make_relationships
import pytest


def test_func_rels():
    data = {
            "Tom": ["Mathilda", "Ryan"],
            "Mathilda": ["Gregory"]
    }
    assert make_relationships(data) == [
        "Tom -> Mathilda",
        "Tom -> Ryan",
        "Mathilda -> Gregory"
    ]

def test_func_graph():
    data = [
        "Tom -> Mathilda",
        "Tom -> Ryan",
        "Mathilda -> Gregory"
    ]
    expected = "digraph{\nTom -> Mathilda\nTom -> Ryan\nMathilda -> Gregory\n}"

    assert make_graph(data) == expected
