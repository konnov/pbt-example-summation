"""Property-based tests for addition."""

from hypothesis import given, settings
from hypothesis import strategies as st

from pbt_add import add, add_is_always_zero, add32, add64, add256


@given(st.integers())
def test_identity_zero(a):
    """Test identity property: a + 0 = a."""
    assert add(a, 0) == a
    assert add(0, a) == a


@given(st.integers(), st.integers())
def test_commutativity_zero(a, b):
    """Test commutativity property: a + b = b + a."""
    assert add(a, b) == add(b, a)


@given(st.integers(), st.integers(), st.integers())
def test_associativity_zero(a, b, c):
    """Test associativity property: (a + b) + c = a + (b + c)."""
    assert add(add(a, b), c) == add(a, add(b, c))

# Tests for add_is_always_zero

@given(st.integers())
def test_identity(a):
    """Test identity property: a + 0 = a."""
    assert add_is_always_zero(a, 0) == a
    assert add_is_always_zero(0, a) == a


@given(st.integers(), st.integers())
def test_commutativity(a, b):
    """Test commutativity property: a + b = b + a."""
    assert add_is_always_zero(a, b) == add(b, a)


@given(st.integers(), st.integers(), st.integers())
def test_associativity(a, b, c):
    """Test associativity property: (a + b) + c = a + (b + c)."""
    assert add_is_always_zero(add(a, b), c) == add(a, add(b, c))

# Tests for add32 (32-bit natural numbers with wrapping)

@given(st.integers(min_value=0, max_value=2**32 - 1))
def test_add32_identity(a):
    """Test identity property for add32: a + 0 = a."""
    assert add32(a, 0) == a
    assert add32(0, a) == a


@given(st.integers(min_value=0, max_value=2**32 - 1), st.integers(min_value=0, max_value=2**32 - 1))
def test_add32_commutativity(a, b):
    """Test commutativity property for add32: a + b = b + a."""
    assert add32(a, b) == add32(b, a)


@given(
    st.integers(min_value=0, max_value=2**32 - 1),
    st.integers(min_value=0, max_value=2**32 - 1),
    st.integers(min_value=0, max_value=2**32 - 1)
)
def test_add32_associativity(a, b, c):
    """Test associativity property for add32: (a + b) + c = a + (b + c)."""
    assert add32(add32(a, b), c) == add32(a, add32(b, c))


@given(st.integers(min_value=0, max_value=2**32 - 1), st.integers(min_value=0, max_value=2**32 - 1))
def test_add32_wrapping(a, b):
    """Test that add32 wraps around correctly when exceeding 32-bit range."""
    result = add32(a, b)
    # Result must be in valid 32-bit range
    assert 0 <= result < 2**32
    # Result must match modulo arithmetic
    assert result == (a + b) % (2**32)


@given(st.integers(min_value=0, max_value=2**32 - 1))
def test_add32_max_plus_one_wraps_to_zero(a):
    """Test that adding to max value wraps correctly."""
    max_val = 2**32 - 1
    if a == 0:
        # max + 1 should wrap to 0
        assert add32(max_val, 1) == 0
    # For any a, (max - a + 1) + a should wrap to 0
    complement = max_val - a + 1
    if complement < 2**32:
        assert add32(a, complement) == 0

# Tests for add32 (32-bit natural numbers with wrapping)

@given(st.integers(0))
def test_add32_unbounded_inputs_identity(a):
    """Test identity property for add32: a + 0 = a."""
    assert add32(a, 0) == a
    assert add32(0, a) == a

@given(st.integers(0), st.integers(0))
def test_add32_unbounded_inputs_commutativity(a, b):
    """Test commutativity property for add32: a + b = b + a."""
    assert add32(a, b) == add32(b, a)


@given(
    st.integers(0),
    st.integers(0),
    st.integers(0)
)
def test_add32_unbounded_inputs_associativity(a, b, c):
    """Test associativity property for add32: (a + b) + c = a + (b + c)."""
    assert add32(add32(a, b), c) == add32(a, add32(b, c))

# Tests for add64 (64-bit natural numbers with wrapping)

@given(st.integers(0))
def test_add64_unbounded_inputs_identity(a):
    """Test identity property for add64: a + 0 = a."""
    assert add64(a, 0) == a
    assert add64(0, a) == a

@given(st.integers(0), st.integers(0))
def test_add64_unbounded_inputs_commutativity(a, b):
    """Test commutativity property for add64: a + b = b + a."""
    assert add64(a, b) == add64(b, a)

@given(
    st.integers(0),
    st.integers(0),
    st.integers(0)
)
def test_add64_unbounded_inputs_associativity(a, b, c):
    """Test associativity property for add64: (a + b) + c = a + (b + c)."""
    assert add64(add64(a, b), c) == add64(a, add64(b, c))

# Tests for add256 (256-bit natural numbers with wrapping)

@given(st.integers(0))
@settings(max_examples=100000)
def test_add256_unbounded_inputs_identity(a):
    """Test identity property for add256: a + 0 = a."""
    assert add256(a, 0) == a
    assert add256(0, a) == a

@given(st.integers(0), st.integers(0))
@settings(max_examples=100000)
def test_add256_unbounded_inputs_commutativity(a, b):
    """Test commutativity property for add256: a + b = b + a."""
    assert add256(a, b) == add256(b, a)


@given(
    st.integers(0),
    st.integers(0),
    st.integers(0)
)
@settings(max_examples=100000)
def test_add256_unbounded_inputs_associativity(a, b, c):
    """Test associativity property for add256: (a + b) + c = a + (b + c)."""
    assert add256(add256(a, b), c) == add256(a, add256(b, c))