"""Core checks for the Enestrom-Kakeya rigidity note.

Everything is exact over Fraction except root finding, which uses float64.
"""
from fractions import Fraction
import itertools, random
import numpy as np

# ---------- polynomial utilities (coeffs low->high) ----------
def poly_mul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out

def poly_trim(a):
    a = [c for c in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def poly_divmod(a, b):
    a = poly_trim([Fraction(c) for c in a]); b = poly_trim([Fraction(c) for c in b])
    if b == [Fraction(0)]:
        raise ZeroDivisionError
    q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    r = a[:]
    while len(poly_trim(r)) >= len(b) and poly_trim(r) != [Fraction(0)]:
        r = poly_trim(r)
        k = len(r) - len(b)
        c = r[-1] / b[-1]
        q[k] += c
        for i, bc in enumerate(b):
            r[k + i] -= c * bc
        r = poly_trim(r)
    return poly_trim(q), poly_trim(r)

def poly_gcd(a, b):
    a = poly_trim([Fraction(c) for c in a]); b = poly_trim([Fraction(c) for c in b])
    while b != [Fraction(0)]:
        _, r = poly_divmod(a, b)
        a, b = b, r
    # monic
    return [c / a[-1] for c in a]

def roots(coeffs):
    c = np.array([float(x) for x in coeffs], dtype=float)
    c = np.trim_zeros(c, 'b')
    if len(c) < 2:
        return np.array([])
    return np.roots(c[::-1])

def reversal(b):
    return list(b)[::-1]

def refl(b):
    """q*(u) = u^n q(1/u) for real coefficients."""
    return reversal(b)

def has_unit_circle_root(b, tol=1e-7):
    """True iff some zero of sum b_k u^k lies on |u| = 1.

    Exact exclusion: gcd(q, q*) = 1 => no zero on the circle.
    Otherwise inspect the common factor numerically.
    """
    b = [Fraction(c) for c in b]
    g = poly_gcd(b, refl(b))
    if len(g) <= 1:
        return False, 0.0
    r = roots(g)
    if len(r) == 0:
        return False, 0.0
    dev = float(np.min(np.abs(np.abs(r) - 1.0)))
    return dev < tol, dev

def block_structure(b):
    """n+1 = m*d with d>=2 and b constant on consecutive blocks of length d."""
    n1 = len(b)
    hits = []
    for d in range(2, n1 + 1):
        if n1 % d:
            continue
        ok = all(b[j*d + r] == b[j*d] for j in range(n1 // d) for r in range(d) if j*d + r < n1)
        if ok:
            hits.append(d)
    return hits

def nondecreasing_seqs(n1, hi):
    for c in itertools.combinations_with_replacement(range(1, hi + 1), n1):
        yield list(c)

# ---------- Experiment 1: theorem 1 (EK) ----------
def check_ek(trials=4000, seed=0):
    rng = random.Random(seed)
    worst = 0.0
    for _ in range(trials):
        n = rng.randint(1, 9)
        a = [Fraction(rng.randint(1, 40), rng.randint(1, 40)) for _ in range(n + 1)]
        r = [a[k] / a[k + 1] for k in range(n)]
        lo, hi = min(r), max(r)
        for z in roots(a):
            m = abs(z)
            if m > float(hi) + 1e-9:
                worst = max(worst, m - float(hi))
            if m < float(lo) - 1e-9:
                worst = max(worst, float(lo) - m)
    return worst

# ---------- Experiment 2: theorem 2 (rigidity) ----------
def check_rigidity(nmax=8, hi=4):
    bad = []
    total = 0
    for n1 in range(2, nmax + 2):     # number of coefficients
        for b in nondecreasing_seqs(n1, hi):
            total += 1
            hit, dev = has_unit_circle_root(b)
            blocks = block_structure(b)
            if hit != bool(blocks):
                bad.append((b, hit, dev, blocks))
    return total, bad

# ---------- Experiment 3: balance identity ----------
def check_balance(trials=2000, seed=1):
    """b_n[1 - R^{n+1} cos((n+1)theta)] == sum_{k in I} Delta_k [1 - R^k cos(k theta)]"""
    rng = random.Random(seed)
    worst = 0.0
    for _ in range(trials):
        n = rng.randint(1, 8)
        b = sorted(Fraction(rng.randint(1, 20), rng.randint(1, 5)) for _ in range(n + 1))
        for z in roots(b):
            R = abs(z); th = float(np.angle(z))
            lhs = float(b[-1]) * (1 - R**(n + 1) * np.cos((n + 1) * th))
            rhs = 0.0
            for k in range(1, n + 1):
                dk = float(b[k] - b[k - 1])
                if dk:
                    rhs += dk * (1 - R**k * np.cos(k * th))
            worst = max(worst, abs(lhs - rhs) / (1 + abs(lhs) + abs(rhs)))
    return worst

if __name__ == "__main__":
    print("EK violation (max excess outside annulus):", check_ek())
    tot, bad = check_rigidity()
    print("rigidity: sequences tested =", tot, " counterexamples =", len(bad))
    for rec in bad[:5]:
        print("   BAD:", rec)
    print("balance identity max relative error:", check_balance())
