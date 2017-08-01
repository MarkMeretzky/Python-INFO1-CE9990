"""
graphpaper.py

This function draws graph paper.  The right and bottom edges are left ragged.
"""

def draw(rowsOfBoxes, columnsOfBoxes, rowsOfSpaces, columnsOfSpaces):
    if not isinstance(rowsOfBoxes, int):
        raise TypeError("rowsOfBoxes must be int, not "
            + str(type(rowsOfBoxes)))

    if rowsOfBoxes < 1:
        raise ValueError("rowsOfBoxes must be >= 1, not " + str(rowsOfBoxes))

    if not isinstance(columnsOfBoxes, int):
        raise TypeError("columnsOfBoxes must be int, not "
            + str(type(columnsOfBoxes)))

    if columnsOfBoxes < 1:
        raise ValueError("columnsOfBoxes must be >= 1, not "
            + str(columnsOfBoxes))

    if not isinstance(rowsOfSpaces, int):
        raise TypeError("rowsOfSpaces must be int, not "
            + str(type(rowsOfSpaces)))

    if rowsOfSpaces < 1:
        raise ValueError("rowsOfSpaces must be >= 1, not " + str(rowsOfSpaces))

    if not isinstance(columnsOfSpaces, int):
        raise TypeError("columnsOfSpaces must be int, not "
            + str(type(columnsOfSpaces)))

    if columnsOfSpaces < 1:
        raise ValueError("columnsOfSpaces must be >= 1, not "
            + str(columnsOfSpaces))

    top = "+" + columnsOfSpaces * "-"
    mid = "|" + columnsOfSpaces * " "

    tops = columnsOfBoxes * top + "\n"
    mids = columnsOfBoxes * mid + "\n"

    row = tops + rowsOfSpaces * mids;
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
