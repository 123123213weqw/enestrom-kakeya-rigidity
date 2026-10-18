# arXiv submission metadata

Copy-paste these into the arXiv form. Everything here matches `paper/main.tex`.

## Title

```
When is the Enestrom-Kakeya annulus sharp? Exact equality cases and a defect identity
```

(Use `Eneström` with the umlaut if the form accepts Unicode; otherwise `Enestrom`.)

## Authors

```
wangyue
```

## Primary category

```
math.CV   (Complex Variables)
```

## Cross-list

```
math.CA   (Classical Analysis and ODEs)
```

## MSC classification

```
30C15 (primary), 26C10, 30C10
```

## Comments

```
8 pages, 1 table. Verification scripts: https://github.com/123123213weqw/enestrom-kakeya-rigidity
```

## Abstract (plain text, no LaTeX)

```
Let p(z) = sum_{k=0}^{n} a_k z^k with a_k > 0, and put A = max_k a_k/a_{k+1},
a = min_k a_k/a_{k+1}. The Enestrom-Kakeya theorem places all zeros of p in the
annulus a <= |z| <= A. We determine exactly when this annulus is sharp, that is,
when a zero actually lies on a boundary circle. In the standard rescaling
b_k = a_k A^k that makes the coefficient sequence nondecreasing, a zero on the unit
circle exists if and only if b is constant on consecutive blocks of some common
length d >= 2 dividing n+1; equivalently, if and only if
q(u) = (1 + u + ... + u^{d-1}) G(u^d) for such a d. Three consequences are that
every boundary zero is a root of unity of order dividing n+1, that for n+1 prime
the outer circle is attained only by geometric polynomials, and that a simple
arithmetic condition on the set of indices where the maximal ratio is not attained
rules out boundary zeros. The proof is a rigidity argument for equality in the
triangle inequality. It is complemented by an exact defect identity and by a
worked perturbation showing that the extremal rate in the family
1 + z + ... + z^{n-1} + gamma z^n is 2 sin^2(pi/(n+1)) (gamma-1)/(n+1), which is
Theta((gamma-1)/n^3). All statements are checked computationally, over 6182
coefficient sequences with no counterexample.
```

## Before submitting — checklist

- [ ] **Endorsement.** A first submission in `math.CV` normally needs an endorsement
      (or a prior submission in a related category). Check
      <https://arxiv.org/auth/need-endorsement> while logged in.
- [ ] **Licence.** The repo uses MIT (code) + CC BY 4.0 (manuscript); arXiv asks for a
      separate licence selection at submission time.
- [ ] **Novelty.** The rigidity statement may be folklore in the polynomial-inequality
      literature; it is not claimed as certainly new. Consider a quick MathSciNet /
      zbMATH search on "Enestrom-Kakeya" + "equality" or + "sharp" before submitting,
      and cite whatever is closest.
- [ ] **Referee risk.** The two open problems in §6 are deliberately left open; a referee
      may ask for the quantitative version. That is the natural follow-up, not a defect.
