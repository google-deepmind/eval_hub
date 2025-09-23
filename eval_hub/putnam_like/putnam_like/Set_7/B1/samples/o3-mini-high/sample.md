```markdown
**Solution:**

We are given that \( f: \mathbb{R} \rightarrow \mathbb{R} \) is Lebesgue integrable, which means
\[
\int_{-\infty}^\infty |f(x)|\,dx < \infty.
\]
Define the function \( g \) by
\[
g(x) = \int_{x}^{x+1} f(y)\,dy.
\]

### Step 1. Show that \( g \) is Lebesgue Integrable

First, observe that by the triangle inequality for integrals, for each \( x \in \mathbb{R} \) we have
\[
|g(x)| = \left|\int_{x}^{x+1} f(y)\,dy\right| \le \int_{x}^{x+1} |f(y)|\,dy.
\]
Integrate both sides with respect to \( x \):
\[
\int_{-\infty}^\infty |g(x)|\,dx \le \int_{-\infty}^\infty \left(\int_{x}^{x+1} |f(y)|\,dy\right) dx.
\]
We now apply Fubini's (or Tonelli's) theorem to switch the order of integration. Notice that the region of integration in the \((x,y)\)-plane is
\[
R = \{(x,y) \in \mathbb{R}^2 : x \le y \le x+1\}.
\]
For fixed \( y \), the condition \( x \le y \le x+1 \) is equivalent to
\[
y - 1 \le x \le y.
\]
Thus, by changing the order of integration, we have
\[
\int_{-\infty}^\infty \left(\int_{x}^{x+1} |f(y)|\,dy\right) dx = \int_{-\infty}^\infty \left(\int_{y-1}^{y} |f(y)|\,dx\right) dy.
\]
Since the inner integral is simply
\[
\int_{y-1}^{y} dx = 1,
\]
it follows that
\[
\int_{-\infty}^\infty |g(x)|\,dx \le \int_{-\infty}^\infty |f(y)|\,dy < \infty.
\]
Thus, \( g \) is Lebesgue integrable.

### Step 2. Show that 
\[
\int_{-\infty}^\infty g(x)\,dx = \int_{-\infty}^\infty f(x)\,dx.
\]

To prove the equality, consider
\[
\int_{-\infty}^\infty g(x)\,dx = \int_{-\infty}^\infty \left( \int_{x}^{x+1} f(y)\,dy \right) dx.
\]
Again, using Fubini's theorem, change the order of integration:
\[
\int_{-\infty}^\infty g(x)\,dx = \int_{-\infty}^\infty f(y) \left( \int_{-\infty}^\infty \mathbf{1}_{\{x \le y \le x+1\}}\,dx \right) dy.
\]
For a fixed \( y \), the indicator function \( \mathbf{1}_{\{x \le y \le x+1\}} \) is equal to 1 if and only if \( y \) lies in the interval \([x, x+1]\), which is equivalent to
\[
y-1 \le x \le y.
\]
Thus,
\[
\int_{-\infty}^\infty \mathbf{1}_{\{x \le y \le x+1\}}\,dx = \int_{y-1}^{y} dx = 1.
\]
Therefore, we obtain
\[
\int_{-\infty}^\infty g(x)\,dx = \int_{-\infty}^\infty f(y)\,dy.
\]

### Conclusion

We have shown that the function
\[
g(x) = \int_x^{x+1} f(y)\,dy
\]
is Lebesgue integrable and that
\[
\int_{-\infty}^\infty g(x)\,dx = \int_{-\infty}^\infty f(x)\,dx.
\]
This completes the proof.
```