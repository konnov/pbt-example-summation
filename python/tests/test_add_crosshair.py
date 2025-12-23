"""CrossHair-only tests for addition."""

from crosshair.core_and_libs import standalone_statespace
from pbt_add import add256


def check_add256_identity(a: int) -> bool:
    """
    Check identity property for add256: a + 0 = a.
    
    pre: a >= 0
    post: _
    """
    return add256(a, 0) == a and add256(0, a) == a


def check_add256_commutativity(a: int, b: int) -> bool:
    """
    Check commutativity property for add256: a + b = b + a.
    
    pre: a >= 0 and b >= 0
    post: _
    """
    return add256(a, b) == add256(b, a)


def check_add256_associativity(a: int, b: int, c: int) -> bool:
    """
    Check associativity property for add256: (a + b) + c = a + (b + c).
    
    pre: a >= 0 and b >= 0 and c >= 0
    post: _
    """
    return add256(add256(a, b), c) == add256(a, add256(b, c))
