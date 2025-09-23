

To show that \( f \) is constant under the given conditions, we proceed as follows:

**Step 1:** Define \( g(x) = f(x) - f(0) \).  
- Then \( g(0) = 0 \), and \( g'(x) = f'(x) \).
- The given inequality becomes \( |g'(x)| \leq |g(x)| \) for all \( x \in \mathbb{R} \).

**Step 2:** Apply the integral form of \( g(x) \).  
- Since \( g(0) = 0 \), we have \( g(x) = \int_0^x g'(t) \, dt \).
- Taking absolute values:  
  \[
  |g(x)| \leq \int_0^x |g'(t)| \, dt \leq \int_0^x |g(t)| \, dt \quad \text{for } x \geq 0.
  \]

**Step 3:** Use Grönwall's inequality.  
- The inequality \( |g(x)| \leq \int_0^x |g(t)| \, dt \) satisfies the conditions of Grönwall's inequality with \( C = 0 \) and \( K = 1 \).  
- Grönwall's inequality implies \( |g(x)| \leq 0 \cdot e^{x} = 0 \), so \( g(x) = 0 \) for \( x \geq 0 \).

**Step 4:** Repeat for \( x \leq 0 \).  
- For \( x \leq 0 \), \( |g(x)| \leq \int_x^0 |g(t)| \, dt \).  
- A similar application of Grönwall's inequality (via substitution \( y = -x \)) gives \( g(x) = 0 \) for \( x \leq 0 \).

**Conclusion:**  
Since \( g(x) = 0 \) for all \( x \in \mathbb{R} \), it follows that \( f(x) = f(0) \) for all \( x \). Therefore, \( f \) is constant.

```markdown
**Final Answer**
\boxed{f \text{ is constant}}
```