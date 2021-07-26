from typing import List


def join(xs: List[int], delimiter: str) -> str:
    """Produce a string where subsequent items are separated by delimiter"""
    generated_string: str = ""

    for item in xs:
        if generated_string == "":
            # don’t put delimiter before first item
            generated_string = str(item)
        else:
            generated_string += delimiter + str(item)

    return generated_string
