#!/usr/bin/env python3

from pygviz.flow import Flow, graph, make_relationships
import pytest
# from pygviz.utils import filename

def setUp():
    data = {
        "Tom": ["Mathilda", "Ryan"],
        "Mathilda": ["Gregory"]
    }
    mock_flow = Flow(data)

    return mock_flow

def test_simple_flow():
    mock_flow = setUp()

    assert mock_flow.make_relationships() == [
        "Tom -> Mathilda",
        "Tom -> Ryan",
        "Mathilda -> Gregory"
    ]

def test_oop_graph():
    # Yes, that string is gross. No, I'm not going to change it.
    mock_flow = setUp()

    return_string = "digraph{\nTom -> Mathilda\nTom -> Ryan\nMathilda -> Gregory\n}"
    assert mock_flow.graph() == return_string

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

    assert graph(data) == expected
