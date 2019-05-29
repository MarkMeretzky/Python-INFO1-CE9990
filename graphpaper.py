"""
graphpaper.py

Define a function that takes arguments and returns a sheet of graph paper.
"""

def draw(rowsOfBoxes, columnsOfBoxes, rowsOfSpaces, columnsOfSpaces):
    """
    Return a string containing a sheet of graph paper with the specified
    dimensions.  The right and bottom edges are left ragged.
    """
    if not isinstance(rowsOfBoxes, int):
        raise TypeError(f"rowsOfBoxes must be int, not {type(rowsOfBoxes)}")

    if rowsOfBoxes < 1:
        raise ValueError(f"rowsOfBoxes must be >= 1, not {rowsOfBoxes}")

    if not isinstance(columnsOfBoxes, int):
        raise TypeError(f"columnsOfBoxes must be int, not {type(columnsOfBoxes)}")

    if columnsOfBoxes < 1:
        raise ValueError(f"columnsOfBoxes must be >= 1, not {columnsOfBoxes}")

    if not isinstance(rowsOfSpaces, int):
        raise TypeError(f"rowsOfSpaces must be int, not {type(rowsOfSpaces)}")

    if rowsOfSpaces < 1:
        raise ValueError(f"rowsOfSpaces must be >= 1, not {rowsOfSpaces}")

    if not isinstance(columnsOfSpaces, int):
        raise TypeError(f"columnsOfSpaces must be int, not {type(columnsOfSpaces)}")

    if columnsOfSpaces < 1:
        raise ValueError(f"columnsOfSpaces must be >= 1, not {columnsOfSpaces}")

    top = "+" + columnsOfSpaces * "-"
    mid = "|" + columnsOfSpaces * " "

    tops = columnsOfBoxes * top + "\n"
    mids = columnsOfBoxes * mid + "\n"

    row = tops + rowsOfSpaces * mids
    return rowsOfBoxes * row


if __name__ == "__main__":
    import sys
    rowsOfBoxes     = int(input("How many rows of boxes? "))
    columnsOfBoxes  = int(input("How many columns of boxes? "))
    rowsOfSpaces    = int(input("How many rows of spaces in each box (e.g., 1)? "))
    columnsOfSpaces = int(input("How many columns of spaces in each box (e.g., 3)? "))
    s = draw(rowsOfBoxes, columnsOfBoxes, rowsOfSpaces, columnsOfSpaces)
    print(s)
    sys.exit(0)
