# When is the Eneström–Kakeya annulus sharp?

A short research note (**not peer reviewed**) on the exact equality case of the
Eneström–Kakeya theorem, plus the code that checks every claim in it.

> **Eneström–Kakeya.** If `p(z) = Σ aₖ zᵏ` has all `aₖ > 0`, then every zero lies in the
> annulus `min aₖ/aₖ₊₁ ≤ |z| ≤ max aₖ/aₖ₊₁`.

The classical statement says where the zeros *are*. This note asks a different question:
**for a given polynomial, is the annulus actually attained — does a zero lie exactly on a
boundary circle?** The answer turns out to be rigid.

---

## Result

Rescale to the extremal normalisation `bₖ = aₖ Aᵏ` with `A = max aₖ/aₖ₊₁`, so that
`b₀ ≤ b₁ ≤ … ≤ bₙ` and `p(z) = q(Az)`. Let `I = {k : bₖ > bₖ₋₁}` be the jump set — the
indices where the *maximal* ratio is *not* attained.

**Theorem (rigidity).** `q` has a zero on the unit circle **iff** `b` is constant on
consecutive blocks of some common length `d ≥ 2` dividing `n+1`. Equivalently,

```
q(u) = (1 + u + … + u^{d-1}) · Σⱼ cⱼ u^{jd},    0 < c₀ ≤ … ≤ c_{m-1},  m = (n+1)/d.
```

A boundary zero is therefore never an accident: it always comes from the cyclotomic factor
`1 + u + … + u^{d-1}`.

Three consequences:

| | statement |
|---|---|
| **Cor. 3.3** | every zero on `\|u\| = 1` is a root of unity of order dividing `n+1` |
| **Cor. 3.4** | if `n+1` is prime, the outer circle is attained **only** by geometric polynomials (`aₖ = cA^{-k}`, annulus collapses) |
| **Cor. 3.5** | if `I ≠ ∅` and `gcd(gcd I, n+1) = 1`, there is **no** zero on `\|z\| = A` |

Example: take `q(u) = 1 + u + 2u² + 2u³`. Then `I = {2}`, `gcd(2,4) = 2`, and indeed
`q = (1+u)(1+2u²)` has a zero at `u = -1`. Replace the last coefficient by `γ > 1` and the
zero disappears: `I = {3}`, `gcd(3,4) = 1`.

### Quantitative side

An exact **defect identity** holds at every zero `u`:

```
bₙ (1 − Re u^{n+1}) = Σₖ Δₖ (1 − Re u^{k}),      Δₖ = bₖ − bₖ₋₁
```

Its degenerate case is the rigidity theorem. It also quantifies how far zeros sit from the
circle. For the family `1 + z + … + z^{n−1} + γzⁿ` (which never attains the bound), the
maximal root modulus is

```
1 − 2 sin²(π/(n+1))/(n+1) · (γ−1) + O((γ−1)²)  =  1 − 2π²(γ−1)/(n+1)³ + …
```

so the bound is sharp but **fragile**: forcing a zero a distance `δ` inside needs
`γ − 1 ≍ n³δ`. The sharpness exponent in the degree is 3.

---

## Status, honestly

- This is a **note, not a published paper**. It has not been refereed.
- **Novelty is not established.** The rigidity characterisation may be folklore in the
  polynomial-inequality literature; I could not find it stated in this generality, so it is
  presented with a self-contained proof and an explicit verification instead. The literature
  contains many *generalizations* (quaternionic, octonionic, matrix) and *refinements* of
  Eneström–Kakeya, but those shrink the annulus under extra hypotheses rather than
  characterising exact attainment.
- Two questions are left **open** in the note (see §6): a quantitative rigidity theorem, and
  whether a non-degenerate annulus can be attained on both circles simultaneously (search
  found no counterexample).

## Verification

Everything is checked by `verify/`. The decision "does `q` have a zero on `|u| = 1`?" is
made **exactly** in rational arithmetic (a boundary zero forces
`gcd(q, q*) ≠ 1` for the reversed polynomial `q*`; when the gcd is 1 there is no boundary
zero and no floating point is involved).

```
sweep n+1 ≤ 12, coefficients ≤ 5 : 6182 sequences
                                    591 attaining, all block-structured
                                      0 counterexamples
zeros found on |u| = 1           :   1111, all satisfy u^{n+1} = 1
non-degenerate annuli (a < A)    :   6116, none attaining both circles
defect identity                  :   max relative error 1.2e-14  (2000 random polys, deg ≤ 8)
```

## Files

```
paper/main.tex      the note (amsart, ~8 pp)
paper/main.pdf      compiled version
verify/ek_core.py   exact gcd test, exhaustive sweep, balance identity
verify/ek_more.py   larger sweep, root-of-unity corollary, gamma-family rates
verify/ek_dual.py   inner/outer attainment, both-attained statistics
Makefile            make paper / make verify
```

## Build and reproduce

```bash
make paper     # tectonic -X compile paper/main.tex   (no TeX distribution needed)
make verify    # python3 checks, ~1 min
```

Requires `tectonic` and `python3` + `numpy`.

## Citation

```bibtex
@misc{wangyue2026ekrigidity,
  author = {wangyue},
  title  = {When is the Enestr{\"o}m--Kakeya annulus sharp? Exact equality cases
            and a defect identity},
  year   = {2026},
  note   = {Preprint, https://github.com/123123213weqw/enestrom-kakeya-rigidity}
}
```

Code: MIT. Manuscript text: CC BY 4.0.
