```markdown
We wish to show that if a continuous function 
\[
f: \mathbb{R}^2 \to \mathbb{R}
\]
satisfies
\[
\int_{B(x_0,r)} f(x) \, dx = 0
\]
for every \( x_0 \in \mathbb{R}^2 \) (with \( B(x_0,r) \) denoting the open ball of radius \( r > 0 \) centered at \( x_0 \)), then
\[
f \equiv 0.
\]

### Proof by Contradiction

Assume, to the contrary, that \( f \) is not identically zero. Then there exists a point \( x_1 \in \mathbb{R}^2 \) such that \( f(x_1) \neq 0 \).

#### Case 1. \( f(x_1) > 0 \)

Since \( f \) is continuous, there exists a small radius \( \delta > 0 \) such that
\[
f(x) > \frac{f(x_1)}{2} > 0 \quad \text{for all } x \in B(x_1,\delta).
\]
The ball \( B(x_1,\delta) \) has positive area; call this area \( A > 0 \). Now, choose any point \( x_0 \) in \( \mathbb{R}^2 \) so that
\[
B(x_1,\delta) \subset B(x_0, r).
\]
This is possible provided that \( x_0 \) is chosen in a suitable neighborhood (for example, if \( \delta < r \), then any \( x_0 \) in \( B(x_1, r-\delta) \) will do).

Then, we obtain
\[
\int_{B(x_0, r)} f(x) \, dx \geq \int_{B(x_1, \delta)} f(x) \, dx \geq \frac{f(x_1)}{2} \cdot A > 0.
\]
However, by hypothesis, the integral over any ball \( B(x_0, r) \) must be zero, which is a contradiction.

#### Case 2. \( f(x_1) < 0 \)

A similar argument applies. By continuity, there exists \( \delta > 0 \) and a neighborhood around \( x_1 \) such that
\[
f(x) < \frac{f(x_1)}{2} < 0 \quad \text{for all } x \in B(x_1, \delta).
\]
Then, for an appropriate choice of \( x_0 \),
\[
\int_{B(x_0, r)} f(x) \, dx \leq \int_{B(x_1, \delta)} f(x) \, dx < 0,
\]
again contradicting the hypothesis that the integral is zero.

### Conclusion

Since both cases lead to a contradiction, no point \( x \) in \( \mathbb{R}^2 \) can satisfy \( f(x) \neq 0 \). Therefore, we must have
\[
f(x) = 0 \quad \text{for all } x \in \mathbb{R}^2,
\]
i.e., \( f \equiv 0 \).

---

### Fourier Analysis Approach (Alternative)

An alternative method uses convolution and the Fourier transform:

1. Notice that the condition
   \[
   \int_{B(x_0, r)} f(x) \, dx = 0 \quad \text{for every } x_0 \in \mathbb{R}^2
   \]
   is equivalent to saying that the convolution
   \[
   (\chi_{B(0,r)} * f)(x) = 0 \quad \text{for all } x \in \mathbb{R}^2,
   \]
   where \(\chi_{B(0,r)}\) is the indicator function of the ball \(B(0,r)\).

2. Taking the Fourier transform yields
   \[
   \widehat{\chi_{B(0,r)} * f}(\xi) = \widehat{\chi_{B(0,r)}}(\xi) \, \widehat{f}(\xi) = 0 \quad \text{for all } \xi \in \mathbb{R}^2.
   \]

3. The Fourier transform \(\widehat{\chi_{B(0,r)}}(\xi)\) is a radial function (expressible in terms of Bessel functions) and is not identically zero. Its zero set has no accumulation point, so it cannot vanish on an open set.

4. It follows that
   \[
   \widehat{f}(\xi) = 0 \quad \text{for all } \xi \in \mathbb{R}^2.
   \]

5. By the injectivity of the Fourier transform on suitable function spaces, \( f \equiv 0 \).

---

### Final Answer

Yes, the given condition implies that \( f \equiv 0 \).
```