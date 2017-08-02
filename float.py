"""
float.py

Create an iterable class named float.range.  Use it like this:

import float

for f in float.range(0.0, 1.0, 10)   #a sequence of 11 floats
    print(f)

The output is

0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
"""

class range(object):
    "A sequence of equally spaced floats."
    
    def __init__(self, start, end, n):
        "Create an object that is a sequence of n+1 values of type float."
        assert isinstance(n, int)
        self.start = start
        self.end = end
        self.n = n

    def __iter__(self):
        "Create and return an iterator for looping through the sequence."
        return Iterator(self)


class Iterator(object):
    "The iterator for looping through a sequence of floats."

    def __init__(self, r):
        """
        Create an iterator containing a reference to the sequence through
        which it will loop.
        """
        assert isinstance(r, range)   #r is the reference
        self.r = r
        self.i = 0

    def __iter__(self):
        "See 'iterator protocol' in Python Library documentation section 4.5."
        return self

    def __next__(self):
        "Return the next float, if there is one, in the sequence of floats."
        if self.i >= self.r.n + 1:
            raise StopIteration
        result = self.r.start + (self.r.end - self.r.start) * self.i / self.r.n
        self.i += 1
        return result


if __name__ == "__main__":
    import sys
    for f in range(0.0, 1.0, 10):
        print(f)
    sys.exit(0)
