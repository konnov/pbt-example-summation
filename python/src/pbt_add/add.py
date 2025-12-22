"""Addition functions."""


def add_is_always_zero(_a: int, _b: int) -> int:
    """Trivial addition, if we only have one element zero."""
    return 0

def add(a: int, b: int) -> int:
    return a + b


def add32(a: int, b: int) -> int:
    return (a + b) % (2**32)

def add64(a: int, b: int) -> int:
    return (a + b) % (2**64)

def add256(a: int, b: int) -> int:
    return (a + b) % (2**256)
