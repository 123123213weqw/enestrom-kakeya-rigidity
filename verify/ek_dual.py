"""Third battery: dual bound, both-bounds-attained, and the dodge of degenerate cases."""
import numpy as np
from fractions import Fraction
from ek_core import roots, has_unit_circle_root, block_structure, nondecreasing_seqs


def ratios(b):
    return [b[k] / b[k + 1] for k in range(len(b) - 1)]


def attained_outer(b):
    A = max(ratios(b))
    return any(abs(abs(z) - float(A)) < 1e-7 for z in roots(b))


def attained_inner(b):
    a = min(ratios(b))
    return any(abs(abs(z) - float(a)) < 1e-7 for z in roots(b))


if __name__ == "__main__":
    both = []
    outer_only = 0
    for n1 in range(2, 9):
        for b in nondecreasing_seqs(n1, 4):
            o, i = attained_outer(b), attained_inner(b)
            if o and i:
                both.append(b)
            elif o:
                outer_only += 1
    print("outer attained only:", outer_only)
    print("both attained:", len(both))
    const = sum(1 for b in both if len(set(b)) == 1)
    print("  of which constant:", const)
    for b in both[:12]:
        print("   ", b)
