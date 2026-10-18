"""Second battery of checks: bigger sweep, root-of-unity corollary, sharpness rate."""
import math
import numpy as np
from ek_core import roots, has_unit_circle_root, block_structure, nondecreasing_seqs


def sweep(nmax, hi):
    tot = hit = 0
    bad = []
    for n1 in range(2, nmax + 2):
        for b in nondecreasing_seqs(n1, hi):
            tot += 1
            h, dev = has_unit_circle_root(b)
            bl = block_structure(b)
            if h:
                hit += 1
            if h != bool(bl):
                bad.append((b, h, dev, bl))
    return tot, hit, bad


def check_root_of_unity(nmax, hi):
    """Every zero on |u| = 1 should satisfy u^(n+1) = 1."""
    tot = 0
    bad = []
    for n1 in range(2, nmax + 2):
        for b in nondecreasing_seqs(n1, hi):
            for r in roots(b):
                if abs(abs(r) - 1) < 1e-7:
                    tot += 1
                    if abs(r ** n1 - 1) > 1e-6:
                        bad.append((b, r))
    return tot, bad


def gamma_max_root(n, g):
    return float(max(abs(r) for r in roots([1.0] * n + [g])))


def predicted(n, g):
    """d|z|/dgamma = -2 sin^2(theta/2)/(n+1) at theta = 2 pi k/(n+1), worst k = 1."""
    return 1.0 - 2.0 * math.sin(math.pi / (n + 1)) ** 2 / (n + 1) * (g - 1.0)


if __name__ == "__main__":
    tot, hit, bad = sweep(11, 5)
    print(f"sweep n+1<=12, values<=5 : {tot} sequences, {hit} attaining, {len(bad)} counterexamples")
    for r in bad[:5]:
        print("  BAD", r)

    t, b2 = check_root_of_unity(11, 5)
    print(f"zeros on |u|=1: {t} checked, {len(b2)} not an (n+1)-th root of unity")
    for r in b2[:5]:
        print("  BAD", r)

    print("\ngamma-family  p = 1+z+...+z^(n-1) + gamma z^n")
    print("   n  gamma        max|zero|      first-order pred   ratio")
    for n in (4, 9, 19):
        for g in (1.001, 1.01, 1.1):
            m = gamma_max_root(n, g)
            p = predicted(n, g)
            print(f"  {n:3d} {g:<8}   {m:.12f}   {p:.12f}   {(1-m)/(1-p):.4f}")
