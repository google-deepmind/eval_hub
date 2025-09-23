

The problem asks whether there exists a sequence \((z_n) \subset \mathbb{R}^2\) such that for every continuous function \(\varphi : \mathbb{R}^2 \rightarrow \mathbb{R}\):

\[
\frac{n}{\pi} \int_{B(z_n, 1/n)} \varphi(x) \, dx \to 0 \quad \text{as } n \to \infty,
\]

while ensuring \(B(z_n, 1/n) \cap B(z_m, 1/m) = \emptyset\) for \(n \neq m\).

### Key Steps and Reasoning:
1. **Integral Approximation**: For a continuous \(\varphi\), the integral over \(B(z_n, 1/n)\) can be approximated by \(\varphi(\xi_n) \cdot \text{Volume}(B(z_n, 1/n))\) for some \(\xi_n \in B(z_n, 1/n)\) (Mean Value Theorem). The volume is \(\pi(1/n)^2 = \pi/n^2\).

2. **Scaled Limit**: Multiplying by \(n/\pi\), the expression becomes:
   \[
   \frac{n}{\pi} \cdot \varphi(\xi_n) \cdot \frac{\pi}{n^2} = \frac{\varphi(\xi_n)}{n}.
   \]
   For this to converge to 0 for **every** continuous \(\varphi\), \(\varphi(\xi_n)/n \to 0\) must hold for all such \(\varphi\).

3. **Constructing a Counterexample**: Suppose such a sequence \((z_n)\) exists. Define a continuous function \(\varphi\) with \(\varphi(x) = n\) on \(B(z_n, 1/(2n))\) and smoothly decaying to 0 outside \(B(z_n, 1/n)\). Since the balls \(B(z_n, 1/n)\) are disjoint, \(\varphi\) is continuous.

4. **Integral for the Counterexample**: Over \(B(z_n, 1/n)\), the integral is at least:
   \[
   \int_{B(z_n, 1/(2n))} \varphi(x) \, dx = n \cdot \text{Volume}(B(z_n, 1/(2n))) = n \cdot \frac{\pi}{(2n)^2} = \frac{\pi}{4n}.
   \]
   Scaling by \(n/\pi\) gives:
   \[
   \frac{n}{\pi} \cdot \frac{\pi}{4n} = \frac{1}{4}.
   \]
   Thus, the limit does not converge to 0 for this \(\varphi\), contradicting the requirement.

### Conclusion:
No such sequence \((z_n)\) exists. For any proposed sequence, we can construct a continuous \(\varphi\) (as above) where the limit fails to be 0. The disjointness condition on the balls does not prevent this contradiction.

**Answer:**  
```latex
\boxed{\text{No}}
```