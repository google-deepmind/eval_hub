

To prove the inequalities, we utilize substitutions and properties of the decreasing function \( f \).

**Upper Bound (\(\leq \int_0^{1/n} f(x)dx\)):**

1. **Substitute \( x = \frac{t}{n} \) in the upper bound integral:**
   \[
   \int_0^{1/n} f(x)dx = \frac{1}{n}\int_0^1 f\left(\frac{t}{n}\right)dt.
   \]

2. **Express the middle integral using \( t = x^n \):**
   \[
   \int_0^1 x^{n-1}f(x)dx = \frac{1}{n}\int_0^1 f(t^{1/n})dt.
   \]

3. **Since \( t^{1/n} \geq \frac{t}{n} \) and \( f \) is decreasing:**
   \[
   f(t^{1/n}) \leq f\left(\frac{t}{n}\right).
   \]

4. **Integrate both sides:**
   \[
   \frac{1}{n}\int_0^1 f(t^{1/n})dt \leq \frac{1}{n}\int_0^1 f\left(\frac{t}{n}\right)dt = \int_0^{1/n} f(x)dx.
   \]

**Lower Bound (\(\geq \int_{1-1/n}^1 f(x)dx\)):**

1. **Substitute \( x = 1 - \frac{t}{n} \) in the lower bound integral:**
   \[
   \int_{1-1/n}^1 f(x)dx = \frac{1}{n}\int_0^1 f\left(1 - \frac{t}{n}\right)dt.
   \]

2. **Use the same substitution for the middle integral:**
   \[
   \int_0^1 x^{n-1}f(x)dx = \frac{1}{n}\int_0^1 f(t^{1/n})dt.
   \]

3. **Since \( t^{1/n} \leq 1 - \frac{t}{n} \) and \( f \) is decreasing:**
   \[
   f(t^{1/n}) \geq f\left(1 - \frac{t}{n}\right).
   \]

4. **Integrate both sides:**
   \[
   \frac{1}{n}\int_0^1 f(t^{1/n})dt \geq \frac{1}{n}\int_0^1 f\left(1 - \frac{t}{n}\right)dt = \int_{1-1/n}^1 f(x)dx.
   \]

Thus, combining both bounds:
\[
\int_{1-\frac{1}{n}}^1 f(x)dx \leq \int_0^1 x^{n-1}f(x)dx \leq \int_0^{\frac{1}{n}}f(x)dx \quad \text{for all } n \in \mathbb{N}.
\]