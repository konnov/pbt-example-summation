----------------------------------- MODULE Add --------------------------------
(*
 * A simple TLA+ specification of different kinds of addition.
 *
 * Igor Konnov, 2025
 *)
EXTENDS Integers

VARIABLE
    \* @type: Int;
    x,
    \* @type: Int;
    y,
    \* @type: Int;
    z

AddMath(a, b) == a + b

Add32(a, b) == (a + b) % (2^32)

Add64(a, b) == (a + b) % (2^64)

Add256(a, b) == (a + b) % (2^256)

InitMath ==
    /\ x \in Int
    /\ y \in Int
    /\ z \in Int

InitNat ==
    /\ x \in Nat
    /\ y \in Nat
    /\ z \in Nat

Init32 ==
    /\ x \in 0..(2^32 - 1)
    /\ y \in 0..(2^32 - 1)
    /\ z \in 0..(2^32 - 1)

Init64 ==
    /\ x \in 0..(2^64 - 1)
    /\ y \in 0..(2^64 - 1)
    /\ z \in 0..(2^64 - 1)

Init256 ==
    /\ x \in 0..(2^256 - 1)
    /\ y \in 0..(2^256 - 1)
    /\ z \in 0..(2^256 - 1)

Next == UNCHANGED <<x, y, z>>

Identity(F(_, _)) ==
    F(x, 0) = x

Commutativity(F(_, _)) ==
    F(x, y) = F(y, x)

Associativity(F(_, _)) ==
    F(F(x, y), z) = F(x, F(y, z))

Bounded(F(_, _), bitwidth) ==
    F(x, y) \in 0..(2^bitwidth - 1)

NoOverflow(F(_, _), bitwidth) ==
    x \in 0..(2^(bitwidth - 1) - 1) /\ y \in 0..(2^(bitwidth - 1) - 1) =>
        F(x, y) >= x /\ F(x, y) >= y

InvMath ==
    /\ Identity(AddMath)
    /\ Commutativity(AddMath)
    /\ Associativity(AddMath)

Inv32 ==
    /\ Identity(Add32)
    /\ Commutativity(Add32)
    /\ Associativity(Add32)
    /\ Bounded(Add32, 32)
    /\ NoOverflow(Add32, 32)

Inv64 ==
    /\ Identity(Add64)
    /\ Commutativity(Add64)
    /\ Associativity(Add64)
    /\ Bounded(Add64, 64)
    /\ NoOverflow(Add64, 64)

Inv256 ==
    /\ Identity(Add256)
    /\ Commutativity(Add256)
    /\ Associativity(Add256)
    /\ Bounded(Add256, 256)
    /\ NoOverflow(Add256, 256)

===============================================================================