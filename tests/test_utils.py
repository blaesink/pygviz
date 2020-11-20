from pygviz.utils import generate_dot_file, dot_to_img
import os
import pytest


def cleanUp():
    os.system("rm *.dot *.png")

# TODO change this to just be an in-memory io.StringIO item later
# it will speed this up
def test_generate_dot_file():
    """Test generating a dot file"""
    file_string = "digraph{\nTom -> Mathilda\nTom -> Ryan\nMathilda -> Gregory\n}"

    generate_dot_file(filestr=file_string, filename="test")

    with open("test.dot", "r") as f:
        assert f.read() == file_string

def test_dot_to_img():
    file_string = "digraph{\nTom -> Mathilda\nTom -> Ryan\nMathilda -> Gregory\n}"
    generate_dot_file(filestr=file_string, filename="test")

    # Probably not the best way to test but it works.
    assert dot_to_img(ext="png", dotfile="test", ofile="test") == True
    cleanUp()

# def test_dot_to_img_fails():
#     file_string = "digraph{\nTom -> Mathilda\nTom -> Ryan\nMathilda -> Gregory\n}"
#     generate_dot_file(filestr=file_string, filename="test")
#
#     # Probably not the best way to test but it works.
#     with pytest.raises(IOError):
#         dot_to_img(ext="png", dotfile="test2", ofile="test")
#     cleanUp()
