Okay, here's the solution.

---

**Problem Statement:**

Suppose that $f : \mathbb{R} \rightarrow \mathbb{R}$ is Lebesgue integrable. Show that the function $g : \mathbb{R} \rightarrow \mathbb{R}$ given by
$$
g(x) = \int_x^{x+1} f(y) \, dy
$$
is Lebesgue integrable and that
$$
\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty f(x) \, dx.
$$

---

**Solution:**

We need to prove two things:
1.  $g(x)$ is Lebesgue integrable on $\mathbb{R}$. This means $g$ must be measurable and $\int_{-\infty}^\infty |g(x)| \, dx < \infty$.
2.  $\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty f(x) \, dx$.

Let's rewrite $g(x)$ using the characteristic function $\chi_A(y)$ (which is 1 if $y \in A$ and 0 otherwise):
$$
g(x) = \int_{-\infty}^\infty f(y) \chi_{[x, x+1]}(y) \, dy
$$
The condition $y \in [x, x+1]$ is equivalent to $x \le y \le x+1$, which is also equivalent to $y-1 \le x \le y$. So, $\chi_{[x, x+1]}(y) = \chi_{[y-1, y]}(x)$.
$$
g(x) = \int_{-\infty}^\infty f(y) \chi_{[y-1, y]}(x) \, dy
$$

**Part 1: Integrability of g(x)**

First, we show that $g(x)$ is measurable. We can show that $g(x)$ is actually continuous. Let $x \in \mathbb{R}$ and $h \in \mathbb{R}$.
$$
g(x+h) - g(x) = \int_{x+h}^{x+h+1} f(y) \, dy - \int_x^{x+1} f(y) \, dy
$$
$$
g(x+h) - g(x) = \int_{-\infty}^\infty f(y) (\chi_{[x+h, x+h+1]}(y) - \chi_{[x, x+1]}(y)) \, dy
$$
Taking the absolute value:
$$
|g(x+h) - g(x)| \le \int_{-\infty}^\infty |f(y)| |\chi_{[x+h, x+h+1]}(y) - \chi_{[x, x+1]}(y)| \, dy
$$
The term $|\chi_{[x+h, x+h+1]}(y) - \chi_{[x, x+1]}(y)|$ is non-zero only on the symmetric difference of the intervals $[x, x+1]$ and $[x+h, x+h+1]$.
If $h > 0$, this symmetric difference is $[x, x+h) \cup (x+1, x+h+1]$.
If $h < 0$, this symmetric difference is $[x+h, x) \cup (x+h+1, x+1]$.
In either case, the measure of the symmetric difference is $2|h|$.

Let $F(z) = \int_{-\infty}^z |f(y)| \, dy$. Since $f$ is Lebesgue integrable, $|f|$ is also integrable, and $F$ is an absolutely continuous function. In particular, $F$ is continuous.
For $h > 0$:
$$
|g(x+h) - g(x)| \le \int_x^{x+h} |f(y)| \, dy + \int_{x+1}^{x+h+1} |f(y)| \, dy
$$
As $h \to 0^+$, $\int_x^{x+h} |f(y)| \, dy \to 0$ and $\int_{x+1}^{x+h+1} |f(y)| \, dy \to 0$ because the integral of an integrable function over an interval of vanishing measure tends to zero (this follows from the absolute continuity of the indefinite integral).
A similar argument holds for $h \to 0^-$.
Thus, $\lim_{h \to 0} |g(x+h) - g(x)| = 0$, which means $g(x)$ is continuous for all $x \in \mathbb{R}$. Since continuous functions are Borel measurable, and Borel sets are Lebesgue measurable, $g(x)$ is Lebesgue measurable.

Next, we show that $\int_{-\infty}^\infty |g(x)| \, dx < \infty$.
$$
|g(x)| = \left| \int_x^{x+1} f(y) \, dy \right| \le \int_x^{x+1} |f(y)| \, dy
$$
Now, integrate $|g(x)|$ over $\mathbb{R}$:
$$
\int_{-\infty}^\infty |g(x)| \, dx \le \int_{-\infty}^\infty \left( \int_x^{x+1} |f(y)| \, dy \right) \, dx
$$
The expression inside the outer integral can be written using the characteristic function:
$$
\int_x^{x+1} |f(y)| \, dy = \int_{-\infty}^\infty |f(y)| \chi_{[x, x+1]}(y) \, dy
$$
So, we have a double integral:
$$
\int_{-\infty}^\infty |g(x)| \, dx \le \int_{-\infty}^\infty \left( \int_{-\infty}^\infty |f(y)| \chi_{[x, x+1]}(y) \, dy \right) \, dx
$$
The integrand $|f(y)| \chi_{[x, x+1]}(y)$ is a non-negative measurable function on $\mathbb{R}^2$ (since $f$ is measurable, $|f|$ is measurable, $\chi_{[x, x+1]}(y)$ is measurable as a function of $(x,y)$). Therefore, by Tonelli's Theorem, we can switch the order of integration:
$$
\int_{-\infty}^\infty |g(x)| \, dx \le \int_{-\infty}^\infty \left( \int_{-\infty}^\infty |f(y)| \chi_{[x, x+1]}(y) \, dx \right) \, dy
$$
Using the equivalence $\chi_{[x, x+1]}(y) = \chi_{[y-1, y]}(x)$:
$$
\int_{-\infty}^\infty |g(x)| \, dx \le \int_{-\infty}^\infty \left( \int_{-\infty}^\infty |f(y)| \chi_{[y-1, y]}(x) \, dx \right) \, dy
$$
$$
\int_{-\infty}^\infty |g(x)| \, dx \le \int_{-\infty}^\infty |f(y)| \left( \int_{-\infty}^\infty \chi_{[y-1, y]}(x) \, dx \right) \, dy
$$
The inner integral is the measure of the interval $[y-1, y]$:
$$
\int_{-\infty}^\infty \chi_{[y-1, y]}(x) \, dx = \int_{y-1}^y 1 \, dx = y - (y-1) = 1
$$
Substituting this back:
$$
\int_{-\infty}^\infty |g(x)| \, dx \le \int_{-\infty}^\infty |f(y)| \cdot 1 \, dy = \int_{-\infty}^\infty |f(y)| \, dy
$$
Since $f$ is Lebesgue integrable, $\int_{-\infty}^\infty |f(y)| \, dy < \infty$.
Therefore, $\int_{-\infty}^\infty |g(x)| \, dx < \infty$.
Since $g(x)$ is measurable and $\int_{-\infty}^\infty |g(x)| \, dx < \infty$, $g(x)$ is Lebesgue integrable.

**Part 2: Evaluating the Integral of g(x)**

We want to calculate $\int_{-\infty}^\infty g(x) \, dx$.
$$
\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty \left( \int_x^{x+1} f(y) \, dy \right) \, dx
$$
$$
\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty \left( \int_{-\infty}^\infty f(y) \chi_{[x, x+1]}(y) \, dy \right) \, dx
$$
Consider the function $H(x, y) = f(y) \chi_{[x, x+1]}(y)$. We showed in Part 1 that
$$
\int_{-\infty}^\infty \int_{-\infty}^\infty |H(x, y)| \, dy \, dx = \int_{-\infty}^\infty |f(y)| \, dy < \infty
$$
Since the integral of $|H(x,y)|$ over $\mathbb{R}^2$ is finite, $H(x,y)$ is integrable on $\mathbb{R}^2$. Therefore, we can apply Fubini's Theorem to switch the order of integration:
$$
\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty \left( \int_{-\infty}^\infty f(y) \chi_{[x, x+1]}(y) \, dx \right) \, dy
$$
Again, using $\chi_{[x, x+1]}(y) = \chi_{[y-1, y]}(x)$:
$$
\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty \left( \int_{-\infty}^\infty f(y) \chi_{[y-1, y]}(x) \, dx \right) \, dy
$$
$$
\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty f(y) \left( \int_{-\infty}^\infty \chi_{[y-1, y]}(x) \, dx \right) \, dy
$$
As calculated before, the inner integral is $\int_{y-1}^y 1 \, dx = 1$.
$$
\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty f(y) \cdot 1 \, dy = \int_{-\infty}^\infty f(y) \, dy
$$
Since the variable of integration is a dummy variable, we can write:
$$
\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty f(x) \, dx
$$

**Conclusion:**

We have shown that $g(x)$ is continuous (and therefore measurable) and that $\int_{-\infty}^\infty |g(x)| \, dx \le \int_{-\infty}^\infty |f(x)| \, dx < \infty$, which proves that $g(x)$ is Lebesgue integrable. We have also shown, using Fubini's Theorem, that $\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty f(x) \, dx$.