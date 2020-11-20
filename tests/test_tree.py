#!/usr/bin/env python3
from pygviz.tree import Tree
import pytest

# FIXME
def test_add_one_layer():
    mock_tree = Tree("George")
    mock_tree.add_layer(["Mathilda", "Ryan"])

    assert len(mock_tree.layers) == 1

    assert mock_tree.dict() == {
        "root": "George",
        "layer_0": ["Mathilda", "Ryan"],
    }

def test_add_two_layers():
    mock_tree = Tree("George")
    mock_tree.add_layer(["Mathilda", "Ryan"])

    # Add a second layer
    mock_tree.add_layer(
        [
            ["Tom", "Gene"],
            ["Ryan II", "Gerald"],
        ]
    )

    assert len(mock_tree.layers) == 2

    assert mock_tree.dict() == {
        "root": "George",
        "layer_0": ["Mathilda", "Ryan"],
        "layer_1": [["Tom", "Gene"], ["Ryan II", "Gerald"]]
    }

def test_add_bad_layers():
    """Add a layer with 3 elements where there should be only 2"""
    mock_tree = Tree("George")
    mock_tree.add_layer(["Mathilda", "Ryan"])

    # Add a second layer
    with pytest.raises(AssertionError):
        mock_tree.add_layer(
            [
                ["Tom", "Gene"],
                ["Ryan II", "Gerald"],
                ["Ryan III", "Gerald II"],
            ]
        )

def test_empty_tree_digraph():
    mock_tree = Tree("George")
    assert mock_tree.generate() == "digraph{\n}"

def test_empty_tree_graph():
    mock_tree = Tree("George")
    assert mock_tree.generate(False) == "graph{\n}"

def test_show():
    mock_tree = Tree("George")
    mock_tree.add_layer(["Mathilda", "Ryan"])

    print()
    mock_tree.show()
