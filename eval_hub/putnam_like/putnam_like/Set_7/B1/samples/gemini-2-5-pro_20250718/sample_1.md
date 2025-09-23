Of course. Here is a detailed, step-by-step solution to the problem.

### Preliminaries

We are given that $f : \mathbb{R} \rightarrow \mathbb{R}$ is a Lebesgue integrable function. By definition, this means that $f$ is a measurable function and the Lebesgue integral of its absolute value is finite:
$$
\int_{-\infty}^\infty |f(x)| \, dx < \infty
$$
The function $g : \mathbb{R} \rightarrow \mathbb{R}$ is defined as:
$$
g(x) = \int_x^{x+1} f(y) \, dy
$$
We need to prove two things:
1.  $g$ is Lebesgue integrable, i.e., $\int_{-\infty}^\infty |g(x)| \, dx < \infty$.
2.  The integrals are equal, i.e., $\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty f(x) \, dx$.

The core of this proof will rely on the Fubini-Tonelli theorem, which allows us to change the order of integration in a double integral under certain conditions.

### Part 1: Showing that $g$ is Lebesgue integrable

To show that $g$ is Lebesgue integrable, we must show that $\int_{-\infty}^\infty |g(x)| \, dx$ is finite.

**Step 1: Express the integral and apply the triangle inequality.**
We start with the integral of $|g(x)|$:
$$
\int_{-\infty}^\infty |g(x)| \, dx = \int_{-\infty}^\infty \left| \int_x^{x+1} f(y) \, dy \right| \, dx
$$
Using the triangle inequality for integrals, which states that $|\int_I h(y) dy| \le \int_I |h(y)| dy$, we have:
$$
\left| \int_x^{x+1} f(y) \, dy \right| \le \int_x^{x+1} |f(y)| \, dy
$$
Substituting this into our main integral gives us an upper bound:
$$
\int_{-\infty}^\infty |g(x)| \, dx \le \int_{-\infty}^\infty \left( \int_x^{x+1} |f(y)| \, dy \right) \, dx
$$

**Step 2: Rewrite the iterated integral using a characteristic function.**
The iterated integral on the right-hand side can be viewed as a double integral over a region in the $xy$-plane. We can make this explicit by using a characteristic function. Let $\chi_A$ be the characteristic function of a set $A$. Then $\int_x^{x+1} |f(y)| \, dy = \int_{-\infty}^\infty |f(y)| \chi_{[x, x+1]}(y) \, dy$.
So our inequality becomes:
$$
\int_{-\infty}^\infty |g(x)| \, dx \le \int_{-\infty}^\infty \left( \int_{-\infty}^\infty |f(y)| \chi_{[x, x+1]}(y) \, dy \right) \, dx
$$
This is a double integral of the function $H(x,y) = |f(y)| \chi_{[x, x+1]}(y)$ over $\mathbb{R}^2$.

**Step 3: Apply Tonelli's Theorem.**
The function $H(x,y)$ is non-negative because $|f(y)| \ge 0$ and $\chi_{[x, x+1]}(y) \ge 0$. Since $f$ is measurable, $|f|$ is also measurable. The function $(x,y) \mapsto \chi_{[x,x+1]}(y)$ is measurable on $\mathbb{R}^2$. Therefore, their product $H(x,y)$ is a non-negative measurable function on $\mathbb{R}^2$.
Tonelli's theorem states that for a non-negative measurable function on a product space, the iterated integrals are equal, regardless of their value (finite or infinite). Thus, we can switch the order of integration:
$$
\int_{-\infty}^\infty \left( \int_{-\infty}^\infty |f(y)| \chi_{[x, x+1]}(y) \, dy \right) \, dx = \int_{-\infty}^\infty \left( \int_{-\infty}^\infty |f(y)| \chi_{[x, x+1]}(y) \, dx \right) \, dy
$$

**Step 4: Evaluate the swapped integral.**
Let's evaluate the inner integral on the right-hand side with respect to $x$:
$$
\int_{-\infty}^\infty |f(y)| \chi_{[x, x+1]}(y) \, dx
$$
For a fixed $y$, $|f(y)|$ is a constant with respect to $x$. So we have:
$$
|f(y)| \int_{-\infty}^\infty \chi_{[x, x+1]}(y) \, dx
$$
The characteristic function $\chi_{[x, x+1]}(y)$ is 1 if $x \le y \le x+1$, and 0 otherwise. We are integrating with respect to $x$ for a fixed $y$. We need to find the range of $x$ for which the condition $x \le y \le x+1$ holds. This is equivalent to the pair of inequalities:
1.  $x \le y$
2.  $y \le x+1 \implies y-1 \le x$

Combining these, we get $y-1 \le x \le y$. So, for a fixed $y$, the integrand $\chi_{[x, x+1]}(y)$ is 1 only when $x$ is in the interval $[y-1, y]$, and 0 otherwise. The inner integral becomes:
$$
|f(y)| \int_{y-1}^y 1 \, dx = |f(y)| \cdot [x]_{y-1}^y = |f(y)| \cdot (y - (y-1)) = |f(y)| \cdot 1 = |f(y)|
$$
Now, we substitute this result back into the outer integral:
$$
\int_{-\infty}^\infty |f(y)| \, dy
$$

**Step 5: Conclude the integrability of g.**
Putting everything together, we have shown:
$$
\int_{-\infty}^\infty |g(x)| \, dx \le \int_{-\infty}^\infty \left( \int_x^{x+1} |f(y)| \, dy \right) \, dx = \int_{-\infty}^\infty |f(y)| \, dy
$$
Since $f$ is Lebesgue integrable, we are given that $\int_{-\infty}^\infty |f(y)| \, dy < \infty$. Therefore,
$$
\int_{-\infty}^\infty |g(x)| \, dx < \infty
$$
This shows that $g(x)$ is Lebesgue integrable.

---

### Part 2: Showing the equality of the integrals

Now we show that $\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty f(x) \, dx$.

**Step 1: Express the integral of g(x) as a double integral.**
We start with the integral we want to evaluate:
$$
\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty \left( \int_x^{x+1} f(y) \, dy \right) \, dx
$$
As before, we can write this as a double integral using a characteristic function:
$$
\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty \left( \int_{-\infty}^\infty f(y) \chi_{[x, x+1]}(y) \, dy \right) \, dx
$$

**Step 2: Apply Fubini's Theorem.**
Let the integrand be $F(x,y) = f(y) \chi_{[x, x+1]}(y)$. Fubini's theorem allows us to switch the order of integration for an integrable function. A function $F(x,y)$ is integrable on $\mathbb{R}^2$ if $\iint_{\mathbb{R}^2} |F(x,y)| \, dA < \infty$.
Let's check this condition:
$$
\iint_{\mathbb{R}^2} |F(x,y)| \, dA = \int_{-\infty}^\infty \int_{-\infty}^\infty |f(y) \chi_{[x, x+1]}(y)| \, dx \, dy = \int_{-\infty}^\infty \int_{-\infty}^\infty |f(y)| \chi_{[x, x+1]}(y) \, dx \, dy
$$
This is precisely the integral we evaluated in Part 1 using Tonelli's theorem. We found that:
$$
\int_{-\infty}^\infty \int_{-\infty}^\infty |f(y)| \chi_{[x, x+1]}(y) \, dx \, dy = \int_{-\infty}^\infty |f(y)| \, dy
$$
Since $f$ is Lebesgue integrable, this value is finite. Thus, the condition for Fubini's theorem is satisfied.

**Step 3: Swap the order of integration and evaluate.**
By Fubini's theorem, we can swap the order of integration:
$$
\int_{-\infty}^\infty \left( \int_{-\infty}^\infty f(y) \chi_{[x, x+1]}(y) \, dy \right) \, dx = \int_{-\infty}^\infty \left( \int_{-\infty}^\infty f(y) \chi_{[x, x+1]}(y) \, dx \right) \, dy
$$
Let's evaluate the new inner integral with respect to $x$. For a fixed $y$, $f(y)$ is a constant:
$$
f(y) \int_{-\infty}^\infty \chi_{[x, x+1]}(y) \, dx
$$
As established in Part 1, the integral $\int_{-\infty}^\infty \chi_{[x, x+1]}(y) \, dx$ evaluates to 1 because the condition $x \le y \le x+1$ is equivalent to $x \in [y-1, y]$.
So the inner integral is $f(y) \cdot 1 = f(y)$.

Substituting this back into the outer integral, we get:
$$
\int_{-\infty}^\infty f(y) \, dy
$$

**Step 4: Conclude the equality.**
We have shown that:
$$
\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty f(y) \, dy
$$
Since the variable of integration is a dummy variable, we can write $\int_{-\infty}^\infty f(y) \, dy = \int_{-\infty}^\infty f(x) \, dx$.
Therefore,
$$
\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty f(x) \, dx
$$

### Summary of Results
1.  We showed that $g$ is Lebesgue integrable by bounding its absolute integral by the integral of $|f|$:
    $$ \int_{-\infty}^\infty |g(x)| \, dx \le \int_{-\infty}^\infty |f(x)| \, dx < \infty $$
2.  We showed the equality of the integrals by applying Fubini's theorem, which was justified by the calculation in the first part:
    $$ \int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty \left( \int_x^{x+1} f(y) \, dy \right) dx = \int_{-\infty}^\infty f(x) \, dx $$

This completes the proof.