#!/usr/bin/env python3
from pygviz.tree import Tree


def test_add_layers():
    mock_tree = Tree("George")
    mock_tree.add_layer(["Mathilda", "Ryan"])

    assert len(mock_tree.layers) == 1

def test_tree_dict():
    mock_tree = Tree("George")
    mock_tree.add_layer(["Mathilda", "Ryan"])

    assert mock_tree.dict() == {
        "top": "George",
        "layer_0": ["Mathilda", "Ryan"],
    }
