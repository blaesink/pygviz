import os


def generate_dot_file(filestr: str, filename: str):
    with open(f"{filename}.dot", "w") as f:
        f.write(filestr)

def dot_to_img(ext: str, dotfile: str, ofile: str) -> bool:
    try:
        os.system(f"dot -T{ext} {dotfile}.dot -o {ofile}.{ext}")
        return True
    except:
        raise IOError

def make_image(filestr: str, ext: str, filename: str):
    """Make the image"""
    generate_dot_file(filestr, filename)
    dot_to_img(ext, filename, filename)
