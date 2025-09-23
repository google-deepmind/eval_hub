```markdown
# Solution

Let the (unknown) bias of the coin be a random variable \(p\sim \mathrm{Uniform}(0,1)\).  Conditioned on \(p\), the number of tosses \(N\) until the first heads is a geometric random variable with success probability \(p\).  

---

## 1. Conditional expectation

For a fixed \(p\), one has
\[
  \mathbb{E}[\,N\mid p\,]
  \;=\;\frac1p.
\]
Thus by the law of total expectation,
\[
  \mathbb{E}[N]
  \;=\;\mathbb{E}\bigl[\mathbb{E}[N\mid p]\bigr]
  \;=\;\mathbb{E}\!\bigl[\tfrac1p\bigr]
  \;=\;\int_{0}^{1}\frac{1}{p}\,dp
  \;=\;\infty.
\]
Since \(\displaystyle\int_{0}^{1}\frac{1}{p}\,dp\) diverges, the overall expected number of tosses is infinite.

---

## 2. Tail‐sum representation

Alternatively, one can use the identity
\[
  \mathbb{E}[N]
  \;=\;\sum_{n=0}^{\infty}\Pr(N>n).
\]
Observe that, given \(p\),
\[
  \Pr(N>n\mid p)\;=\;(1-p)^{n},
\]
so averaging over \(p\sim\mathrm{Uniform}(0,1)\) gives
\[
  \Pr(N>n)
  \;=\;\int_{0}^{1}(1-p)^{n}\,dp
  \;=\;\frac{1}{n+1}.
\]
Hence
\[
  \mathbb{E}[N]
  \;=\;\sum_{n=0}^{\infty}\frac{1}{n+1}
  \;=\;\sum_{k=1}^{\infty}\frac{1}{k}
  \;=\;\infty.
\]

---

**Conclusion.**  
Because \(\mathbb{E}[N]=\displaystyle\int_{0}^{1}\tfrac{1}{p}\,dp\) diverges (or equivalently because the harmonic series \(\sum1/k\) diverges), the expected number of tosses to get the first heads is infinite.
```