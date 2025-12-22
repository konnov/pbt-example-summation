"""Addition functions."""


def add(a: int, b: int) -> int:
    return a + b


def add32(a: int, b: int) -> int:
    return (a + b) % (2**32)

def add64(a: int, b: int) -> int:
    return (a + b) % (2**64)

def add256(a: int, b: int) -> int:
    return (a + b) % (2**256)
